#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_auth_nsg_info
short_description: Manage AuthNsg
description:
    - Manage AuthNsg
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
  - name: Get Auth NSG information by ID
    infoblox.bloxone.dns_auth_nsg_info:
      id: "{{ auth_nsg_id }}"

  - name: Get Auth NSG information by filters (e.g. name)
    infoblox.bloxone.dns_auth_nsg_info:
      filters:
        name: "example_nsg"

  - name: Get Auth NSG information by raw filter query
    infoblox.bloxone.dns_auth_nsg_info:
      filter_query: "name=='example_nsg'"

  - name: Get Auth NSG information by tag filters
    infoblox.bloxone.dns_auth_nsg_info:
      tag_filters:
        location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the AuthNsg object
    type: str
    returned: Always
objects:
    description:
        - AuthNsg object
    type: list
    elements: dict
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for the object."
            type: str
            returned: Always
        external_primaries:
            description:
                - "Optional. DNS primaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Optional. Required only if I(type) is I(server). IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Optional. Required only if I(type) is I(server). FQDN of nameserver."
                    type: str
                    returned: Always
                nsg:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                tsig_enabled:
                    description:
                        - "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
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
                type:
                    description:
                        - "Allowed values:"
                        - "* I(nsg),"
                        - "* I(primary)."
                    type: str
                    returned: Always
        external_secondaries:
            description:
                - "DNS secondaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "FQDN of nameserver."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                stealth:
                    description:
                        - "If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_enabled:
                    description:
                        - "If enabled, secondaries will use the configured TSIG key when requesting a zone transfer."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
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
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        internal_secondaries:
            description:
                - "Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        name:
            description:
                - "Name of the object."
            type: str
            returned: Always
        nsgs:
            description:
                - "The resource identifier."
            type: list
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from dns_config import AuthNsgApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AuthNsgInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AuthNsgInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = AuthNsgApi(self.client).read(self.params["id"])
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
                resp = AuthNsgApi(self.client).list(
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

    module = AuthNsgInfoModule(
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
