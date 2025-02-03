#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_delegation
short_description: Manage Delegation
description:
    - Manage Delegation
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
            - "Optional. Comment for zone delegation."
        type: str
    delegation_servers:
        description:
            - "Required. DNS zone delegation servers. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "Optional. IP Address of nameserver."
                    - "Only required when fqdn of a delegation server falls under delegation fqdn"
                type: str
            fqdn:
                description:
                    - "Required. FQDN of nameserver."
                type: str
    disabled:
        description:
            - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating resource records."
        type: bool
    fqdn:
        description:
            - "Delegation FQDN. The FQDN supplied at creation will be converted to canonical form."
            - "Read-only after creation."
        type: str
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
- name: Create an Auth Zone (Delegation requires a parent zone)
  infoblox.bloxone.dns_auth_zone:
    fqdn: example_zone
    primary_type: cloud
    state: present

- name: Create a Delegation
  infoblox.bloxone.dns_delegation:
    fqdn: delegation.example_zone.
    view: default
    delegation_servers:
      - fqdn: ns1.example.com.
        address: 12.0.0.0
    state: present
    tags:
      location: my-location

- name: Delete the DNS Delegation
  infoblox.bloxone.dns_delegation:
    fqdn: delegation.example_zone.
    view: default
    state: absent
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Delegation object
    type: str
    returned: Always
item:
    description:
        - Delegation object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for zone delegation."
            type: str
            returned: Always
        delegation_servers:
            description:
                - "Required. DNS zone delegation servers. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Optional. IP Address of nameserver."
                        - "Only required when fqdn of a delegation server falls under delegation fqdn"
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Required. FQDN of nameserver."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
        disabled:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating resource records."
            type: bool
            returned: Always
        fqdn:
            description:
                - "Delegation FQDN. The FQDN supplied at creation will be converted to canonical form."
                - "Read-only after creation."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol_fqdn:
            description:
                - "Delegation FQDN in punycode."
            type: str
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
        view:
            description:
                - "The resource identifier."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_config import Delegation, DelegationApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class DelegationModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(DelegationModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Delegation.from_dict(self._payload_params)
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
                resp = DelegationApi(self.client).read(self.params["id"], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"fqdn=='{self.params['fqdn']}' and view =='{self.params['view']}'"
            resp = DelegationApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Delegation: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = DelegationApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["fqdn", "view"])

        resp = DelegationApi(self.client).update(id=self.existing.id, body=update_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        DelegationApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Delegation created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Delegation updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Delegation deleted"

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
        delegation_servers=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
            ),
        ),
        disabled=dict(type="bool"),
        fqdn=dict(type="str"),
        parent=dict(type="str"),
        tags=dict(type="dict"),
        view=dict(type="str", required=True),
    )

    module = DelegationModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["fqdn", "delegation_servers", "view"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
