#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_auth_nsg
short_description: Manage AuthNsg
description:
    - Manage AuthNSG
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    state:
        description:
            - Indicate desired state of the object
        type: str
        required: false
        choices:
            - present
            - absent
        default: present
    comment:
        description:
            - "Optional. Comment for the object."
        type: str
    external_primaries:
        description:
            - "Optional. DNS primaries external to BloxOne DDI. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "Optional. Required only if I(type) is I(server). IP Address of nameserver."
                type: str
            fqdn:
                description:
                    - "Optional. Required only if I(type) is I(server). FQDN of nameserver."
                type: str
            nsg:
                description:
                    - "The resource identifier."
                type: str
            tsig_enabled:
                description:
                    - "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
                type: bool
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Error if empty while I(tsig_enabled) is I(true)."
                type: dict
                suboptions:
                    algorithm:
                        description:
                            - "TSIG key algorithm."
                            - "Possible values:"
                            - "* I(hmac_sha256),"
                            - "* I(hmac_sha1),"
                            - "* I(hmac_sha224),"
                            - "* I(hmac_sha384),"
                            - "* I(hmac_sha512)."
                        type: str
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
            type:
                description:
                    - "Allowed values:"
                    - "* I(nsg),"
                    - "* I(primary)."
                type: str
    external_secondaries:
        description:
            - "DNS secondaries external to BloxOne DDI. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "IP Address of nameserver."
                type: str
            fqdn:
                description:
                    - "FQDN of nameserver."
                type: str
            stealth:
                description:
                    - "If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment."
                    - "Default: I(false)"
                type: bool
            tsig_enabled:
                description:
                    - "If enabled, secondaries will use the configured TSIG key when requesting a zone transfer."
                    - "Default: I(false)"
                type: bool
            tsig_key:
                description:
                    - "TSIG key."
                    - "Error if empty while I(tsig_enabled) is I(true)."
                type: dict
                suboptions:
                    algorithm:
                        description:
                            - "TSIG key algorithm."
                            - "Possible values:"
                            - "* I(hmac_sha256),"
                            - "* I(hmac_sha1),"
                            - "* I(hmac_sha224),"
                            - "* I(hmac_sha384),"
                            - "* I(hmac_sha512)."
                        type: str
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
    internal_secondaries:
        description:
            - "Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant."
        type: list
        elements: dict
        suboptions:
            host:
                description:
                    - "The resource identifier."
                type: str
    name:
        description:
            - "Name of the object."
        type: str
    nsgs:
        description:
            - "The resource identifier."
        type: list
        elements: str
    tags:
        description:
            - "Tagging specifics."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create an Auth NSG
    infoblox.bloxone.dns_auth_nsg:
      name: "example_nsg"
      state: "present"

  - name: Create an Auth NSG with Additional Fields
    infoblox.bloxone.dns_auth_nsg:
      name: "example_nsg"
      comment: "Example Auth NSG"
      external_primaries:
        - address: "1.1.1.1"
          fqdn: "a.com."
          type: "primary"
      state: "present"
      tags:
        location: "site-1"

  - name: Delete the Auth NSG
    infoblox.bloxone.dns_auth_nsg:
      name: "example_nsg"
      state: "absent"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the AuthNsg object
    type: str
    returned: Always
item:
    description:
        - AuthNsg object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for the object."
            type: str
            returned: Always
        external_primaries:
            description:
                - "Optional. DNS primaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Optional. Required only if I(type) is I(server). IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Optional. Required only if I(type) is I(server). FQDN of nameserver."
                    type: str
                    returned: Always
                nsg:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                tsig_enabled:
                    description:
                        - "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
                type:
                    description:
                        - "Allowed values:"
                        - "* I(nsg),"
                        - "* I(primary)."
                    type: str
                    returned: Always
        external_secondaries:
            description:
                - "DNS secondaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "FQDN of nameserver."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                stealth:
                    description:
                        - "If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_enabled:
                    description:
                        - "If enabled, secondaries will use the configured TSIG key when requesting a zone transfer."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        internal_secondaries:
            description:
                - "Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        name:
            description:
                - "Name of the object."
            type: str
            returned: Always
        nsgs:
            description:
                - "The resource identifier."
            type: list
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from dns_config import AuthNSG, AuthNsgApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AuthNsgModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AuthNsgModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = AuthNSG.from_dict(self._payload_params)
        self._existing = None

    @property
    def existing(self):
        return self._existing

    @existing.setter
    def existing(self, value):
        self._existing = value

    @property
    def payload_params(self):
        return self._payload_params

    @property
    def payload(self):
        return self._payload

    def payload_changed(self):
        if self.existing is None:
            # if existing is None, then it is a create operation
            return True

        return self.is_changed(self.existing.model_dump(by_alias=True, exclude_none=True), self.payload_params)

    def find(self):
        if self.params["id"] is not None:
            try:
                resp = AuthNsgApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = AuthNsgApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple AuthNsg: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = AuthNsgApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = AuthNsgApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        AuthNsgApi(self.client).delete(self.existing.id)

    def run_command(self):
        result = dict(changed=False, object={}, id=None)

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            self.existing = self.find()
            item = {}
            if self.params["state"] == "present" and self.existing is None:
                item = self.create()
                result["changed"] = True
                result["msg"] = "AuthNsg created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "AuthNsg updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "AuthNsg deleted"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result["diff"] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result["object"] = item
            result["id"] = (
                self.existing.id if self.existing is not None else item["id"] if (item and "id" in item) else None
            )
        except ApiException as e:
            self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        self.exit_json(**result)


def main():
    module_args = dict(
        id=dict(type="str", required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        comment=dict(type="str"),
        external_primaries=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
                nsg=dict(type="str"),
                tsig_enabled=dict(type="bool"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
                type=dict(type="str"),
            ),
        ),
        external_secondaries=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
                stealth=dict(type="bool"),
                tsig_enabled=dict(type="bool"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
            ),
        ),
        internal_secondaries=dict(
            type="list",
            elements="dict",
            options=dict(
                host=dict(type="str"),
            ),
        ),
        name=dict(type="str"),
        nsgs=dict(type="list", elements="str"),
        tags=dict(type="dict"),
    )

    module = AuthNsgModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
