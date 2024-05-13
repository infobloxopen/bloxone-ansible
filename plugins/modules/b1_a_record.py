#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_a_record
author: "Amit Mishra amishra2@infoblox.com"
short_description: Configure DNS Authoritative Zone on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  - Get, Create, Update and Delete DNS Authoritative Zone on Infoblox BloxOne DDI. This module manages the DNS Authoritative Zone object using BloxOne REST APIs.
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
  fqdn:
    description:
      - Configures the fqdn of the DNS Authoritative Zone to fetch, add, update or remove from the system.
      - The fqdn of the DNS Authoritative Zone can be in forward or reverse domain name.
    type: str
    required: true
  internal_secondaries:
    description:
      - Configures the DNS Server configured on Bloxone for the DNS Authoritative Zone to fetch, add, update or remove from the system.
    type: list
    required: true
  external_primaries:
    description:
      - Configures the external primary DNS server associated with the DNS Authoritative Zone object to add or update from the system.
    type: list
  view:
    description:
      - Configures the name of DNS View containing the DNS Authoritative Zone to fetch, add, update or remove from the system.
    type: str 
  primary_type:
    description:
      - Configures the type of the DNS Authoritative Zone object to fetch, add, update or remove from the system. Default is set to 'cloud'.
    type: str
    choices:
      - cloud
      - external
  tags:
    description:
      - Configures the tags associated with the DNS Authoritative Zone object to add or update from the system.
    type: list
  comment:
    description:
      - Configures the comment/description for the DNS Authoritative Zone object to add or update from the system.
    type: str
  state:
    description:
      - Configures the state of the DNS Authoritative Zone object on BloxOne DDI. When this value is set to C(get), the object
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
"""  # noqa: E501


EXAMPLES = """
    - name: GET all A Records
      b1_a_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        state: get

    - name: GET A Records of a zone
      b1_a_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        zone: "{{ Zone_name }}"
        state: get

    - name: GET Specific A Record
      b1_a_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        zone: "{{ Zone_name }}"
        name: "{{ domain name of A Record }}"
        state: get

    - name: CREATE A Record
      b1_a_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        zone: "{{ Zone_name }}"
        address: "{{ ip address of A Record }}"
        name: "{{ domain name of A Record }}"
        state: present


    - name: UPADATE A Record # Only update of Name is supported in this release
      b1_a_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        zone: "{{ Zone_name }}"
        address: "{{ ip address of the record }}"
        name: '{"new_name": "New domain name of the record", "old_name": "Old domain name of the record"}'
        state: present


    - name: Delete A record
      b1_ptr_record:
        api_key: "{{ api_key }}"
        host: "{{ host }}"
        zone: "{{ Zone_name }}"
        name: "{{ domain name of A record }"
        address:  "{{ address of A record }}"
        state: absent
"""

RETURN = """ # """

import json

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_a_record(data):
    """Fetches the BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    if "zone" in data.keys() and data["zone"] is not None:
        zone_endpoint = f"/api/ddi/v1/dns/auth_zone?_filter=fqdn==\"{data['zone']}\""
        zone = connector.get(zone_endpoint)
        if "results" in zone[2].keys() and len(zone[2]["results"]) > 0:
            zone_ref = zone[2]["results"][0]["id"]
            if "name" in data.keys() and data["name"] is not None:
                endpoint = f"/api/ddi/v1/dns/record?_filter=zone=='{zone_ref}' and name_in_zone=='{data['name']}'"
            else:
                endpoint = f"/api/ddi/v1/dns/record?_filter=zone=='{zone_ref}'"
            return connector.get(endpoint)
        else:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Error in fetching DNS Zone",
                    "data": data,
                    "zone": zone,
                },
            )
    else:
        return connector.get("/api/ddi/v1/dns/record")


def update_a_record(data):
    """Updates the existing BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    payload = {}
    if all(k in data["name"] and data["name"] is not None for k in ("new_name", "old_name")):
        try:
            name = json.loads(data["name"])
        except Exception:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Invalid Syntax",
                    "where": "i am in update",
                    "data": data,
                },
            )
        new_name = name["new_name"]
        old_name = name["old_name"]
        data["name"] = old_name
        payload["name_in_zone"] = new_name
        data["name"] = old_name
        payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    reference = get_a_record(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "Address Block not found", "data": data},
        )
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_a_record(data):
    """Creates a new BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("name", "zone")):
        if "new_name" in data["name"]:
            return update_a_record(data)
        else:
            auth_zone = get_a_record(data)
            payload = {}
            if "results" in auth_zone[2].keys() and len(auth_zone[2]["results"]) > 0:
                return update_a_record(data)
            else:
                zone_endpoint = f"/api/ddi/v1/dns/auth_zone?_filter=fqdn==\"{data['zone']}\""
                zone = connector.get(zone_endpoint)
                if "results" in zone[2].keys() and len(zone[2]["results"]) > 0:
                    payload["zone"] = zone[2]["results"][0]["id"]
                    payload["name_in_zone"] = data["name"]
                    payload["rdata"] = {"address": data["address"]}
                    payload["type"] = "A"
                    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                    if "tags" in data.keys() and data["tags"] is not None:
                        payload["tags"] = helper.flatten_dict_object("tags", data)
                    return connector.create("/api/ddi/v1/dns/record", payload)
                else:
                    return (
                        True,
                        False,
                        {
                            "status": "400",
                            "response": "Error in fetching DNS Zone",
                            "data": data,
                        },
                    )
    else:
        return (
            True,
            False,
            {
                "status": "400",
                "response": "Zone or Record Name not defined",
                "data": data,
            },
        )


def delete_a_record(data):
    """Delete a BloxOne DDI DNS Authoritative Zone object"""
    if all(k in data and data[k] is not None for k in ("name", "zone")):
        connector = Request(data["host"], data["api_key"])
        record_data = get_a_record(data)
        if "results" in record_data[2].keys() and len(record_data[2]["results"]) > 0:
            ref_id = record_data[2]["results"][0]["id"]
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
            {"status": "400", "response": "FQDN or DNS View not defined", "data": data},
        )


def main():
    """Main entry point for module execution"""
    argument_spec = dict(
        zone=dict(type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        name=dict(type="str"),
        address=dict(type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {
        "present": create_a_record,
        "get": get_a_record,
        "absent": delete_a_record,
    }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
