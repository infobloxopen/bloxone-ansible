#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: infra_host_info
short_description: Retrieve Infrastructure Hosts
description:
    - Retrieve Infrastructure Hosts
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
  - name: Get Host information by ID
    infoblox.bloxone.infra_host_info:
      id: "{{ host_id }}"

  - name: Get Host information by filters (e.g. display name)
    infoblox.bloxone.infra_host_info:
      filters:
        display_name: "example_host"

  - name: Get Host information by raw filter query
    infoblox.bloxone.infra_host_info:
      filter_query: "display_name=='example_host'"

  - name: Get Host information by tag filters
    infoblox.bloxone.infra_host_info:
      tag_filters:
        location: "site-1"

  - name: Get Host Information with retries
    infoblox.bloxone.infra_host_info:
      filters:
        display_name: "example_host"
    timeout: 10
    retries: 5
    delay: 1
    until: "infra_host_info.objects | length == 1"
"""

RETURN = r"""
id:
    description:
        - ID of the Hosts object
    type: str
    returned: Always
objects:
    description:
        - Hosts object
    type: list
    elements: dict
    returned: Always
    contains:
        configs:
            description:
                - "The list of Host-specific configurations for each Service deployed on this Host."
            type: list
            returned: Always
            elements: dict
            contains:
                current_version:
                    description:
                        - "The current version of the Service deployed on the Host."
                    type: str
                    returned: Always
                extra_data:
                    description:
                        - "The field to carry any extra data specific to this configuration."
                    type: str
                    returned: Always
                host_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                service_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                service_type:
                    description:
                        - "The type of the Service deployed on the Host (C(\"dns\"), C(\"cdc\"), etc.)."
                    type: str
                    returned: Always
                upgraded_at:
                    description:
                        - "The timestamp of the latest upgrade of the Host-specific Service configuration."
                    type: str
                    returned: Always
        connectivity_monitor:
            description:
                - "Represents the connectivity monitor properties of a Host, to enable/disable connectivity monitoring for redundant network interfaces."
                - "The \"endpoint_type\" is:"
                - "- C(\"\"csp\"\") for enabling monitoring"
                - "- C(\"\"\"\") for disabling monitoring (default)"
                - "Note: Currently, all fields except \"endpoint_type\" are read-only, and will be overridden to default values in case they are edited."
                - "Example:"
                - "{"
                - "\"connectivity_monitor\": {"
                - "\"cost\":1000000,"
                - "\"endpoint_type\":\"csp\","
                - "\"endpoint\":\"http://csp.infoblox.com\","
                - "\"interval\":15,"
                - "\"failure_threshold\":1,"
                - "\"success_threshold\":2"
                - "}"
                - "}"
            type: dict
            returned: Always
        created_at:
            description:
                - "The timestamp of creation of Host."
            type: str
            returned: Always
        created_by:
            description:
                - "The creator of the Host (internal use only)."
            type: str
            returned: Always
        description:
            description:
                - "The description of the Host (optional)."
            type: str
            returned: Always
        display_name:
            description:
                - "The name of the Host (unique)."
            type: str
            returned: Always
        host_subtype:
            description:
                - "The sub-type of a specific Host type."
                - "Example: For Host type BloxOne Appliance, sub-type could be \"B105\" or \"VEP1425\""
            type: str
            returned: Always
        host_type:
            description:
                - "The type of Host."
                - "Should be one of: 1. NIOS , 2. NIOS HA, 3. BloxOne VM , 4. BloxOne Appliance, 5. BloxOne Container, 6. CNIOS"
            type: str
            returned: Always
        host_version:
            description:
                - "The version of the Host platform services."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        ip_address:
            description:
                - "The IP address of the Host."
            type: str
            returned: Always
        ip_space:
            description:
                - "The IP Space of the Host."
            type: str
            returned: Always
        legacy_id:
            description:
                - "The legacy Host object identifier."
            type: str
            returned: Always
        location_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        mac_address:
            description:
                - "The MAC address of the Host."
            type: str
            returned: Always
        maintenance_mode:
            description: ""
            type: str
            returned: Always
        nat_ip:
            description:
                - "The NAT IP address of the Host."
            type: str
            returned: Always
        noa_cluster:
            description:
                - "The CSP cluster identifier (internal use only)."
            type: str
            returned: Always
        ophid:
            description:
                - "The unique On-Prem Host ID generated by the On-Prem device and assigned to the Host once it is registered and logged into the Infoblox Cloud."
            type: str
            returned: Always
        pool_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        serial_number:
            description:
                - "The unique serial number of the Host."
            type: str
            returned: Always
        tags:
            description:
                - "Tags associated with this Host."
            type: dict
            returned: Always
        timezone:
            description:
                - "The timezone of the Host."
            type: str
            returned: Always
        updated_at:
            description:
                - "The timestamp of the latest update on Host."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from infra_mgmt import HostsApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class HostsInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(HostsInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = HostsApi(self.client).read(self.params["id"])
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
                resp = HostsApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str
                )

                # If no results, set results to empty list
                if not resp.results:
                    resp.results = []

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

    module = HostsInfoModule(
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
