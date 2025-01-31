#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_acl_info
short_description: "Manages a named Access Control List (ACL)"
description:
    - "Manages a named Access Control List (ACL)"
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
  - name: Get ACL by ID
    infoblox.bloxone.dns_acl_info:
        id: "{{ acl_id }}"

  - name: Get ACL by filters
    infoblox.bloxone.dns_acl_info:
      filters:
        name: "{{ acl_name }}"

  - name: Get ACL by filter query
    infoblox.bloxone.dns_acl_info:
      filter_query: "name=='{{ acl_name }}'"

  - name: Get ACL by tag filters
    infoblox.bloxone.dns_acl_info:
      tag_filters:
        location: "us-west"
"""

RETURN = r"""
id:
    description:
        - ID of the Acl object
    type: str
    returned: Always
objects:
    description:
        - Acl object
    type: list
    elements: dict
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for ACL."
            type: str
            returned: Always
        compartment_id:
            description:
                - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        list:
            description:
                - "Optional. Ordered list of access control elements."
                - "Elements are evaluated in order to determine access. If evaluation reaches the end of the list then access is denied."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of AccessList item."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        name:
            description:
                - "ACL object name."
            type: str
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_config import AclApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AclInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AclInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = AclApi(self.client).read(self.params["id"])
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
                resp = AclApi(self.client).list(
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

    module = AclInfoModule(
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
