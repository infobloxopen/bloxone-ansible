#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_ipam_ipv4_reservation_gather
author: "Amit Mishra (@amishra), Sriram Kannan(@kannans)"
short_description: Gather information about Address Block in B1DDI
version_added: "1.0.1"
description:
  - Gather information about Address Block object on Infoblox BloxOne DDI. This module gather information about address block object using BloxOne REST APIs.
requirements:
  - requests
options:
  api_key:
    description:
      - Configures the API token for authentication against Infoblox BloxOne patform.
    type: str
    required: true
  host:
    description:
      - Configures the Infoblox BloxOne host URL.
    type: dict
    required: true
  fields:
    description:
      - Configures the list of fields to be available as a part of search result.
    type: list
    required: false
  filters:
    description:
      - Configure a list of filters to be applied on the search result.
    type: dict
    required: false
  state:
    description:
      - Configures the state of the object on BloxOne DDI. When this value is set to C(get), the object
        details are fetched (if present) from the platform, when this value is set to C(present), the object
        is configured on the platform and when this value is set to C(absent)
        the value is removed (if necessary) from the platform.
    type: str
    default: present
    choices:
      - gather
    required: true
"""


EXAMPLES = """

- name: Gather all IPAM IPV4 information
  b1_ipam_ipv4_reservation_gather:
    host: "{{ host }}"
    api_key: "{{ api }}"
    state: gather

- name: Gather the IPAM IPV4 information
  b1_ipam_ipv4_reservation_gather:
    host: "{{ host_server }}"
    api_key: "{{ api }}"
    state: gather
    fields: ['id']
    filters: {'address': 'ip address' }
  register: address_block_id
- debug: msg="{{ address_block_id }}"

"""

RETURN = """ # """

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request


def get_ipv4_reservation(data):
    """Fetches the BloxOne DDI IP Space object"""
    connector = Request(data["host"], data["api_key"])
    endpoint = "/api/ddi/v1/ipam/address"

    flag = 0
    fields = data["fields"]
    filters = data["filters"]
    if fields is not None and isinstance(fields, list):
        temp_fields = ",".join(fields)
        endpoint = endpoint + "?_fields=" + temp_fields
        flag = 1

    if filters != {} and isinstance(filters, dict):
        temp_filters = []
        for k, v in filters.items():
            if str(v).isdigit():
                temp_filters.append(f"{k}=={v}")
            else:
                temp_filters.append(f"{k}=='{v}'")
        res = " and ".join(temp_filters)
        if flag == 1:
            endpoint = endpoint + "&_filter=" + res
        else:
            endpoint = endpoint + "?_filter=" + res

    try:
        return connector.get(endpoint)
    except Exception:
        raise Exception(endpoint)


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        name=dict(default="", type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        comment=dict(type="str"),
        fields=dict(type="list"),
        filters=dict(type="dict", default={}),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "gather"]),
    )

    choice_map = {"gather": get_ipv4_reservation}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
