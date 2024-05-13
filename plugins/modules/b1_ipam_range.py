#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """

---
module: b1_ipam_range
author: "Amit Mishra (@amishra), Sriram Kannan(@kannans)"
short_description: Configure the IPAM range on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  - Create, Update and Delete the IPAM range on Infoblox BloxOne DDI. This module manages the IPAM IPAM range object using BloxOne REST APIs.
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
  start:
    description:
      - Configures the start address of the IPAM range to fetch, add, update or remove from the system.
        The address of the IPAM range in the form "a.b.c.d".
    type: str
    required: true
  end:
    description:
      - Configures the end address of the IPAM range to fetch, add, update or remove from the system.
        The address of the IPAM range in the form "a.b.c.d".
    type: str
    required: true
  space:
    description:
      - Configures the name of IP Space containing the IPAM range to fetch, add, update or remove from the system.
    type: str
    required: true
  dhcp_host:
    description:
      - Configures the name of the on-prem DHCP host for the IPAM range.
    type: str
  name:
    description:
      - Configures the name of the IPAM range object to fetch, add, update or remove from the system.
    type: str
  tags:
    description:
      - Configures the tags associated with the IPAM range object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the IPAM range object to add or update from the system.
    type: str
  state:
    description:
      - Configures the state of the IPAM range object on BloxOne DDI. When this value is set to C(get), the object
        details are fetched (if present) from the platform, when this value is set to C(present), the object
        is configured on the platform and when this value is set to C(absent)
        the value is removed (if necessary) from the platform.
    type: str
    choices:
      - present
      - absent
    required: true

"""

EXAMPLES = """

- name: Create IPAM range
  b1_ipam_range:
    start: "{{ start_IP_address }}"
    end: "{{ end_IP_address }}"
    space: "{{ IP_space }}"
    name: "{{ range_name }}"
    dhcp_host: "{{ onprem_dhcp_host }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Update IPAM range
  b1_ipam_range:
    start: '{"new_address": "{{ new start IP address of the range }}", "old_address": "{{ old start IP address of the range }}"}'
    end: '{"new_address": "{{ new end IP address of the range }}", "old_address": "{{ old end IP address of the range }}"}'
    name: "{{ range_name }}"
    space: "{{ ip_space }}"
    dhcp_host: "{{ onprem_dhcp_host }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Delete IPAM range
  b1_ipam_range:
    start: "{{ start_IP_address }}"
    end: "{{ end_IP_address }}"
    space: "{{ IP_space }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: absent

"""

RETURN = """ # """

