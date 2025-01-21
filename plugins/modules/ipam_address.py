#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_address
short_description: Manage an Address
description:
    - Manage an Address
    - The Address object represents any single IP address within a given IP space.
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
    address:
        description:
            - "The address in form \"a.b.c.d\"."
        type: str
    comment:
        description:
            - "The description for the address object. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    host:
        description:
            - "The resource identifier."
        type: str
    hwaddr:
        description:
            - "The hardware address associated with this IP address."
        type: str
    interface:
        description:
            - "The name of the network interface card (NIC) associated with the address, if any."
        type: str
    names:
        description:
            - "The list of all names associated with this address."
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - "The name expressed as a single label or FQDN."
                type: str
            type:
                description:
                    - "The origin of the name."
                type: str
    next_available_id:
        description:
            - "The resource identifier for the address block, subnet or range where the next available address should be generated."
        type: str
    parent:
        description:
            - "The resource identifier."
        type: str
    range:
        description:
            - "The resource identifier."
        type: str
    space:
        description:
            - "The resource identifier."
        type: str
    tags:
        description:
            - "The tags for this address in JSON format."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: "Create an IP Space (required as parent)"
      infoblox.bloxone.ipam_ip_space:
        name: "example-ipspace"
        state: "present"
      register: ip_space

    - name: "Create a Subnet (required as parent)"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0/16"
        space: "{{ ip_space.id }}"
        state: "present"
      register: subnet

    - name: Create an Address
      infoblox.bloxone.ipam_address:
        address: "10.0.0.3"
        space: "{{ ip_space.id }}"
        state: "present"
      
    - name: Create an Address with Additional Fields
      infoblox.bloxone.ipam_address:
        address: "10.0.0.3"
        comment: "test comment"
        space: "{{ _ip_space.id }}"
        tags:
            "location": "site 1"
        state: "present"

    - name: Create a Next Available Address in subnet
      infoblox.bloxone.ipam_address:
        space: "{{ _ip_space.id }}"
        next_available_id: "{{ subnet.id }}"
        state: "present"

    - name: Delete an Address
      infoblox.bloxone.ipam_address:
        address: "10.0.0.3"
        space: "{{ ip_space.id }}"
        state: "absent"

"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Address object
    type: str
    returned: Always
