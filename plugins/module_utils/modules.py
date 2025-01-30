# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Infoblox
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import traceback

from ansible.module_utils.basic import AnsibleModule, env_fallback, missing_required_lib

try:
    import universal_ddi_client

    HAS_UNIVERSAL_DDI_CLIENT = True
    UNIVERSAL_DDI_CLIENT_IMP_ERR = None
except ImportError:
    HAS_UNIVERSAL_DDI_CLIENT = False
    UNIVERSAL_DDI_CLIENT_IMP_ERR = traceback.format_exc()


class BloxoneAnsibleModule(AnsibleModule):
    def __init__(self, *args, **kwargs):
        # Add common arguments to the module argument_spec
        args_full = universal_ddi_client_common_argument_spec()
        try:
            args_full.update(kwargs["argument_spec"])
        except (TypeError, NameError):
            pass
        kwargs["argument_spec"] = args_full

        super(BloxoneAnsibleModule, self).__init__(*args, **kwargs)
        self._client = None

        if not HAS_UNIVERSAL_DDI_CLIENT:
            self.fail_json(
                msg=missing_required_lib(
                    "universal_ddi_client",
                    url="https://github.com/infobloxopen/universal-ddi-python-client",
                ),
                exception=UNIVERSAL_DDI_CLIENT_IMP_ERR,
            )

    @property
    def client(self):
        if not self._client:
            self._client = _get_client(self)

        return self._client

    def is_changed(self, existing, payload):
        return _is_changed(existing, payload)

    def validate_readonly_on_update(self, existing, update_body, fields):
        for field in fields:
            if getattr(update_body, field) != getattr(existing, field):
                self.fail_json(msg=f"{field} cannot be updated")
            setattr(update_body, field, None)

        return update_body


def universal_ddi_client_common_argument_spec():
    return dict(
        portal_key=dict(
            type="str",
            aliases=["infoblox_portal_key", "api_key"],
            fallback=(env_fallback, ["INFOBLOX_PORTAL_KEY"]),
            no_log=True,
        ),
        portal_url=dict(
            type="str",
            aliases=["infoblox_portal_url", "csp_url"],
            fallback=(env_fallback, ["INFOBLOX_PORTAL_URL"]),
            default="https://csp.infoblox.com",
        ),
    )


def _get_client(module):
    config = _get_client_config(module)
    client = universal_ddi_client.ApiClient(config)
    return client


def _get_client_config(module):
    portal_url = module.params.get("portal_url")
    portal_key = module.params.get("portal_key")

    # Use None for empty values, so that the client can handle it
    if not portal_url:
        portal_url = None
    if not portal_key:
        portal_key = None

    config = universal_ddi_client.Configuration(
        csp_url=portal_url,
        api_key=portal_key,
        client_name="ansible",
    )
    config.debug = True
    return config


def _is_changed(existing, payload):
    """
    Check if the existing object is different from the payload.
    The payload keys that are not none are considered for comparison, others are ignored.
    If the value is a complex object, the comparison is done recursively.

    :param existing:
    :param payload:
    :return:
    """
    changed = False
    for k, v in payload.items():
        if v is not None:
            if k not in existing:
                changed = True
            elif isinstance(v, list):
                # If the order of the list is different, it is considered as changed
                if len(v) != len(existing[k]):
                    changed = True
                else:
                    for i in range(len(v)):
                        if _is_changed(existing[k][i], v[i]):
                            changed = True
            elif isinstance(v, dict):
                changed = _is_changed(existing[k], v)
            elif existing[k] != v:
                changed = True
        if changed:
            break

    return changed
