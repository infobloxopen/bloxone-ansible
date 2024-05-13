#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: b1_dns_auth_zone
author: "Vedant Sethia (@vedantsethia) Amit Mishra ( @amishra2) Sriram Kanan"
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
        The fqdn of the DNS Authoritative Zone can be in forward or reverse domain name.
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
- name: GET all DNS Authoritative Zones
  b1_dns_auth_zone:
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: get

- name: GET DNS Authoritative Zone
  b1_dns_auth_zone:
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    view: "{{ Name of the View}}"
    fqdn: "{{ Name of the Zone }}"
    state: get

- name: Create DNS Authoritative Zone
  b1_dns_auth_zone:
    fqdn: "{{ Name of the Zone }}"
    view: "{{ Name of the View }}"
    primary_type: "{{ Type of the Zone - cloud/external }}"
    internal_secondaries:
      - "{{ Name of the On Prem Host }}"
    tags:
      - key: "{{ value }}"
    comment: "{{ Description }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Update DNS Authoritative Zone
  b1_dns_auth_zone:
    fqdn: "{{ Name of the Zone }}"
    view: "{{ Name of the View }}"
    internal_secondaries:
      - "{{ Name of the On Prem Host}}"
    tags:
      - key: "{{ value }}"
    comment: "{{ Description }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: present

- name: Delete DNS Authoritative Zone
  b1_dns_auth_zone:
    fqdn: "{{ Name of the Zone }}"
    view: "{{ Name of the View }}"
    api_key: "{{ api_token }}"
    host: "{{ host_server }}"
    state: absent
"""

RETURN = """ # """

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request, Utilities


def get_auth_zone(data):
    """Fetches the BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    if "view" in data.keys() and data["view"] is not None:
        view_endpoint = f"/api/ddi/v1/dns/view?_filter=name==\"{data['view']}\""
        view = connector.get(view_endpoint)
        if "results" in view[2].keys() and len(view[2]["results"]) > 0:
            view_ref = view[2]["results"][0]["id"]
            if "fqdn" in data.keys() and data["fqdn"] is not None:
                endpoint = f"/api/ddi/v1/dns/auth_zone?_filter=view=='{view_ref}' and fqdn=='{data['fqdn']}'"
            else:
                endpoint = f"/api/ddi/v1/dns/auth_zone?_filter=view=='{view_ref}'"
            return connector.get(endpoint)
        else:
            return (
                True,
                False,
                {
                    "status": "400",
                    "response": "Error in fetching DNS View",
                    "data": data,
                },
            )
    else:
        if "fqdn" in data.keys() and data["fqdn"] is not None:
            endpoint = f"/api/ddi/v1/dns/auth_zone?_filter=fqdn=='{data['fqdn']}'"
            return connector.get(endpoint)
        else:
            return connector.get("/api/ddi/v1/dns/auth_zone")


def update_auth_zone(data):
    """Updates the existing BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    reference = get_auth_zone(data)
    if "results" in reference[2].keys() and len(reference[2]["results"]) > 0:
        ref_id = reference[2]["results"][0]["id"]
    else:
        return (
            True,
            False,
            {"status": "400", "response": "Authoritative Zone not found", "data": data},
        )
    payload = {}
    payload["comment"] = data["comment"] if "comment" in data.keys() else ""
    if "external_primaries" in data.keys() and data["external_primaries"] is not None:
        # payload['external_primaries']=helper.flatten_dict_object('external_primaries',data)
        payload["external_primaries"] = data["external_primaries"]
    if "internal_secondaries" in data.keys() and data["internal_secondaries"] is not None:
        payload["internal_secondaries"] = []
        for i in data["internal_secondaries"]:
            endpoint = f'/api/ddi/v1/dns/host?_filter=name=="{i}"'
            dns_host = connector.get(endpoint)
            if "results" in dns_host[2].keys() and len(dns_host[2]["results"]) > 0:
                ref = dns_host[2]["results"][0]["id"]
                payload["internal_secondaries"].append({"host": ref})
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Error in fetching DNS On-prem hosts",
                        "data": data,
                    },
                )
    if "tags" in data.keys() and data["tags"] is not None:
        payload["tags"] = helper.flatten_dict_object("tags", data)
    endpoint = f"/api/ddi/v1/{ref_id}"
    return connector.update(endpoint, payload)


