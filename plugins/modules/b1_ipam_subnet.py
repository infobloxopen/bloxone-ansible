#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_ipam_subnet
author: "Amit Mishra (@amishra), Sriram Kannan(@kannans)"
contributor: "Chris Marrison (@ccmarris)"
short_description: Configure Subnet on Infoblox BloxOne DDI
version_added: "1.1.2"
description:
  - Create, Update and Delete Subnets on Infoblox BloxOne DDI. This module manages the IPAM Subnet object using BloxOne REST APIs.
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
      - Configures the address of the subnet to fetch, add, update or remove from the system.
        The address of the subnet in the form "a.b.c.d/n".
        When fetching, the address field can be in the form "a.b.c.d".
    type: str
    required: true
  space:
    description:
      - Configures the name of IP Space containing the subnet to fetch, add, update or remove from the system.
    type: str
    required: true
  dhcp_host:
    description:
      - Configures the name of the on-prem DHCP host for the subnet.
    type: str
  name:
    description:
      - Configures the name of subnet object to fetch, add, update or remove from the system.
    type: str
  dhcp_options:
    description:
      - Configures the DHCP options associated with the subnet.
      - note: routers option supports first|last as special command to assign IP based on subnet
    type: list
  tags:
    description:
      - Configures the tags associated with the subnet object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the subnet object to add or update from the system.
    type: str
  state:
    description:
      - Configures the state of the subnet object on BloxOne DDI. When this value is set to C(get), the object
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

- name: Create Subnet
  b1_ipam_subnet:
    address: "{{ network_address }}"
    space: "{{ ip_space }}"
    name: "{{ subnet_name }}"
    dhcp_host: "{{ onprem_dhcp_host }}"
    tags:
      - key: "{{ value }}"
    dhcp_options:
      - routers: '<first|last|<IP Address>>'
      - key: "{{ value }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Create Subnet using next available function
  b1_ipam_subnet:
    address: '{"next_available_subnet": {"parent_block": "<parent address block>", "cidr": "<cidr of child subnet>", "count": "<quantity>"}}'
    space: "{{ ip_space }}"
    name: "{{ subnet_name }}"
    comment: "{{ comment }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Update Subnet
  b1_ipam_subnet:
    address: '{"new_address": "{{ new address of the subnet }}", "old_address": "{{ old address of the subnet }}"}'
    name: "{{ subnet_name }}"
    dhcp_host: "{{ onprem_dhcp_host }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ comment }}"
    space: "{{ ip_space }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Delete Subnet
  b1_ipam_subnet:
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


