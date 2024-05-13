#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """

---
module: b1_dhcp_fixed_address
author: "Amit Mishra (@amishra)"
contributor: "Chris Marrison (@ccmarris)"
short_description: Configure fixed address on Infoblox BloxOne DDI
version_added: "1.1.2"
description:
  - Get, Create, Update and Delete fixed address on Infoblox BloxOne DDI. This module manages the fixed address object using BloxOne REST APIs.
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
      - Configures the address of the fixed address to fetch, add, update or remove from the system.
        The address of the fixed address in the form "a.b.c.d".
    type: str
    required: true
  space:
    description:
      - Configures the name of IP Space containing the fixed address to fetch, add, update or remove from the system.
    type: str
    required: true
  name:
    description:
      - Configures the name of the fixed address object to fetch, add, update or remove from the system.
    type: str
  match_type:
    description:
      - Indicates how to match the client to the fixed address allocation
    type: str
    choices:
      - mac
      - client_text
      - client_hex
      - relay_text
      - relay_hex
    required: true
  match_value:
    description:
      - Configures the value to match for the fixed address match_type
    type: str
    required: true
  tags:
    description:
      - Configures the tags associated with the fixed address object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the fixed address object to add or update from the system.
    type: str
  state:
    description:
      - Configures the state of the fixed address object on BloxOne DDI. When this value is set to C(get), the object
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

- name: GET all fixed address allocations
  b1_ipam_fixed_address:
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: get

- name: GET fixed address
  b1_ipam_fixed_address:
    space: "{{ IP_space }}"
    address: "{{ IP_address }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: get

- name: Create fixed address
  b1_ipam_fixed_address:
    address: "{{ IP_address }}"
    space: "{{ IP_space }}"
    name: "{{ fixed_address_name }}"
    match_type: "{{ match_type }}"
    match_value: "{{ match_value }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Create fixed address using next available IP functionality
  b1_ipam_fixed_address:
    address: '{"next_available_ip": {"subnet": "<subnet>"}}'
    space: "{{ IP_space }}"
    name: "{{ fixed_address_name }}"
    match_type: "{{ match_type }}"
    match_value: "{{ match_value }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Update fixed address
  b1_ipam_fixed_address:
    address: '{"new_address": "{{ new IP address of the fixed address }}", "old_address": "{{ old IP address of the fixed address }}"}'
    name: "{{ fixed_address_name }}"
    space: "{{ ip_space }}"
    tags:
      - key: "{{ value }}"
    match_type: "{{ match_type }}"
    match_value: "{{ match_value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Delete fixed address
  b1_ipam_fixed_address:
    address: "{{ IP_address }}"
    space: "{{ IP_space }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: absent

"""

RETURN = """ # """

