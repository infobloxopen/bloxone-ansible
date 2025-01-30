#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_forward_zone
short_description: Manage ForwardZone
description:
    - Manage ForwardZone
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
            - "Optional. Comment for zone configuration."
        type: str
    disabled:
        description:
            - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
        type: bool
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
    forward_only:
        description:
            - "Optional. I(true) to only forward."
        type: bool
    fqdn:
        description:
            - "Zone FQDN. The FQDN supplied at creation will be converted to canonical form."
            - "Read-only after creation."
        type: str
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
    nsgs:
        description:
            - "The resource identifier."
        type: list
        elements: str
    parent:
        description:
            - "The resource identifier."
        type: str
    tags:
        description:
            - "Tagging specifics."
        type: dict
    view:
        description:
            - "The resource identifier."
        type: str
        required: true

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create a Forward Zone
    infoblox.bloxone.dns_forward_zone:
      fqdn: "example_zone."
      state: present

  - name: Create an Forward Zone with Additional Fields
    infoblox.bloxone.dns_forward_zone:
      fqdn: "example_zone."
      comment: "Example Forward Zone"
      disabled: true
      external_forwarders:
       - address: "192.168.10.10"
      notify: true
      state: "present"
      tags:
        location: "site-1"

  - name: Delete the Zone
    infoblox.bloxone.dns_forward_zone:
      name: "example_zone."
      state: "absent"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the ForwardZone object
    type: str
    returned: Always
item:
    description:
        - ForwardZone object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for zone configuration."
            type: str
            returned: Always
        created_at:
            description:
                - "The timestamp when the object has been created."
            type: str
            returned: Always
        disabled:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
            type: bool
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
        forward_only:
            description:
                - "Optional. I(true) to only forward."
            type: bool
            returned: Always
        fqdn:
            description:
                - "Zone FQDN. The FQDN supplied at creation will be converted to canonical form."
                - "Read-only after creation."
            type: str
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
        mapped_subnet:
            description:
                - "Reverse zone network address in the following format: \"ip-address/cidr\". Defaults to empty."
            type: str
            returned: Always
        mapping:
            description:
                - "Read-only. Zone mapping type. Allowed values:"
                - "* I(forward),"
                - "* I(ipv4_reverse)."
                - "* I(ipv6_reverse)."
                - "Defaults to I(forward)."
            type: str
            returned: Always
        nsgs:
            description:
                - "The resource identifier."
            type: list
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol_fqdn:
            description:
                - "Zone FQDN in punycode."
            type: str
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
        updated_at:
            description:
                - "The timestamp when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        view:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        warnings:
            description:
                - "The list of a forward zone warnings."
            type: list
            returned: Always
            elements: dict
            contains:
                message:
                    description:
                        - "Warning message."
                    type: str
                    returned: Always
                name:
                    description:
                        - "Name of a warning."
                    type: str
                    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_config import ForwardZone, ForwardZoneApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class ForwardZoneModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(ForwardZoneModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = ForwardZone.from_dict(self._payload_params)
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
                resp = ForwardZoneApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"fqdn=='{self.params['fqdn']}' and view=='{self.params['view']}'"
            resp = ForwardZoneApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple ForwardZone: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = ForwardZoneApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["fqdn", "view"])

        resp = ForwardZoneApi(self.client).update(id=self.existing.id, body=update_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        ForwardZoneApi(self.client).delete(self.existing.id)

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
                result["msg"] = "ForwardZone created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "ForwardZone updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "ForwardZone deleted"

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
        disabled=dict(type="bool"),
        external_forwarders=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
            ),
        ),
        forward_only=dict(type="bool"),
        fqdn=dict(type="str"),
        hosts=dict(type="list", elements="str"),
        internal_forwarders=dict(type="list", elements="str"),
        nsgs=dict(type="list", elements="str"),
        parent=dict(type="str"),
        tags=dict(type="dict"),
        view=dict(type="str", required=True),
    )

    module = ForwardZoneModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["fqdn", "view"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
