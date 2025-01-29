#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_host_info
short_description: Manage IpamHost
description:
    - Manage IpamHost
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
      infoblox.bloxone.ipam_host_info:
        id: "{{ host.id }}"

    - name: Get Host information by filters
      infoblox.bloxone.ipam_host_info:
        filters:
          name: "example_host"

    - name: Get Host information by filter query
      infoblox.bloxone.ipam_host_info:
        filter_query: "name=='example_host'"

    - name: Get Host information by tag filters
      infoblox.bloxone.ipam_host_info:
        tag_filters:
            location: "site-1"
"""

RETURN = r"""
id:
    description:
        - ID of the IpamHost object
    type: str
    returned: Always
objects:
    description:
        - IpamHost object
    type: list
    elements: dict
    returned: Always
    contains:
        addresses:
            description:
                - "The list of all addresses associated with the IPAM host, which may be in different IP spaces."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Field usage depends on the operation:"
                        - "* For read operation, I(address) of the I(Address) corresponding to the I(ref) resource."
                        - "* For write operation, I(address) to be created if the I(Address) does not exist. Required if I(ref) is not set on write:"
                        - "* If the I(Address) already exists and is already pointing to the right I(Host), the operation proceeds."
                        - "* If the I(Address) already exists and is pointing to a different _Host, the operation must abort."
                        - "* If the I(Address) already exists and is not pointing to any I(Host), it is linked to the I(Host)."
                    type: str
                    returned: Always
                ref:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                space:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        auto_generate_records:
            description:
                - "This flag specifies if resource records have to be auto generated for the host."
            type: bool
            returned: Always
        comment:
            description:
                - "The description for the IPAM host. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        host_names:
            description:
                - "The name records to be generated for the host."
                - "This field is required if I(auto_generate_records) is true."
            type: list
            returned: Always
            elements: dict
            contains:
                alias:
                    description:
                        - "When I(true), the name is treated as an alias."
                    type: bool
                    returned: Always
                name:
                    description:
                        - "A name for the host."
                    type: str
                    returned: Always
                primary_name:
                    description:
                        - "When I(true), the name field is treated as primary name. There must be one and only one primary name in the list of host names. The primary name will be treated as the canonical name for all the aliases. PTR record will be generated only for the primary name."
                    type: bool
                    returned: Always
                zone:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name:
            description:
                - "The name of the IPAM host. Must contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the IPAM host in JSON format."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from ipam import IpamHostApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class IpamHostInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(IpamHostInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = IpamHostApi(self.client).read(self.params["id"])
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
                resp = IpamHostApi(self.client).list(
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

    module = IpamHostInfoModule(
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