import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_range(data):
    """Fetches the BloxOne DDI IPAM range object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "space" in data.keys() and data["space"] is not None:
        space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
        space = connector.get(space_endpoint)
        if "results" in space[2].keys() and len(space[2]["results"]) > 0:
            space_ref = space[2]["results"][0]["id"]
            if "start" in data.keys() and data["start"] is not None:
                start = helper.normalize_ip(data["start"])
                if "end" in data.keys() and data["end"] is not None:
                    end = helper.normalize_ip(data["end"])
                    if start[0] != "" and start[1] == "" and end[0] != "" and end[1] == "":
                        endpoint = f"/api/ddi/v1/ipam/range?_filter=space=='{space_ref}' and start=='{start[0]}' and end=='{end[0]}'"
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Invalid Address",
                                "data": data,
                            },
                        )
                else:
                    if start[0] != "" and start[1] == "":
                        endpoint = f"/api/ddi/v1/ipam/range?_filter=space=='{space_ref}' and start=='{start[0]}'"
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Invalid Address",
                                "data": data,
                            },
                        )
            elif "end" in data.keys() and data["end"] is not None:
                end = helper.normalize_ip(data["end"])
                if end[0] != "" and end[1] == "":
                    endpoint = f"/api/ddi/v1/ipam/range?_filter=space=='{space_ref}' and end=='{end[0]}'"
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "Invalid Address", "data": data},
                    )
            else:
                endpoint = f"/api/ddi/v1/ipam/range?_filter=space=='{space_ref}'"
            return connector.get(endpoint)
        else:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Error in fetching IP Space",
                    "data": data,
                },
            )
    else:
        if "start" in data.keys() and data["start"] is not None:
            start = helper.normalize_ip(data["start"])
            if "end" in data.keys() and data["end"] is not None:
                end = helper.normalize_ip(data["end"])
                if start[0] != "" and start[1] == "" and end[0] != "" and end[1] == "":
                    endpoint = f"/api/ddi/v1/ipam/range?_filter=start=='{start[0]}' and end=='{end[0]}'"
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "Invalid Address", "data": data},
                    )
            else:
                if start[0] != "" and start[1] == "":
                    endpoint = f"/api/ddi/v1/ipam/range?_filter=start=='{start[0]}'"
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "Invalid Address", "data": data},
                    )
        elif "end" in data.keys() and data["end"] is not None:
            end = helper.normalize_ip(data["end"])
            if end[0] != "" and end[1] == "":
                endpoint = f"/api/ddi/v1/ipam/range?_filter=end=='{end[0]}'"
            else:
                return (
                    True,
                    False,
                    {"status": "400", "response": "Invalid Address", "data": data},
                )
        else:
            endpoint = "/api/ddi/v1/ipam/range"
        return connector.get(endpoint)


def update_range(data):
    """Updates the existing BloxOne DDI IPAM range object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data["start"] and data["start"] is not None for k in ("new_address", "old_address")):
        try:
            start = json.loads(data["start"])
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        new_start_address = helper.normalize_ip(start["new_address"])
        old_start_address = helper.normalize_ip(start["old_address"])
        data["start"] = old_start_address[0]
    else:
        new_start_address = helper.normalize_ip(data["start"])

    if all(k in data["end"] and data["end"] is not None for k in ("new_address", "old_address")):
        try:
            end = json.loads(data["end"])
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        new_end_address = helper.normalize_ip(end["new_address"])
        old_end_address = helper.normalize_ip(end["old_address"])
        data["end"] = old_end_address[0]
    else:
        new_end_address = helper.normalize_ip(data["end"])

    reference = get_range(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "IPAM range not found", "data": data},
        )
    payload = {}
    payload["start"] = new_start_address[0]
    payload["end"] = new_end_address[0]
    payload["name"] = data["name"] if "name" in data.keys() else ""
    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    if "dhcp_host" in data.keys() and data["dhcp_host"] is not None:
        endpoint = f"/api/ddi/v1/dhcp/host?_filter=name==\"{data['dhcp_host']}\""
        dhcp_host = connector.get(endpoint)
        if "results" in dhcp_host[2].keys() and len(dhcp_host[2]["results"]) > 0:
            payload["dhcp_host"] = dhcp_host[2]["results"][0]["id"]
        else:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Error in fetching On-prem host",
                    "data": data,
                },
            )
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_range(data):
    """Creates a new BloxOne DDI IPAM range object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("space", "start", "end")):
        if "new_address" in data["start"] or "new_address" in data["end"]:
            return update_range(data)
        else:
            start = helper.normalize_ip(data["start"])
            end = helper.normalize_ip(data["end"])
            if start[0] == "" or start[1] != "" or end[0] == "" or end[1] != "":
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Incorrect start/end address definition",
                        "data": data,
                    },
                )
            range = get_range(data)
            payload = {}
            if "results" in range[2].keys() and len(range[2]["results"]) > 0:
                return update_range(data)
            else:
                space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
                space = connector.get(space_endpoint)
                if "results" in space[2].keys() and len(space[2]["results"]) > 0:
                    payload["space"] = space[2]["results"][0]["id"]
                else:
                    return (
                        True,
                        False,
                        {
                            "status": "400",
                            "response": "Error in fetching IP Space",
                            "data": data,
                        },
                    )
                if "dhcp_host" in data.keys() and data["dhcp_host"] is not None:
                    endpoint = f"/api/ddi/v1/dhcp/host?_filter=name==\"{data['dhcp_host']}\""
                    dhcp_host = connector.get(endpoint)
                    if "results" in dhcp_host[2].keys() and len(dhcp_host[2]["results"]) > 0:
                        payload["dhcp_host"] = dhcp_host[2]["results"][0]["id"]
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Error in fetching On-prem host",
                                "data": data,
                            },
                        )
                payload["start"] = data["start"]
                payload["end"] = data["end"]
                payload["name"] = data["name"] if "name" in data.keys() else ""
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                if "tags" in data.keys() and data["tags"] is not None:
                    payload["tags"] = helper.flatten_dict_object("tags", data)
                return connector.create("/api/ddi/v1/ipam/range", payload)
    else:
        return (
            True,
            False,
            {
                "status": "400",
                "response": "Start/End IP address or IP Space not defined",
                "data": data,
            },
        )


def delete_range(data):
    """Delete a BloxOne DDI IPAM range object"""
    if all(k in data and data[k] is not None for k in ("space", "start", "end")):
        connector = Request(data["host"], data["api_key"])
        helper = Utilities()
        start = helper.normalize_ip(data["start"])
        end = helper.normalize_ip(data["end"])
        if start[0] == "" or start[1] != "" or end[0] == "" or end[1] != "":
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Incorrect address definition",
                    "data": data,
                },
            )
        range = get_range(data)
        if "results" in range[2].keys() and len(range[2]["results"]) > 0:
            ref_id = range[2]["results"][0]["id"]
            endpoint = f"/api/ddi/v1/{ref_id}"
            return connector.delete(endpoint)
        else:
            return (
                True,
                False,
                {"status": "400", "response": "Object not found", "data": data},
            )
    else:
        return (
            True,
            False,
            {
                "status": "400",
                "response": "Start/End Address or IP Space not defined",
                "data": data,
            },
        )


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        name=dict(type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        start=dict(type="str"),
        end=dict(type="str"),
        space=dict(type="str"),
        dhcp_host=dict(type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {"present": create_range, "get": get_range, "absent": delete_range}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
