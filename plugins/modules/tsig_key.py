#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: tsig_key
short_description: Manage TSIG Key
description:
    - Manage TSIG Key
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
    algorithm:
        description:
            - "The TSIG key algorithm."
        choices:
            - hmac_sha1
            - hmac_sha224
            - hmac_sha256
            - hmac_sha384
            - hmac_sha512
        type: str
        default: hmac_sha256
    comment:
        description:
            - "The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    name:
        description:
            - "The TSIG key name in the absolute domain name format."
        type: str
        required: true
    secret:
        description:
            - "The TSIG key secret as a Base64 encoded string."
        type: str
    tags:
        description:
            - "The tags for the TSIG key in JSON format."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
- name: Create TSIG Key
  infoblox.bloxone.tsig_key:
    name: "test-tsig-key"
    secret: "rA+n89+aOCjFVNzBPbYkl+j3oQcl4U19JAkCIK9Ad8k="
    algorithm: "hmac_sha512"
    state: present

- name: Create TSIG Key with additional Fields
  infoblox.bloxone.tsig_key:
    name: "test-tsig-key"
    secret: "fA+n89+aOCjFVNzBPbYkl+j3oQcl4U19JAkCIK9Ad8k="
    algorithm: "hmac_sha512"
    state: present
    tags:
      location: "site-1"
      
- name: Create TSIG Key with secret dynamically generated
  infoblox.bloxone.tsig_key:
    name: "test-tsig-key2"
    algorithm: "hmac_sha512"
    state: present
    tags:
      location: "site-1"

- name: Delete TSIG Key
  infoblox.bloxone.tsig_key:
    name: "test-tsig-key"
    state: absent
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the TSIG object
    type: str
    returned: Always
item:
    description:
        - Tsig object
    type: complex
    returned: Always
    contains:
        algorithm:
            description:
                - "The TSIG key algorithm."
                - "Valid values are:"
                - "* I(hmac_sha1)"
                - "* I(hmac_sha224)"
                - "* I(hmac_sha256)"
                - "* I(hmac_sha384)"
                - "* I(hmac_sha512)"
                - "Defaults to I(hmac_sha256)."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name:
            description:
                - "The TSIG key name in the absolute domain name format."
            type: str
            returned: Always
        protocol_name:
            description:
                - "The TSIG key name supplied during a create/update operation that is converted to canonical form in punycode."
            type: str
            returned: Always
        secret:
            description:
                - "The TSIG key secret as a Base64 encoded string."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the TSIG key in JSON format."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from keys import GenerateTsigApi, TsigApi, TSIGKey
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class TsigKeyModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(TsigKeyModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = TSIGKey.from_dict(self._payload_params)
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
                resp = TsigApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = TsigApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Tsig: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        if self.params["secret"] is None:
            # Generate secret dynamically
            api_res = GenerateTsigApi(self.client).generate_tsig(algorithm=self.params["algorithm"])
            if api_res is None:
                self.fail_json(msg="Failed to generate TSIG secret.")
            # Extract and set the secret
            self.payload.secret = api_res.result.secret

        # Perform the create operation
        resp = TsigApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = TsigApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        TsigApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Tsig created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Tsig updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Tsig deleted"

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
        algorithm=dict(
            type="str",
            choices=["hmac_sha1", "hmac_sha224", "hmac_sha256", "hmac_sha384", "hmac_sha512"],
            default="hmac_sha256",
        ),
        comment=dict(type="str"),
        name=dict(type="str", required=True),
        secret=dict(type="str", no_log=True, required=False),
        tags=dict(type="dict"),
    )

    module = TsigKeyModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
