#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dhcp_fixed_address_info
short_description: Manage FixedAddress
description:
    - Manage FixedAddress
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
- name: Retrieve a fixed address by ID
  dhcp_fixed_address_info:
    id: "fixed_address_id"
  register: result

- name: Retrieve fixed addresses with specific filters
  dhcp_fixed_address_info:
    filters:
      address: "192.168.1.10"
      hostname: "example-host"
  register: result

- name: Retrieve fixed addresses using a filter query
  dhcp_fixed_address_info:
    filter_query: "address=='192.168.1.10' and hostname=='example-host'"
  register: result

- name: Retrieve fixed addresses with tag filters
  dhcp_fixed_address_info:
    tag_filters:
      environment: "production"
      role: "webserver"
  register: result

- name: Retrieve fixed addresses using a tag filter query
  dhcp_fixed_address_info:
    tag_filter_query: "environment=='production' and role=='webserver'"
  register: result

- name: Retrieve fixed addresses with partial inheritance
  dhcp_fixed_address_info:
    inherit: "partial"
  register: result
"""

RETURN = r"""
id:
    description:
        - ID of the FixedAddress object
    type: str
    returned: Always
objects:
    description:
        - FixedAddress object
    type: list
    elements: dict
    returned: Always
    contains:
        address:
            description:
                - "The reserved address."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the fixed address. May contain 0 to 1024 characters. Can include UTF-8."
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
                - "Optional. I(true) to disable object. The fixed address is converted to an exclusion when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        header_option_filename:
            description:
                - "The configuration for header option filename field."
            type: str
            returned: Always
        header_option_server_address:
            description:
                - "The configuration for header option server address field."
            type: str
            returned: Always
        header_option_server_name:
            description:
                - "The configuration for header option server name field."
            type: str
            returned: Always
        hostname:
            description:
                - "The DHCP host name associated with this fixed address. It is of FQDN type and it defaults to empty."
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
                - "The inheritance configuration."
            type: dict
            returned: Always
            contains:
                dhcp_options:
                    description:
                        - "The inheritance configuration for I(dhcp_options) field."
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
                header_option_filename:
                    description:
                        - "The inheritance configuration for I(header_option_filename) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
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
                                - "The inherited value."
                            type: str
                            returned: Always
                header_option_server_address:
                    description:
                        - "The inheritance configuration for I(header_option_server_address) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
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
                                - "The inherited value."
                            type: str
                            returned: Always
                header_option_server_name:
                    description:
                        - "The inheritance configuration for I(header_option_server_name) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
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
                                - "The inherited value."
                            type: str
                            returned: Always
        ip_space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        match_type:
            description:
                - "Indicates how to match the client:"
                - "* I(mac): match the client MAC address for both IPv4 and IPv6,"
                - "* I(client_text) or I(client_hex): match the client identifier for IPv4 only,"
                - "* I(relay_text) or I(relay_hex): match the circuit ID or remote ID in the DHCP relay agent option (82) for IPv4 only,"
                - "* I(duid): match the DHCP unique identifier, currently match only for IPv6 protocol."
            type: str
            returned: Always
        match_value:
            description:
                - "The value to match."
            type: str
            returned: Always
        name:
            description:
                - "The name of the fixed address. May contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the fixed address in JSON format."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
"""

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from ipam import FixedAddressApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class FixedAddressInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(FixedAddressInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = FixedAddressApi(self.client).read(self.params["id"], inherit="full")
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
                resp = FixedAddressApi(self.client).list(
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

    module = FixedAddressInfoModule(
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
