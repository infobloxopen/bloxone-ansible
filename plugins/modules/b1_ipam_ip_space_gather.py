#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_ipam_ip_space
author: "Amit Mishra (@amishra), Sriram Kannan(@kannans)"
contributor: "Chris Marrison (@ccmarris)"
short_description: Configure IP space on Infoblox BloxOne DDI
version_added: "1.1.0"
description:
  - Gather facts about IP spaces in Infoblox BloxOne DDI. This module manages the gather fact of IPAM IP space object using BloxOne REST APIs.
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
    type: str
    required: true
  fields:
    description:
      - List of fields to be available from the gather results.
    type: list
    required: false
  filters:
    description:
      - Filters the result based on the key, value provided .
    type: dict
  tfilters:
    description:
      - Filters the result based on the Tag key, value provided .
    type: dict
  state:
    description:
      - Configures the state of the object on BloxOne DDI. When this value is set to C(get), the object
        details are fetched (if present) from the platform, when this value is set to C(present), the object
        is configured on the platform and when this value is set to C(absent)
        the value is removed (if necessary) from the platform.
    type: str
    default: present
    choices:
      - present
      - absent
    required: true
"""


EXAMPLES = """

    - name: Gather IP space
      b1_ipam_ip_space_gather:
        host: "{{ host_server }}"
        api_key: "{{ api }}"
        state: gather

    - name: Gather the ID information of an for a given name
      b1_ipam_ip_space_gather:
        host: "{{ host_server }}"
        api_key: "{{ api }}"
        state: gather
        fields: ['id' ]
        filters: {'name': 'testIP1'}

    - name: Gather ip_space information for given tag key/value pairs
      b1_ipam_ip_space_gather:
        host: "{{ host_server }}"
        api_key: "{{ api }}"
        state: gather
        tfilters: {'Owner': 'chris'}
"""

RETURN = """ # """

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request


def get_ip_space(data):
    """Fetches the BloxOne DDI IP Space object"""
    """Fetches the BloxOne DDI IP Space object
    """
    connector = Request(data["host"], data["api_key"])
    endpoint = "/api/ddi/v1/ipam/ip_space"

    flag = 0
    fields = data["fields"]
    filters = data["filters"]
    tfilters = data["tfilters"]
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

    if tfilters != {} and isinstance(tfilters, dict):
        temp_tfilters = []
        for k, v in tfilters.items():
            if str(v).isdigit():
                temp_tfilters.append(f"{k}=={v}")
            else:
                temp_tfilters.append(f"{k}=='{v}'")
        res = " and ".join(temp_tfilters)
        if flag == 1:
            endpoint = endpoint + "&_tfilter=" + res
        else:
            endpoint = endpoint + "?_tfilter=" + res

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
        tfilters=dict(type="dict", default={}),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "gather"]),
    )

    choice_map = {"gather": get_ip_space}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
