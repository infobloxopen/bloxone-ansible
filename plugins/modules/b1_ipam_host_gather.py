from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.infoblox.bloxone.plugins.module_utils.b1ddi import Request

DOCUMENTATION = """
---
module: b1_ipam_ip_space
author: "Akhilesh Kabade (@akhilesh-kabade-infoblox)"
short_description: Gather IPAM host facts
description:
  - Gather facts about IPAM hosts in Infoblox BloxOne DDI. This module gathers facts of IPAM Hosts object using BloxOne REST APIs.
requirements:
  - requests
options:
  api_key:
    description:
      - Configures the API token for authentication against Infoblox BloxOne platform.
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

- name: Gather Host
  b1_ipam_host_gather:
    host: "{{ host }}"
    api_key: "{{ api }}"
    state: gather

"""

RETURN = """ # """


def get_host(data):
    """Fetches the BloxOne DDI IPAM Host object"""
    connector = Request(data["host"], data["api_key"])
    endpoint = "/api/ddi/v1/ipam/host"

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

    choice_map = {"gather": get_host}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params["state"])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Operation failed", meta=result)


if __name__ == "__main__":
    main()
