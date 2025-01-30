#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_host
short_description: Manage IPAM host
description:
    - Manage IPAM host
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
    addresses:
        description:
            - "The list of all addresses associated with the IPAM host, which may be in different IP spaces."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "Field usage depends on the operation:"
                    - "* For read operation, I(address) of the I(Address) corresponding to the I(ref) resource."
                    - "* For write operation, I(address) to be created if the I(Address) does not exist. Required if I(ref) is not set on write:"
                    - "* If the I(Address) already exists and is already pointing to the right I(Host), the operation proceeds."
                    - "* If the I(Address) already exists and is pointing to a different _Host, the operation must abort."
                    - "* If the I(Address) already exists and is not pointing to any I(Host), it is linked to the I(Host)."
                type: str
            ref:
                description:
                    - "The resource identifier."
                type: str
            space:
                description:
                    - "The resource identifier."
                type: str
    auto_generate_records:
        description:
            - "This flag specifies if resource records have to be auto generated for the host."
        type: bool
    comment:
        description:
            - "The description for the IPAM host. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    host_names:
        description:
            - "The name records to be generated for the host."
            - "This field is required if I(auto_generate_records) is true."
        type: list
        elements: dict
        suboptions:
            alias:
                description:
                    - "When I(true), the name is treated as an alias."
                type: bool
            name:
                description:
                    - "A name for the host."
                type: str
            primary_name:
                description:
                    - "When I(true), the name field is treated as primary name. There must be one and only one primary name in the list of host names. The primary name will be treated as the canonical name for all the aliases. PTR record will be generated only for the primary name."
                type: bool
            zone:
                description:
                    - "The resource identifier."
                type: str
    name:
        description:
            - "The name of the IPAM host. Must contain 1 to 256 characters. Can include UTF-8."
        type: str
    tags:
        description:
            - "The tags for the IPAM host in JSON format."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: "Create an IP space (required as parent)"
      infoblox.bloxone.ipam_ip_space:
        name: "example_ip_space"
        state: "present"

    - name: "Create a Subnet (required as parent)"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0/24"
        space: "{{ ip_space.id }}"
        state: "present"

    - name: "Create a Host"
      infoblox.bloxone.ipam_host:
        name: "example_host"
        state: "present"

    - name: "Create a Host with Additional Fields"
      infoblox.bloxone.ipam_host:
          name: "example_host"
          addresses:
              - address: "10.0.0.1"
                space: "{{ ip_space.id }}"
          comment: "IPAM Host"
          tags:
             location: "site-1"
          state: "present"

    - name: "Delete a host"
      infoblox.bloxone.ipam_host:
        name: "example_host"
        state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the IPAM host object
    type: str
    returned: Always
item:
    description:
        - IPAM host object
    type: complex
    returned: Always
    contains:
        addresses:
            description:
                - "The list of all addresses associated with the IPAM host, which may be in different IP spaces."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Field usage depends on the operation:"
                        - "* For read operation, I(address) of the I(Address) corresponding to the I(ref) resource."
                        - "* For write operation, I(address) to be created if the I(Address) does not exist. Required if I(ref) is not set on write:"
                        - "* If the I(Address) already exists and is already pointing to the right I(Host), the operation proceeds."
                        - "* If the I(Address) already exists and is pointing to a different _Host, the operation must abort."
                        - "* If the I(Address) already exists and is not pointing to any I(Host), it is linked to the I(Host)."
                    type: str
                    returned: Always
                ref:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                space:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        auto_generate_records:
            description:
                - "This flag specifies if resource records have to be auto generated for the host."
            type: bool
            returned: Always
        comment:
            description:
                - "The description for the IPAM host. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        host_names:
            description:
                - "The name records to be generated for the host."
                - "This field is required if I(auto_generate_records) is true."
            type: list
            returned: Always
            elements: dict
            contains:
                alias:
                    description:
                        - "When I(true), the name is treated as an alias."
                    type: bool
                    returned: Always
                name:
                    description:
                        - "A name for the host."
                    type: str
                    returned: Always
                primary_name:
                    description:
                        - "When I(true), the name field is treated as primary name. There must be one and only one primary name in the list of host names. The primary name will be treated as the canonical name for all the aliases. PTR record will be generated only for the primary name."
                    type: bool
                    returned: Always
                zone:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name:
            description:
                - "The name of the IPAM host. Must contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the IPAM host in JSON format."
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
    from ipam import IpamHost, IpamHostApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class IpamHostModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(IpamHostModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = IpamHost.from_dict(self._payload_params)
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
                resp = IpamHostApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = IpamHostApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple IpamHost: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = IpamHostApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = IpamHostApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        IpamHostApi(self.client).delete(self.existing.id)

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
                result["msg"] = "IpamHost created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "IpamHost updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "IpamHost deleted"

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
        addresses=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                ref=dict(type="str"),
                space=dict(type="str"),
            ),
        ),
        auto_generate_records=dict(type="bool"),
        comment=dict(type="str"),
        host_names=dict(
            type="list",
            elements="dict",
            options=dict(
                alias=dict(type="bool"),
                name=dict(type="str"),
                primary_name=dict(type="bool"),
                zone=dict(type="str"),
            ),
        ),
        name=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = IpamHostModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
