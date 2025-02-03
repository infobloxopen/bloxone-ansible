#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: infra_service_info
short_description: Retrieve Infrastructure Services
description:
    - Retrieve Infrastructure Services
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
    - name: Get Service Information by ID
      infoblox.bloxone.infra_service_info:
        id: "{{ service.id }}"

    - name: Get Service information by filters (Display Name)
      infoblox.bloxone.infra_service_info:
        filters:
          service_name: "example_service"

    - name: Get Service information by filter query
      infoblox.bloxone.infra_service_info:
        filter_query: "service_name=='example_service'"

    - name: Get Service information by tag filters
      infoblox.bloxone.infra_service_info:
        tag_filters:
          location: "site-1"
"""

RETURN = r"""
id:
    description:
        - ID of the Services object
    type: str
    returned: Always
objects:
    description:
        - Services object
    type: list
    elements: dict
    returned: Always
    contains:
        configs:
            description:
                - "List of Host-specific configurations of this Service."
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
        created_at:
            description:
                - "Timestamp of creation of Service."
            type: str
            returned: Always
        description:
            description:
                - "The description of the Service (optional)."
            type: str
            returned: Always
        desired_state:
            description:
                - "The desired state of the Service. Should either be C(\"\"start\"\") or C(\"\"stop\"\")."
            type: str
            returned: Always
        desired_version:
            description:
                - "The desired version of the Service."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        interface_labels:
            description:
                - "List of interfaces on which this Service can operate. Note: The list can contain custom interface labels (Example: C(\"[\"WAN\",\"LAN\",\"label1\",\"label2\"]\"))"
            type: list
            returned: Always
        name:
            description:
                - "The name of the Service (unique)."
            type: str
            returned: Always
        pool_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        service_type:
            description:
                - "The type of the Service deployed on the Host (C(\"dns\"), C(\"cdc\"), etc.)."
            type: str
            returned: Always
        tags:
            description:
                - "Tags associated with this Service."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Timestamp of the latest update on Service."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from infra_mgmt import ServicesApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class ServicesInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(ServicesInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = ServicesApi(self.client).read(self.params["id"])
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
                resp = ServicesApi(self.client).list(
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

    module = ServicesInfoModule(
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
