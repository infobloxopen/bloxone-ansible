#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_forward_nsg
short_description: Manage Forward NSG
description:
    - Manage Forward NSG
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
    external_forwarders:
        description:
            - "Optional. External DNS servers to forward to. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "Server IP address."
                type: str
            fqdn:
                description:
                    - "Server FQDN."
                type: str
    forwarders_only:
        description:
            - "Optional. I(true) to only forward."
        type: bool
    hosts:
        description:
            - "The resource identifier."
        type: list
        elements: str
    internal_forwarders:
        description:
            - "The resource identifier."
        type: list
        elements: str
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
  - name: Create a Forward NSG
    infoblox.bloxone.dns_forward_nsg:
      name: "example_nsg"
      state: "present"
      
  - name: Create a Forward NSG with Additional Fields
    infoblox.bloxone.dns_forward_nsg:
      name: "example_nsg"
      comment: "Example Forward NSG"
      external_forwarders:
        - address: "1.1.1.1"
          fqdn: "a.com."
      state: "present"
      tags:
        location: "site-1"
        
  - name: Delete the Forward NSG
    infoblox.bloxone.dns_forward_nsg:
      name: "example_nsg"
      state: "absent"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the ForwardNsg object
    type: str
    returned: Always
item:
    description:
        - ForwardNsg object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for the object."
            type: str
            returned: Always
        external_forwarders:
            description:
                - "Optional. External DNS servers to forward to. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Server IP address."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Server FQDN."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "Server FQDN in punycode."
                    type: str
                    returned: Always
        forwarders_only:
            description:
                - "Optional. I(true) to only forward."
            type: bool
            returned: Always
        hosts:
            description:
                - "The resource identifier."
            type: list
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        internal_forwarders:
            description:
                - "The resource identifier."
            type: list
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
    from dns_config import ForwardNSG, ForwardNsgApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class ForwardNsgModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(ForwardNsgModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = ForwardNSG.from_dict(self._payload_params)
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
                resp = ForwardNsgApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = ForwardNsgApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple ForwardNsg: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = ForwardNsgApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = ForwardNsgApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        ForwardNsgApi(self.client).delete(self.existing.id)

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
                result["msg"] = "ForwardNsg created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "ForwardNsg updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "ForwardNsg deleted"

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
        external_forwarders=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
            ),
        ),
        forwarders_only=dict(type="bool"),
        hosts=dict(type="list", elements="str"),
        internal_forwarders=dict(type="list", elements="str"),
        name=dict(type="str"),
        nsgs=dict(type="list", elements="str"),
        tags=dict(type="dict"),
    )

    module = ForwardNsgModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
