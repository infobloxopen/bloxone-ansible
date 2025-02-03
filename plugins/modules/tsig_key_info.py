#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: tsig_key_info
short_description: Retrieves TSIG Keys
description:
    - Retrieves information about existing TSIG Keys.
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
- name: Get TSIG Key information by ID
  infoblox.bloxone.tsig_key_info:
    id: "{{ tsig_key_id }}"

- name: Get TSIG Key information by filters (e.g. name)
  infoblox.bloxone.tsig_key_info:
    filters:
      name: "tsig-name"

- name: Get TSIG Key information by raw filter query
  infoblox.bloxone.tsig_key_info:
    filter_query: "name=='tsig-name'"

- name: Get TSIG Key information by tag filters
  infoblox.bloxone.tsig_key_info:
    tag_filters:
      location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the TSIG object
    type: str
    returned: Always
objects:
    description:
        - TSIG object
    type: list
    elements: dict
    returned: Always
    contains:
        algorithm:
            description:
                - "The TSIG key algorithm."
                - "Valid values are:"
                - "* I(hmac_sha1)"
                - "* I(hmac_sha224)"
                - "* I(hmac_sha256)"
                - "* I(hmac_sha384)"
                - "* I(hmac_sha512)"
                - "Defaults to I(hmac_sha256)."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the TSIG key. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name:
            description:
                - "The TSIG key name in the absolute domain name format."
            type: str
            returned: Always
        protocol_name:
            description:
                - "The TSIG key name supplied during a create/update operation that is converted to canonical form in punycode."
            type: str
            returned: Always
        secret:
            description:
                - "The TSIG key secret as a Base64 encoded string."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the TSIG key in JSON format."
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
    from keys import TsigApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class TsigKeyInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(TsigKeyInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = TsigApi(self.client).read(self.params["id"])
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
                resp = TsigApi(self.client).list(
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

    module = TsigKeyInfoModule(
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