item:
    description:
        - Address object
    type: complex
    returned: Always
    contains:
        address:
            description:
                - "The address in form \"a.b.c.d\"."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the address object. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        compartment_id:
            description:
                - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        dhcp_info:
            description:
                - "The DHCP information associated with this object."
            type: dict
            returned: Always
            contains:
                client_hostname:
                    description:
                        - "The DHCP host name associated with this client."
                    type: str
                    returned: Always
                client_hwaddr:
                    description:
                        - "The hardware address associated with this client."
                    type: str
                    returned: Always
                client_id:
                    description:
                        - "The ID associated with this client."
                    type: str
                    returned: Always
                end:
                    description:
                        - "The timestamp at which the I(state), when set to I(leased), will be changed to I(free)."
                    type: str
                    returned: Always
                fingerprint:
                    description:
                        - "The DHCP fingerprint for the associated lease."
                    type: str
                    returned: Always
                iaid:
                    description:
                        - "Identity Association Identifier (IAID) of the lease. Applicable only for DHCPv6."
                    type: int
                    returned: Always
                lease_type:
                    description:
                        - "Lease type. Applicable only for address under DHCP control. The value can be empty for address not under DHCP control."
                        - "Valid values are:"
                        - "* I(DHCPv6NonTemporaryAddress): DHCPv6 non-temporary address (NA)"
                        - "* I(DHCPv6TemporaryAddress): DHCPv6 temporary address (TA)"
                        - "* I(DHCPv6PrefixDelegation): DHCPv6 prefix delegation (PD)"
                        - "* I(DHCPv4): DHCPv4 lease"
                    type: str
                    returned: Always
                preferred_lifetime:
                    description:
                        - "The length of time that a valid address is preferred (i.e., the time until deprecation). When the preferred lifetime expires, the address becomes deprecated on the client. It is still considered leased on the server. Applicable only for DHCPv6."
                    type: str
                    returned: Always
                remain:
                    description:
                        - "The remaining time, in seconds, until which the I(state), when set to I(leased), will remain in that state."
                    type: int
                    returned: Always
                start:
                    description:
                        - "The timestamp at which I(state) was first set to I(leased)."
                    type: str
                    returned: Always
                state:
                    description:
                        - "Indicates the status of this IP address from a DHCP protocol standpoint as:"
                        - "* I(none): Address is not under DHCP control."
                        - "* I(free): Address is under DHCP control but has no lease currently assigned."
                        - "* I(leased): Address is under DHCP control and has a lease currently assigned. The lease details are contained in the matching I(dhcp/lease) resource."
                    type: str
                    returned: Always
                state_ts:
                    description:
                        - "The timestamp at which the I(state) was last reported."
                    type: str
                    returned: Always
        disable_dhcp:
            description:
                - "Read only. Represent the value of the same field in the associated I(dhcp/fixed_address) object."
            type: bool
            returned: Always
        discovery_attrs:
            description:
                - "The discovery attributes for this address in JSON format."
            type: dict
            returned: Always
        discovery_metadata:
            description:
                - "The discovery metadata for this address in JSON format."
            type: dict
            returned: Always
        host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        hwaddr:
            description:
                - "The hardware address associated with this IP address."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        interface:
            description:
                - "The name of the network interface card (NIC) associated with the address, if any."
            type: str
            returned: Always
        names:
            description:
                - "The list of all names associated with this address."
            type: list
            returned: Always
            elements: dict
            contains:
                name:
                    description:
                        - "The name expressed as a single label or FQDN."
                    type: str
                    returned: Always
                type:
                    description:
                        - "The origin of the name."
                    type: str
                    returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol:
            description:
                - "The type of protocol (I(ip4) or I(ip6))."
            type: str
            returned: Always
        range:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        state:
            description:
                - "The state of the address (I(used) or I(free))."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for this address in JSON format."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        usage:
            description:
                - "The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:"
                - "Below are listed some usage indicators with their descriptions :"
                - " I(IPAM) - Address was created by the IPAM component."
                - " I(IPAM), I(RESERVED) - Address was created by the API call I(ipam/address) or I(ipam/host)."
                - " I(IPAM), I(NETWORK) - Address was automatically created by the IPAM component and is the network address of the parent subnet."
                - " I(IPAM), I(BROADCAST) - Address was automatically created by the IPAM component and is the broadcast address of the parent subnet."
                - " I(DHCP) - Address was created by the DHCP component."
                - " I(DHCP), I(FIXEDADDRESS) - Address was created by the API call I(dhcp/fixed_address)."
                - " I(DHCP), I(LEASED) - An active lease for that address was issued by a DHCP server."
                - " I(DHCP), I(DISABLED) - Address is disabled."
                - " I(DNS) - Address is used by one or more DNS records."
                - " I(DISCOVERED) - Address is discovered by some network discovery probe like Network Insight or NetMRI in NIOS."
            type: list
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from ipam import Address, AddressApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AddressModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AddressModule, self).__init__(*args, **kwargs)
        self.next_available_id = self.params.get("next_available_id")

        exclude = ["state", "csp_url", "api_key", "id", "next_available_id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Address.from_dict(self._payload_params)
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
                resp = AddressApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            # If address is None, return None, indicating next_available_address block should be created
            if self.params["address"] is None:
                return None
            filter = f"address=='{self.params['address']}' and space=='{self.params['space']}'"
            resp = AddressApi(self.client).list(filter=filter)
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Address: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        if self.next_available_id is not None:
            naId = f"{self.next_available_id}/nextavailableip"
            self._payload.address = naId

        resp = AddressApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["space"])

        resp = AddressApi(self.client).update(id=self.existing.id, body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        AddressApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Address created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Address updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Address deleted"

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
        address=dict(type="str", required=False),
        next_available_id=dict(type="str", required=False),
        comment=dict(type="str"),
        host=dict(type="str"),
        hwaddr=dict(type="str"),
        interface=dict(type="str"),
        names=dict(
            type="list",
            elements="dict",
            options=dict(
                name=dict(type="str"),
                type=dict(type="str"),
            ),
        ),
        parent=dict(type="str"),
        range=dict(type="str"),
        space=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = AddressModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[["address", "next_available_id"]],
        required_if=[("state", "present", ["space"])],
        required_one_of=[["address", "next_available_id"]],
    )

    module.run_command()


if __name__ == "__main__":
    main()
