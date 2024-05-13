#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_ipam_address_block
author: "Amit Mishra (@amishra), Sriram Kannan(@kannans)"
short_description: Configure Address Block on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  - Create, Update and Delete Address Block on Infoblox BloxOne DDI. This module manages the IPAM Address Block object using BloxOne REST APIs.
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
  address:
    description:
      - Configures the address of the address block to fetch, add, update or remove from the system.
        The address of the address block in the form "a.b.c.d/n".
        When fetching, the address field can be in the form "a.b.c.d".
    type: str
    required: true
  space:
    description:
      - Configures the name of IP Space containing the address block to fetch, add, update or remove from the system.
    type: str
    required: true
  name:
    description:
      - Configures the name of address block object to fetch, add, update or remove from the system.
    type: str
  tags:
    description:
      - Configures the tags associated with the address block object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the address block object to add or update from the system.
    type: str
  state:
    description:
      - Configures the state of the address block object on BloxOne DDI. When this value is set to C(get), the object
        details are fetched (if present) from the platform, when this value is set to C(present), the object
        is configured on the platform and when this value is set to C(absent)
        the value is removed (if necessary) from the platform.
    type: str
    default: present
    choices:
      - present
      - absent
      - get
    required: true
"""


EXAMPLES = """

- name: Create Address Block
  b1_ipam_address_block:
    address: "{{ network_address }}"
    space: "{{ ip_space }}"
    name: "{{ address_block_name }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Create Address Block using next available function
  b1_ipam_address_block:
    address: '{"next_available_address_block": {"parent_block": "<parent address block>", "cidr": "<cidr of child blocks>", "count": "<quantity>"}}'
    space: "{{ ip_space }}"
    name: "{{ address_block_name }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Update Address Block
  b1_ipam_address_block:
    address: '{"new_address": "{{ new address of the address block }}", "old_address": "{{ old address of the address block }}"}'
    name: "{{ address_block_name }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    space: "{{ ip_space }}"
    host: "{{ host_server }}"
    state: present

- name: Delete Address Block
  b1_ipam_address_block:
    address: "{{ network_address }}"
    space: "{{ ip_space }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: absent

"""

RETURN = """ # """

