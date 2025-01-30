#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_next_available_ip_info
short_description: Retrieves the Next available IP addresses
description:
    - Retrieves the next available IP addresses in the specified resource
    - The resource can be an address block, subnet or range.
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - "ID of the object."
        type: str
        required: true
    contiguous:
        description:
            - "Indicates whether the IP addresses should belong to a contiguous block."
        type: bool
        default: false
        required: false
    count:
        description:
            - "The number of IP addresses requested."
        type: int
        default: 1
        required: false
            

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Get Information about Next Available IP in Address Block
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _address_block.id }}"
        count: 5

    - name: Get Information about Next Available IP in Address Block Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _address_block.id }}"

    - name: Get Information about Next Available IP in Subnet
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _subnet.id }}"
        count: 5

    - name: Get Information about Next Available IP in Subnet Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _subnet.id }}"
        
    - name: Get Information about Next Available IP in Range
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _range.id }}"
        count: 5
        
    - name: Get Information about Next Available IP in Range Default Count
      infoblox.bloxone.ipam_next_available_ip_info:
        id: "{{ _range.id }}"
   
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Address object
    type: str
    returned: Always
objects:
    description:
        - List of next available ip addresses
    type: list
    elements: str
    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from ipam import AddressBlockApi, RangeApi, SubnetApi
    from universal_ddi_client import ApiException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class NextAvailableIPInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(NextAvailableIPInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find(self):

        all_results = []
        offset = 0

        while True:
            try:
                id = self.params["id"]
                address_str = id.rsplit("/", 1)[0]
                if address_str == "ipam/address_block":
                    resp = AddressBlockApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
                    )
                elif address_str == "ipam/subnet":
                    resp = SubnetApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
                    )

                elif address_str == "ipam/range":
                    resp = RangeApi(self.client).list_next_available_ip(
                        id=id, contiguous=self.params["contiguous"], count=self.params["count"]
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
            # The expected output is a list of addresses as strings.
            # Therefore, we extract only the 'address' field from each object in the results.
            all_results.append(r.address)

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=True),
        contiguous=dict(type="bool", required=False, default=False),
        count=dict(type="int", required=False, default=1),
    )

    module = NextAvailableIPInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    module.run_command()


if __name__ == "__main__":
    main()
