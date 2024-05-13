#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_dhcp_option_space
author: "Akhilesh Kabade (@akhilesh-kabade-infoblox), Sriram Kannan(@kannans)"
short_description: Configure DHCP Option Space on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  -  Create, Update and Delete Option spaces on Infoblox BloxOne DDI. This module manages the IPAM Optionspace object using BloxOne REST APIs.
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
  name:
    description:
      - Configures the name of object to fetch, add, update or remove from the system. User can also update the name as it is possible
        to pass a dict containing I(new_name), I(old_name).
    type: str
    required: true
  protocol:
    description:
      - Configures the protocol,this field is mandatory for only Create flow. It should be either ip4 or ip6.
    type: str
  tags:
    description:
      - Configures the tags associated with the object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the object to add or update from the system.
    type: str
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
   - name: Create Option Space
     b1_dhcp_option_space:
        name: "test"
        protocol: ip4/ip6
        tags:
          - "Org": "Infoblox"
          - "Dept": "QA"
        comment: "This is a test Optionspace to validate Infoblox Ansible Collection"
        host: "{{ host }}"
        api_key: "{{ api }}"
        state: present

   - name: Update Option Space
     b1_dhcp_option_space:
        name: '{"new_name": "test1", "old_name": "test"}'
        tags:
          - "Org": "Infoblox"
          - "Dept": "QA"
        comment: "Updating the Optionspace"
        host: "{{ host }}"
        api_key: "{{ api }}"
        state: present

   - name: Delete Option Space
     b1_dhcp_option_space:
        name: "test"
        host: "{{ host }}"
        api_key: "{{ api }}"
        state: absent

"""

RETURN = """ # """

import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_option_space(data):
    """Fetches the BloxOne DDI Option Space object"""
    connector = Request(data["host"], data["api_key"])
    if data["name"] == "":
        return connector.get("/api/ddi/v1/dhcp/option_space")
    else:
        endpoint = f"/api/ddi/v1/dhcp/option_space?_filter=name==\"{data['name']}\""
        return connector.get(endpoint)


def update_option_space(data):
    """Updates the existing BloxOne DDI Option Space object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if "new_name" in data["name"] and "old_name" in data["name"]:
        try:
            name = json.loads(data["name"])
        except Exception:
            return (
                True,
                False,
                {"status": "400", "response": "Invalid Syntax", "data": data},
            )
        new_name = name["new_name"]
        old_name = name["old_name"]
        data["name"] = old_name
    else:
        new_name = data["name"]

    reference = get_option_space(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "Option Space not found", "data": data},
        )
    payload = {}
    payload["name"] = new_name
    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    if "tags" in data.keys():
        payload["tags"] = helper.flatten_dict_object("tags", data)

    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_option_space(data):
    """Creates a new BloxOne DDI Option Space object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if data["name"] != "":
        if "new_name" in data["name"]:
            return update_option_space(data)
        else:
            option_space = get_option_space(data)
            payload = {}
            if "results" in option_space[2].keys() and len(option_space[2]["results"]) > 0:
                return update_option_space(data)
            else:
                payload["name"] = data["name"]
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                if "protocol" in data.keys() and (data["protocol"] == "ip4" or data["protocol"] == "ip6"):
                    payload["protocol"] = data["protocol"]
                else:
                    return (
                        True,
                        False,
                        {"status": "400", "response": "invalid protocol", "data": data},
                    )
                if "tags" in data.keys():
                    payload["tags"] = helper.flatten_dict_object("tags", data)

                return connector.create("/api/ddi/v1/dhcp/option_space", payload)
    else:
        return (
            True,
            False,
            {"status": "400", "response": "object name not defined", "data": data},
        )


def delete_option_space(data):
    """Delete a BloxOne DDI Option Space object"""
    if data["name"] != "":
        connector = Request(data["host"], data["api_key"])
        option_space = get_option_space(data)
        if "results" in option_space[2].keys() and len(option_space[2]["results"]) > 0:
            ref_id = option_space[2]["results"][0]["id"]
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
            {"status": "400", "response": "object name not defined", "data": data},
        )


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        name=dict(default="", type="str"),
        protocol=dict(default="", type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {
        "present": create_option_space,
        "get": get_option_space,
        "absent": delete_option_space,
    }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
