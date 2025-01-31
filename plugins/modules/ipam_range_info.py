#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_range_info
short_description: Retrieves a Range
description:
    - Retrieves information about existing Ranges.
    - A Range object represents a set of contiguous IP addresses in the same IP space with no gap.
    - They are expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management.
    - The start and end values are not required to align with CIDR boundaries.
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
    inherit:
        description:
            - Return inheritance information
        type: str
        required: false
        choices:
            - full
            - partial
            - none
        default: full
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
"""

EXAMPLES = r"""
  - name: Get range information by ID
    infoblox.bloxone.ipam_range_info:
      id: "{{range.id}}"

  - name: Get range information with filters
    infoblox.bloxone.ipam_range_info:
      filters:
        start: "192.168.1.0"
        end: "192.168.1.255"
        space: "{{ ip_space.id }}"

  - name: Get range information with filters (eg. start , end)
    infoblox.bloxone.ipam_range_info:
      filter_query: "start=='10.0.0.1' and end=='10.0.0.100'"

  - name: Get range information with tag filters
    infoblox.bloxone.ipam_range_info:
        tag_filters:
          location: "site-1"
"""

RETURN = r"""
id:
    description:
        - ID of the Range object
    type: str
    returned: Always
objects:
    description:
        - Range object
    type: list
    elements: dict
    returned: Always
    contains:
        comment:
            description:
                - "The description for the range. May contain 0 to 1024 characters. Can include UTF-8."
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
        dhcp_host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        dhcp_options:
            description:
                - "The list of DHCP options. May be either a specific option or a group of options."
            type: list
            returned: Always
            elements: dict
            contains:
                group:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_code:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_value:
                    description:
                        - "The option value."
                    type: str
                    returned: Always
                type:
                    description:
                        - "The type of item."
                        - "Valid values are:"
                        - "* I(group)"
                        - "* I(option)"
                    type: str
                    returned: Always
        disable_dhcp:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        end:
            description:
                - "The end IP address of the range."
            type: str
            returned: Always
        exclusion_ranges:
            description:
                - "The list of all exclusion ranges in the scope of the range."
            type: list
            returned: Always
            elements: dict
            contains:
                comment:
                    description:
                        - "The description for the exclusion range. May contain 0 to 1024 characters. Can include UTF-8."
                    type: str
                    returned: Always
                end:
                    description:
                        - "The end address of the exclusion range."
                    type: str
                    returned: Always
                start:
                    description:
                        - "The start address of the exclusion range."
                    type: str
                    returned: Always
        filters:
            description:
                - "The list of all allow/deny filters of the range."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "The access type of DHCP filter (I(allow) or I(deny))."
                        - "Defaults to I(allow)."
                    type: str
                    returned: Always
                hardware_filter_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_filter_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_assigned_hosts:
            description:
                - "The list of the inheritance assigned hosts of the object."
            type: list
            returned: Always
            elements: dict
            contains:
                display_name:
                    description:
                        - "The human-readable display name for the host referred to by I(ophid)."
                    type: str
                    returned: Always
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                ophid:
                    description:
                        - "The on-prem host ID."
                    type: str
                    returned: Always
        inheritance_parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The DHCP inheritance configuration for the range."
            type: dict
            returned: Always
            contains:
                dhcp_options:
                    description:
                        - "The inheritance configuration for the I(dhcp_options) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(block): Don't use the inherited value."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited DHCP option values."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(block): Don't use the inherited value."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value for the DHCP option."
                                    type: dict
                                    returned: Always
                                    contains:
                                        option:
                                            description:
                                                - "Option inherited from the ancestor."
                                            type: dict
                                            returned: Always
                                            contains:
                                                group:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_code:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_value:
                                                    description:
                                                        - "The option value."
                                                    type: str
                                                    returned: Always
                                                type:
                                                    description:
                                                        - "The type of item."
                                                        - "Valid values are:"
                                                        - "* I(group)"
                                                        - "* I(option)"
                                                    type: str
                                                    returned: Always
                                        overriding_group:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
        name:
            description:
                - "The name of the range. May contain 1 to 256 characters. Can include UTF-8."
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
        space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        space_name:
            description:
                - "The name of the IP Space the range belongs to."
            type: str
            returned: Always
        start:
            description:
                - "The start IP address of the range."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the range in JSON format."
            type: dict
            returned: Always
        threshold:
            description:
                - "The utilization threshold settings for the range."
            type: dict
            returned: Always
            contains:
                enabled:
                    description:
                        - "Indicates whether the utilization threshold for IP addresses is enabled or not."
                    type: bool
                    returned: Always
                high:
                    description:
                        - "The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
                low:
                    description:
                        - "The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        utilization:
            description:
                - "The utilization statistics of IPV4 addresses for the range."
            type: dict
            returned: Always
            contains:
                abandon_utilization:
                    description:
                        - "The percentage of abandoned IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
                abandoned:
                    description:
                        - "The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client)."
                    type: str
                    returned: Always
                dynamic:
                    description:
                        - "The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases."
                    type: str
                    returned: Always
                free:
                    description:
                        - "The number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                static:
                    description:
                        - "The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) = I(used) - I(dynamic)."
                    type: str
                    returned: Always
                total:
                    description:
                        - "The total number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                used:
                    description:
                        - "The number of IP addresses used in the scope of the object."
                    type: str
                    returned: Always
                utilization:
                    description:
                        - "The percentage of used IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
        utilization_v6:
            description:
                - "The utilization of IPV6 addresses in the range."
            type: dict
            returned: Always
            contains:
                abandoned:
                    description: "The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client)."
                    type: str
                    returned: Always
                dynamic:
                    description: "The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases."
                    type: str
                    returned: Always
                static:
                    description: "The number of defined IP addresses such as reservations or DNS records. It can be computed as static = used - dynamic."
                    type: str
                    returned: Always
                total:
                    description: "The total number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                used:
                    description: "The number of IP addresses used in the scope of the object."
                    type: str
                    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from ipam import RangeApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class RangeInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(RangeInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = RangeApi(self.client).read(self.params["id"], inherit="full")
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
                resp = RangeApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str, inherit="full"
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
        inherit=dict(type="str", required=False, choices=["full", "partial", "none"], default="full"),
        tag_filters=dict(type="dict", required=False),
        tag_filter_query=dict(type="str", required=False),
    )

    module = RangeInfoModule(
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