import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_address_block(data):
    """Fetches the BloxOne DDI Address Block object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "space" in data.keys() and data["space"] is not None:
        space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
        space = connector.get(space_endpoint)
        if "results" in space[2].keys() and len(space[2]["results"]) > 0:
            space_ref = space[2]["results"][0]["id"]
            if "address" in data.keys() and data["address"] is not None:
                p_data = helper.normalize_ip(data["address"])
                if p_data[0] != "" and p_data[1] != "":
                    endpoint = f"/api/ddi/v1/ipam/address_block?_filter=space=='{space_ref}' and address=='{p_data[0]}' and cidr=={p_data[1]}"
                elif p_data[0] != "" and p_data[1] == "":
                    endpoint = f"/api/ddi/v1/ipam/address_block?_filter=space=='{space_ref}' and address=='{p_data[0]}'"
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "Invalid Address", "data": data},
                    )
            else:
                endpoint = f"/api/ddi/v1/ipam/address_block?_filter=space=='{space_ref}'"
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
        if "address" in data.keys() and data["address"] is not None:
            p_data = helper.normalize_ip(data["address"])
            if p_data[0] != "" and p_data[1] != "":
                endpoint = f"/api/ddi/v1/ipam/address_block?_filter=address=='{p_data[0]}' and cidr=={p_data[1]}"
            elif p_data[0] != "" and p_data[1] == "":
                endpoint = f"/api/ddi/v1/ipam/address_block?_filter=address=='{p_data[0]}'"
            else:
                return (
                    True,
                    False,
                    {"status": "400", "response": "Invalid Address", "data": data},
                )
            return connector.get(endpoint)
        else:
            return connector.get("/api/ddi/v1/ipam/address_block")


def update_address_block(data):
    """Updates the existing BloxOne DDI Address Block object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data["address"] and data["address"] is not None for k in ("new_address", "old_address")):
        try:
            address = json.loads(data["address"])
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        new_address = helper.normalize_ip(address["new_address"])
        old_address = helper.normalize_ip(address["old_address"])
        if new_address[0] != old_address[0]:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Address mismatched. The address cannot be changed, only CIDR can be updated.",
                    "data": data,
                },
            )
        data["address"] = f"{old_address[0]}/{old_address[1]}"
    else:
        new_address = helper.normalize_ip(data["address"])

    reference = get_address_block(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "Address Block not found", "data": data},
        )
    payload = {}
    payload["cidr"] = int(new_address[1])
    payload["name"] = data["name"] if "name" in data.keys() else ""
    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_address_block(data):
    """Creates a new BloxOne DDI Address Block object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("space", "address")):
        if "next_available_address_block" in data["address"]:
            return next_available_address_block(data)
        elif "new_address" in data["address"]:
            return update_address_block(data)
        else:
            p_data = helper.normalize_ip(data["address"])
            if p_data[0] == "" or p_data[1] == "":
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Incorrect address definition",
                        "data": data,
                    },
                )
            address_block = get_address_block(data)
            payload = {}
            if "results" in address_block[2].keys() and len(address_block[2]["results"]) > 0:
                return update_address_block(data)
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
                payload["address"] = f"{p_data[0]}/{p_data[1]}"
                payload["name"] = data["name"] if "name" in data.keys() else ""
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                if "tags" in data.keys() and data["tags"] is not None:
                    payload["tags"] = helper.flatten_dict_object("tags", data)
                return connector.create("/api/ddi/v1/ipam/address_block", payload)
    else:
        return (
            True,
            False,
            {
                "status": "400",
                "response": "Address or IP Space not defined",
                "data": data,
            },
        )


def delete_address_block(data):
    """Delete a BloxOne DDI Address Block object"""
    if all(k in data and data[k] is not None for k in ("space", "address")):
        connector = Request(data["host"], data["api_key"])
        helper = Utilities()
        p_data = helper.normalize_ip(data["address"])
        if p_data[0] == "" or p_data[1] == "":
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Incorrect address definition",
                    "data": data,
                },
            )
        address_block = get_address_block(data)
        if "results" in address_block[2].keys() and len(address_block[2]["results"]) > 0:
            ref_id = address_block[2]["results"][0]["id"]
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
                "response": "Address or IP Space not defined",
                "data": data,
            },
        )


def next_available_address_block(data):
    """Implementation of next available functionality"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    try:
        address_data = json.loads(data["address"])["next_available_address_block"]
        if "parent_block" not in address_data.keys() or "cidr" not in address_data.keys():
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Parent block and CIDR are mandatory fields",
                    "data": data,
                },
            )
        p_data = helper.normalize_ip(address_data["parent_block"])
        if p_data[0] == "" or p_data[1] == "":
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Invalid Syntax for parent block",
                    "data": data,
                },
            )
        count = int(address_data["count"]) if "count" in address_data.keys() else 1
        cidr = int(address_data["cidr"])
        name = data["name"] if "name" in data.keys() else ""
        comment = data["comment"] if "comment" in data.keys() else ""

        data["address"] = address_data["parent_block"]
        address_block = get_address_block(data)
        if "results" in address_block[2].keys() and len(address_block[2]["results"]) > 0:
            ref_id = address_block[2]["results"][0]["id"]
        else:
            return (
                True,
                False,
                {"status": "400", "response": "Object not found", "data": data},
            )
        # Endpoint API URL
        if name != "" and comment != "":
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailableaddressblock?count={count}&cidr={cidr}&name={name}&comment={comment}"
        elif name == "" and comment != "":
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailableaddressblock?count={count}&cidr={cidr}&comment={comment}"
        elif name != "" and comment == "":
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailableaddressblock?count={count}&cidr={cidr}&name={name}"
        else:
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailableaddressblock?count={count}&cidr={cidr}"
        return connector.create(endpoint, body=False)
    except Exception:
        return (
            True,
            False,
            {"status": "400", "response": "Invalid Syntax", "data": data},
        )


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        name=dict(default="", type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        address=dict(type="str"),
        space=dict(type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {
        "present": create_address_block,
        "get": get_address_block,
        "absent": delete_address_block,
    }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
