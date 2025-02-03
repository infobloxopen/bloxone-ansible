#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_acl
short_description: "Manages a named Access Control List (ACL)"
description:
    - "Manages a named Access Control List (ACL)"
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
            - "Optional. Comment for ACL."
        type: str
    compartment_id:
        description:
            - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
        type: str
    list:
        description:
            - "Optional. Ordered list of access control elements."
            - "Elements are evaluated in order to determine access. If evaluation reaches the end of the list then access is denied."
        type: list
        elements: dict
        suboptions:
            access:
                description:
                    - "Access permission for I(element)."
                    - "Allowed values:"
                    - "* I(allow),"
                    - "* I(deny)."
                type: str
                choices:
                    - allow
                    - deny
                    - ""
            acl:
                description:
                    - "The resource identifier."
                type: str
            address:
                description:
                    - "Optional. Data for I(ip) I(element)."
                    - "Must be empty if I(element) is not I(ip)."
                type: str
            element:
                description:
                    - "Type of AccessList item."
                    - "Allowed values:"
                    - "* I(any),"
                    - "* I(ip),"
                    - "* I(acl),"
                    - "* I(tsig_key)."
                type: str
                choices:
                    - any
                    - ip
                    - acl
                    - tsig_key
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Must be empty if I(element) is not I(tsig_key)."
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
                        choices:
                            - hmac_sha256
                            - hmac_sha1
                            - hmac_sha224
                            - hmac_sha384
                            - hmac_sha512
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
    name:
        description:
            - "ACL object name."
        type: str
    tags:
        description:
            - "Tagging specifics."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create ACL
    infoblox.bloxone.dns_acl:
      name: "example-acl"
      state: "present"

  - name: Create ACL with additional fields
    infoblox.bloxone.dns_acl:
      name: "example-acl"
      comment: "example comment"
      list:
        - access: "allow"
          element: "ip"
          address: "1.1.1.1"
      tags:
        location: "us-west"
      state: "present"

  - name: Delete ACL
    infoblox.bloxone.dns_acl:
      name: "example-acl"
      state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the ACL object
    type: str
    returned: Always
item:
    description:
        - ACL object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for ACL."
            type: str
            returned: Always
        compartment_id:
            description:
                - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        list:
            description:
                - "Optional. Ordered list of access control elements."
                - "Elements are evaluated in order to determine access. If evaluation reaches the end of the list then access is denied."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of AccessList item."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
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
        name:
            description:
                - "ACL object name."
            type: str
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_config import ACL, AclApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AclModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AclModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = ACL.from_dict(self._payload_params)
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
                resp = AclApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = AclApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple ACL: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = AclApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = AclApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        AclApi(self.client).delete(self.existing.id)

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
                result["msg"] = "ACL created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "ACL updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "ACL deleted"

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
        compartment_id=dict(type="str"),
        list=dict(
            type="list",
            elements="dict",
            options=dict(
                access=dict(type="str", choices=["allow", "deny", ""]),
                acl=dict(type="str"),
                address=dict(type="str"),
                element=dict(type="str", choices=["any", "ip", "acl", "tsig_key"]),
                tsig_key=dict(
                    type="dict",
                    options=dict(
                        algorithm=dict(
                            type="str",
                            choices=["hmac_sha256", "hmac_sha1", "hmac_sha224", "hmac_sha384", "hmac_sha512"],
                        ),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                    no_log=True,
                ),
            ),
        ),
        name=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = AclModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
