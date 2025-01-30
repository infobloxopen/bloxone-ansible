#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_address_info
short_description: Retrieve an Address
description:
    - Retrieves information about existing Addresses.
    - The Address object represents any single IP address within a given IP space.
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    filters:
        description:
            - Filter dict to filter objects
        type: dict
        required: false
    filter_query:
        description:
            - Filter query to filter objects
        type: str
        required: false
    tag_filters:
        description:
            - Filter dict to filter objects by tags
        type: dict
        required: false
    tag_filter_query:
        description:
            - Filter query to filter objects by tags
        type: str
        required: false

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Get information about the Address by ID
      infoblox.bloxone.ipam_address_info:
        id: "{{ address.id }}"

    - name: Get Address Block information by filters
      infoblox.bloxone.ipam_address_info:
        filters:
          address: "10.0.0.3"
          space: "{{ ip_space.id }}"

    - name: Get information about the Address by tag
      infoblox.bloxone.ipam_address_info:
        tag_filters:
          location : "site-1"

    - name:  Get Address information by filter query
      infoblox.bloxone.ipam_address_info:
        filter_query: "address=='10.0.0.3' and space=='{{ ip_space.id }}'"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Address object
    type: str
    returned: Always
objects:
    description:
        - Address object
    type: list
    elements: dict
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
        external_keys:
            description:
                - "The external keys (source key) for this address in JSON format."
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
    from ipam import AddressApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AddressInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AddressInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = AddressApi(self.client).read(self.params["id"])
            return [resp.result]
        except NotFoundException as e:
            return None

    def find(self):
        if self.params["id"] is not None:
            return self.find_by_id()

        filter_str = None
        if self.params["filters"] is not None:
            filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["filters"].items()])
        elif self.params["filter_query"] is not None:
            filter_str = self.params["filter_query"]

        tag_filter_str = None
        if self.params["tag_filters"] is not None:
            tag_filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["tag_filters"].items()])
        elif self.params["tag_filter_query"] is not None:
            tag_filter_str = self.params["tag_filter_query"]

        all_results = []
        offset = 0

        while True:
            try:
                resp = AddressApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str
                )
                all_results.extend(resp.results)

                if len(resp.results) < self._limit:
                    break
                offset += self._limit

            except ApiException as e:
                self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        return all_results

    def run_command(self):
        result = dict(objects=[])

        if self.check_mode:
            self.exit_json(**result)

        find_results = self.find()

        all_results = []
        for r in find_results:
            all_results.append(r.model_dump(by_alias=True, exclude_none=True))

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=False),
        filters=dict(type="dict", required=False),
        filter_query=dict(type="str", required=False),
        tag_filters=dict(type="dict", required=False),
        tag_filter_query=dict(type="str", required=False),
    )

    module = AddressInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[
            ["id", "filters", "filter_query"],
            ["id", "tag_filters", "tag_filter_query"],
        ],
    )
    module.run_command()


if __name__ == "__main__":
    main()