def get_subnet(data):
    """Fetches the BloxOne DDI Subnet object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "space" in data.keys() and data["space"] is not None:
        space_endpoint = f"/api/ddi/v1/ipam/ip_space?_filter=name==\"{data['space']}\""
        space = connector.get(space_endpoint)
        if "results" in space[2].keys() and len(space[2]["results"]) > 0:
            space_ref = space[2]["results"][0]["id"]
            if "address" in data.keys() and data["address"] is not None:
                address = helper.normalize_address(data["address"])
                if address:
                    p_data = helper.normalize_ip(address)
                    if p_data[0] != "" and p_data[1] != "":
                        endpoint = f"/api/ddi/v1/ipam/subnet?_filter=space=='{space_ref}' and address=='{p_data[0]}' and cidr=={p_data[1]}"
                    elif p_data[0] != "" and p_data[1] == "":
                        endpoint = f"/api/ddi/v1/ipam/subnet?_filter=space=='{space_ref}' and address=='{p_data[0]}'"
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
                    return (
                        True,
                        False,
                        {
                            "status": "400",
                            "response": "Invalid Address Syntax",
                            "data": data,
                        },
                    )

            else:
                endpoint = f"/api/ddi/v1/ipam/subnet?_filter=space=='{space_ref}'"
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
                endpoint = f"/api/ddi/v1/ipam/subnet?_filter=address=='{p_data[0]}' and cidr=={p_data[1]}"
            elif p_data[0] != "" and p_data[1] == "":
                endpoint = f"/api/ddi/v1/ipam/subnet?_filter=address=='{p_data[0]}'"
            else:
                return (
                    True,
                    False,
                    {"status": "400", "response": "Invalid Address", "data": data},
                )
            return connector.get(endpoint)
        else:
            return connector.get("/api/ddi/v1/ipam/subnet")


def update_subnet(data):
    """Updates the existing BloxOne DDI Subnet object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "new_address" in data["address"]:
        try:
            address = json.loads(data["address"].replace("'", '"'))
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        if "old_address" in address.keys():
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
            new_address = helper.normalize_ip(address["new_address"])
    else:
        new_address = helper.normalize_ip(data["address"])

    reference = get_subnet(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "Subnet not found", "data": data},
        )
    payload = {}
    payload["cidr"] = int(new_address[1])
    # Ensure we don't overwrite existing name/comment
    if "name" in data.keys() and data.get("name"):
        payload["name"] = data["name"]
    if "comment" in data.keys() and data.get("comment"):
        payload["comment"] = data["comment"]
    if "dhcp_host" in data.keys() and data["dhcp_host"] is not None:
        endpoint = f"/api/ddi/v1/dhcp/host?_filter=name==\"{data['dhcp_host']}\""
        dhcp_host = connector.get(endpoint)
        if "results" in dhcp_host[2].keys() and len(dhcp_host[2]["results"]) > 0:
            payload["dhcp_host"] = dhcp_host[2]["results"][0]["id"]
        else:
            # Search for HA_Group if DHCP host is not found.
            endpoint = f"/api/ddi/v1/dhcp/ha_group?_filter=name==\"{data['dhcp_host']}\""
            dhcp_host = connector.get(endpoint)
            if "results" in dhcp_host[2].keys() and len(dhcp_host[2]["results"]) > 0:
                payload["dhcp_host"] = dhcp_host[2]["results"][0]["id"]
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Error in fetching On-prem hosts or host HA group",
                        "data": data,
                    },
                )
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    if "dhcp_options" in data.keys() and data["dhcp_options"] is not None:
        dhcp_option_codes = connector.get("/api/ddi/v1/dhcp/option_code")
        if "results" in dhcp_option_codes[2].keys() and len(dhcp_option_codes[2]["results"]) > 0:
            payload["dhcp_options"] = helper.dhcp_options("dhcp_options", data, dhcp_option_codes[2]["results"])
        else:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Error in fetching DHCP option codes",
                    "data": data,
                },
            )
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_subnet(data):
    """Creates a new BloxOne DDI Subnet object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("space", "address")):
        if "next_available_subnet" in data["address"]:
            return next_available_subnet(data)
        elif "new_address" in data["address"]:
            return update_subnet(data)
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
            subnet = get_subnet(data)
            payload = {}
            if "results" in subnet[2].keys() and len(subnet[2]["results"]) > 0:
                return update_subnet(data)
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
                        # Search for HA_Group if DHCP host is not found.
                        endpoint = '{}"{}"'.format(
                            "/api/ddi/v1/dhcp/ha_group?_filter=name==",
                            data["dhcp_host"],
                        )
                        dhcp_host = connector.get(endpoint)
                        if "results" in dhcp_host[2].keys() and len(dhcp_host[2]["results"]) > 0:
                            payload["dhcp_host"] = dhcp_host[2]["results"][0]["id"]
                        else:
                            return (
                                True,
                                False,
                                {
                                    "status": "400",
                                    "response": "Error in fetching On-prem hosts or host HA group",
                                    "data": data,
                                },
                            )
                payload["address"] = f"{p_data[0]}/{p_data[1]}"
                payload["name"] = data["name"] if "name" in data.keys() else ""
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                if "tags" in data.keys() and data["tags"] is not None:
                    payload["tags"] = helper.flatten_dict_object("tags", data)
                if "dhcp_options" in data.keys() and data["dhcp_options"] is not None:
                    dhcp_option_codes = connector.get("/api/ddi/v1/dhcp/option_code")
                    if "results" in dhcp_option_codes[2].keys() and len(dhcp_option_codes[2]["results"]) > 0:
                        payload["dhcp_options"] = helper.dhcp_options(
                            "dhcp_options", data, dhcp_option_codes[2]["results"]
                        )
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Error in fetching DHCP option codes",
                                "data": data,
                            },
                        )
                return connector.create("/api/ddi/v1/ipam/subnet", payload)
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


def delete_subnet(data):
    """Delete a BloxOne DDI Subnet object"""
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
        subnet = get_subnet(data)
        if "results" in subnet[2].keys() and len(subnet[2]["results"]) > 0:
            ref_id = subnet[2]["results"][0]["id"]
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


def next_available_subnet(data):
    """Implementation of next available functionality"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    try:
        subnet_data = json.loads(data["address"].replace("'", '"'))["next_available_subnet"]
    except Exception:
        return (
            True,
            False,
            {
                "status": 400,
                "response": "Address syntax error, failed to load json data",
                "data": data,
            },
        )
    try:
        if "parent_block" not in subnet_data.keys() or "cidr" not in subnet_data.keys():
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Parent block and CIDR are mandatory fields",
                    "data": data,
                },
            )
        p_data = helper.normalize_ip(subnet_data["parent_block"])
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
        endpoint = f"/api/ddi/v1/ipam/address_block?_filter=space=='{space_ref}' and address=='{p_data[0]}' and cidr=={p_data[1]}"
        address_block = connector.get(endpoint)
        if "results" in address_block[2].keys() and len(address_block[2]["results"]) > 0:
            ref_id = address_block[2]["results"][0]["id"]
        else:
            return (
                True,
                False,
                {"status": "400", "response": "Parent block not found", "data": data},
            )

        count = int(subnet_data["count"]) if "count" in subnet_data.keys() else 1
        cidr = int(subnet_data["cidr"])
        name = data["name"] if "name" in data.keys() else ""
        comment = data["comment"] if "comment" in data.keys() else ""

        # Endpoint API URL
        if name != "" and comment != "":
            endpoint = (
                f"/api/ddi/v1/{ref_id}/nextavailablesubnet?count={count}&cidr={cidr}&name={name}&comment={comment}"
            )
        elif name == "" and comment != "":
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailablesubnet?count={count}&cidr={cidr}&comment={comment}"
        elif name != "" and comment == "":
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailablesubnet?count={count}&cidr={cidr}&name={name}"
        else:
            endpoint = f"/api/ddi/v1/{ref_id}/nextavailablesubnet?count={count}&cidr={cidr}"
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
        dhcp_host=dict(type="str"),
        comment=dict(type="str"),
        dhcp_options=dict(type="list", elements="dict", default=[{}]),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {"present": create_subnet, "get": get_subnet, "absent": delete_subnet}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