def create_auth_zone(data):
    """Creates a new BloxOne DDI DNS Authoritative Zone object"""
    connector = Request(data["host"], data["api_key"])
    helper = Utilities()
    if all(k in data and data[k] is not None for k in ("view", "fqdn")):
        auth_zone = get_auth_zone(data)
        payload = {}
        if "results" in auth_zone[2].keys() and len(auth_zone[2]["results"]) > 0:
            return update_auth_zone(data)
        else:
            view_endpoint = f"/api/ddi/v1/dns/view?_filter=name==\"{data['view']}\""
            view = connector.get(view_endpoint)
            if "results" in view[2].keys() and len(view[2]["results"]) > 0:
                payload["view"] = view[2]["results"][0]["id"]
                payload["primary_type"] = data["primary_type"] if "primary_type" in data.keys() else ""
                payload["comment"] = data["comment"] if "comment" in data.keys() else ""
                payload["fqdn"] = data["fqdn"]
                if "external_primaries" in data.keys() and data["external_primaries"] is not None:
                    # payload['external_primaries']=helper.flatten_dict_object('external_primaries',data)
                    payload["external_primaries"] = data["external_primaries"]
                if "tags" in data.keys() and data["tags"] is not None:
                    payload["tags"] = helper.flatten_dict_object("tags", data)
                if "internal_secondaries" in data.keys() and data["internal_secondaries"] is not None:
                    payload["internal_secondaries"] = []
                    for i in data["internal_secondaries"]:
                        endpoint = f'/api/ddi/v1/dns/host?_filter=name=="{i}"'
                        dns_host = connector.get(endpoint)
                        if "results" in dns_host[2].keys() and len(dns_host[2]["results"]) > 0:
                            ref = dns_host[2]["results"][0]["id"]
                            payload["internal_secondaries"].append({"host": ref})
                        else:
                            return (
                                True,
                                False,
                                {
                                    "status": "400",
                                    "response": "Error in fetching DNS On-prem hosts",
                                    "data": data,
                                },
                            )
                return connector.create("/api/ddi/v1/dns/auth_zone", payload)
            else:
                return (
                    True,
                    False,
                    {
                        "status": "400",
                        "response": "Error in fetching DNS View",
                        "data": data,
                    },
                )
    else:
        return (
            True,
            False,
            {"status": "400", "response": "FQDN or DNS View not defined", "data": data},
        )


def delete_auth_zone(data):
    """Delete a BloxOne DDI DNS Authoritative Zone object"""
    if all(k in data and data[k] is not None for k in ("view", "fqdn")):
        connector = Request(data["host"], data["api_key"])
        auth_zone = get_auth_zone(data)
        if "results" in auth_zone[2].keys() and len(auth_zone[2]["results"]) > 0:
            ref_id = auth_zone[2]["results"][0]["id"]
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
        fqdn=dict(type="str"),
        api_key=dict(required=True, type="str"),
        host=dict(required=True, type="str"),
        primary_type=dict(type="str"),
        internal_secondaries=dict(type="list", elements="str", default=[""]),
        external_primaries=dict(type="list", elements="str", default=[]),
        view=dict(type="str"),
        comment=dict(type="str"),
        tags=dict(type="list", elements="dict", default=[{}]),
        state=dict(type="str", default="present", choices=["present", "absent", "get"]),
    )

    choice_map = {
        "present": create_auth_zone,
        "get": get_auth_zone,
        "absent": delete_auth_zone,
    }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
