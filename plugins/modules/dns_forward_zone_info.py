#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_forward_zone_info
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
  - name: Get Forward Zone information by filters (FQDN)
    infoblox.bloxone.dns_forward_zone_info:
      filters:
        id: "{{ forward_zone_id }}"

  - name: Get Forward Zone information by filters (e.g. name)
    infoblox.bloxone.dns_forward_zone_info:
      filters:
        name: "example_zone"

  - name: Get Forward Zone information by raw filter query
    infoblox.bloxone.dns_auth_zone_info:
      filter_query: "name=='example_zone'"

  - name: Get Forward Zone information by tag filters
    infoblox.bloxone.dns_forward_zone_info:
      tag_filters:
        location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the ForwardZone object
    type: str
    returned: Always
objects:
    description:
        - ForwardZone object
    type: list
    elements: dict
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
    from dns_config import ForwardZoneApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class ForwardZoneInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(ForwardZoneInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = ForwardZoneApi(self.client).read(self.params["id"])
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
                resp = ForwardZoneApi(self.client).list(
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

    module = ForwardZoneInfoModule(
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