import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_fixed_address(data):
    """Fetches the BloxOne DDI fixed address object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "space" in data.keys() and data["space"] is not None:
        space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
        space = connector.get(space_endpoint)
        if "results" in space[2].keys() and len(space[2]["results"]) > 0:
            space_ref = space[2]["results"][0]["id"]
            if "address" in data.keys() and data["address"] is not None:
                p_data = helper.normalize_ip(data["address"])
                if p_data[0] != "" and p_data[1] == "":
                    endpoint = (
                        f"/api/ddi/v1/dhcp/fixed_address?_filter=ip_space=='{space_ref}' and address=='{p_data[0]}'"
                    )
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "Invalid Address", "data": data},
                    )
            else:
                endpoint = f"/api/ddi/v1/dhcp/fixed_address?_filter=ip_space=='{space_ref}'"
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
            if p_data[0] != "" and p_data[1] == "":
                endpoint = f"/api/ddi/v1/dhcp/fixed_address?_filter=address=='{p_data[0]}'"
            else:
                return (
                    True,
                    False,
                    {"status": "400", "response": "Invalid Address", "data": data},
                )
            return connector.get(endpoint)
        else:
            return connector.get("/api/ddi/v1/dhcp/fixed_address")


def update_fixed_address(data):
    """Updates the existing BloxOne DDI IPv4 address reservation object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data["address"] and data["address"] is not None for k in ("new_address", "old_address")):
        try:
            address = json.loads(data["address"].replace("'", '"'))
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        new_address = helper.normalize_ip(address["new_address"])
        old_address = helper.normalize_ip(address["old_address"])
        data["address"] = str(old_address[0])
    else:
        new_address = helper.normalize_ip(data["address"])

    reference = get_fixed_address(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {
                "status": "400",
                "response": "IPv4 address reservation not found",
                "data": data,
            },
        )
    payload = {}
    payload["address"] = new_address[0]
    payload["name"] = data["name"] if "name" in data.keys() else ""
    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    payload["match_type"] = data["match_type"] if "match_type" in data.keys() else ""
    payload["match_value"] = data["match_value"] if "match_value" in data.keys() else ""
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_fixed_address(data):
    """Creates a new BloxOne DDI fixed address object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("space", "address")):
        """Implementation of the next available functionality"""
        if "next_available_ip" in data["address"]:
            try:
                subnet = json.loads(data["address"].replace("'", '"'))["next_available_ip"]["subnet"]
                p_data = helper.normalize_ip(subnet)
            except Exception:
                return (
                    True,
                    False,
                    {"status": "400", "response": "Invalid Syntax", "data": data},
                )
            space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
            space = connector.get(space_endpoint)
            if "results" in space[2].keys() and len(space[2]["results"]) > 0:
                space_ref = space[2]["results"][0]["id"]
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
            if p_data[0] != "" and p_data[1] != "":
                subnet_endpoint = f"/api/ddi/v1/ipam/subnet?_filter=space=='{space_ref}' and address=='{p_data[0]}' and cidr=={p_data[1]}"
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Invalid syntax for subnet. It should be in the form of a.b.c.d/e",
                        "data": data,
                    },
                )
            subnet = connector.get(subnet_endpoint)
            if "results" in subnet[2].keys() and len(subnet[2]["results"]) > 0:
                subnet_ref = subnet[2]["results"][0]["id"]
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Error in fetching Subnet",
                        "data": data,
                    },
                )
            address_endpoint = f"/api/ddi/v1/{subnet_ref}/nextavailableip"
            address = connector.get(address_endpoint)
            if "results" in address[2].keys() and len(address[2]["results"]) > 0:
                data["address"] = address[2]["results"][0]["address"]
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Error in fetching Next Available IP",
                        "data": data,
                    },
                )

        if "new_address" in data["address"]:
            return update_fixed_address(data)
        else:
            p_data = helper.normalize_ip(data["address"])
            result = get_fixed_address(data)
            payload = {}
            if "results" in result[2].keys() and len(result[2]["results"]) > 0:
                return update_fixed_address(data)
            else:
                space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
                space = connector.get(space_endpoint)
                if "results" in space[2].keys() and len(space[2]["results"]) > 0:
                    payload["ip_space"] = space[2]["results"][0]["id"]
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
                payload["address"] = str(p_data[0])
                payload["name"] = data["name"] if "name" in data.keys() else ""
                payload["match_type"] = data["match_type"] if "match_type" in data.keys() else ""
                payload["match_value"] = data["match_value"] if "match_value" in data.keys() else ""
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                if "tags" in data.keys() and data["tags"] is not None:
                    payload["tags"] = helper.flatten_dict_object("tags", data)
                return connector.create("/api/ddi/v1/dhcp/fixed_address", payload)
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


def delete_fixed_address(data):
    """Delete a BloxOne DDI IPv4 address reservation object"""
    if all(k in data and data[k] is not None for k in ("space", "address")):
        connector = Request(data["host"], data["api_key"])
        helper = Utilities()
        p_data = helper.normalize_ip(data["address"])
        if p_data[0] == "":
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Incorrect address definition",
                    "data": data,
                },
            )
        result = get_fixed_address(data)
        if "results" in result[2].keys() and len(result[2]["results"]) > 0:
            ref_id = result[2]["results"][0]["id"]
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


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        name=dict(type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        match_type=dict(
            type="str",
            choices=["mac", "client_text", "client_hex", "relay_text", "relay_hex"],
        ),
        match_value=dict(type="str"),
        address=dict(type="str"),
        space=dict(type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {
        "present": create_fixed_address,
        "get": get_fixed_address,
        "absent": delete_fixed_address,
    }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
