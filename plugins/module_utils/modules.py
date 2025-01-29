# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Infoblox
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import traceback

from ansible.module_utils.basic import AnsibleModule, env_fallback, missing_required_lib

try:
    import bloxone_client

    HAS_BLOXONE_CLIENT = True
    BLOXONE_CLIENT_IMP_ERR = None
except ImportError:
    HAS_BLOXONE_CLIENT = False
    BLOXONE_CLIENT_IMP_ERR = traceback.format_exc()


class BloxoneAnsibleModule(AnsibleModule):
    def __init__(self, *args, **kwargs):
        # Add common arguments to the module argument_spec
        args_full = bloxone_client_common_argument_spec()
        try:
            args_full.update(kwargs["argument_spec"])
        except (TypeError, NameError):
            pass
        kwargs["argument_spec"] = args_full

        super(BloxoneAnsibleModule, self).__init__(*args, **kwargs)
        self._client = None

        if not HAS_BLOXONE_CLIENT:
            self.fail_json(
                msg=missing_required_lib(
                    "bloxone_client",
                    url="https://github.com/infobloxopen/bloxone-python-client",
                ),
                exception=BLOXONE_CLIENT_IMP_ERR,
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


def bloxone_client_common_argument_spec():
    return dict(
        api_key=dict(
            type="str", aliases=["bloxone_api_key"], fallback=(env_fallback, ["BLOXONE_API_KEY"]), no_log=True
        ),
        csp_url=dict(
            type="str",
            aliases=["bloxone_csp_url"],
            fallback=(env_fallback, ["BLOXONE_CSP_URL"]),
            default="https://csp.infoblox.com",
        ),
    )


def _get_client(module):
    config = _get_client_config(module)
    client = bloxone_client.ApiClient(config)
    return client


def _get_client_config(module):
    csp_url = module.params.get("csp_url")
    api_key = module.params.get("api_key")

    # Use None for empty values, so that the client can handle it
    if not csp_url:
        csp_url = None
    if not api_key:
        api_key = None

    config = bloxone_client.Configuration(
        csp_url=csp_url,
        api_key=api_key,
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
