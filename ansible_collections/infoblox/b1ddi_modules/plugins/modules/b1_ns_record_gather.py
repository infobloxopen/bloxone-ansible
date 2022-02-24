#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: b1_ns_record_gather
author: "amishra2@infoblox"
short_description: Configure IP space on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  - Get, Create, Update and Delete IP spaces on Infoblox BloxOne DDI. This module manages the IPAM IP space object using BloxOne REST APIs.
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
      - gather
    required: true
'''

  
EXAMPLES = '''

'''

RETURN = ''' # '''

from ansible.module_utils.basic import *
from ..module_utils.b1ddi import Request, Utilities
import json

def get_ns_record_gather(data):
    '''Fetches the BloxOne DDI IP Space object
    '''
    '''Fetches the BloxOne DDI IP Space object
    '''
    connector = Request(data['host'], data['api_key'])

    endpoint = f'/api/ddi/v1/dns/record'

    flag=0
    fields=data['fields']
    filters=data['filters']
    if 'name' in filters:
        filters['dns_name_in_zone'] = filters.pop('name')
    if 'dname' in filters:
        filters['dns_rdata'] = filters.pop('dname')
    if fields!=None and isinstance(fields, list):
        temp_fields = ",".join(fields)
        endpoint = endpoint+"?_fields="+temp_fields
        flag=1

    if filters!={} and isinstance(filters,dict):
        temp_filters = []
        for k,v in filters.items():
            if(str(v).isdigit()):
                temp_filters.append(f'{k}=={v}')
            else:
                temp_filters.append(f'{k}==\'{v}\'')
        res = " and ".join(temp_filters)
        if(flag==1):
            endpoint = endpoint+"&_filter="+res
        else:
            endpoint = endpoint+"?_filter="+res

    try:
        return connector.get(endpoint)
    except:
        raise Exception(endpoint)



    if result.status_code in [200,201,204]:
        meta = {'status': result.status_code,'url': url, 'response': result.json()} 
        return (False, False, meta)
    elif result.status_code == 401:
        meta = {'status': result.status_code,'url': url, 'response': result.json()}
        return (True, False, meta)
    else:
        meta = {'status': result.status_code,'url': url, 'response': result.json()}
        return (True, False, meta)


def main():
    '''Main entry point for module execution
    '''
    argument_spec = dict(
        name=dict(default='', type='str'),
        api_key=dict(required=True, type='str'),
        host=dict(required=True, type='str'),
        comment=dict(type='str'),
        fields=dict(type='list'),
        filters=dict(type='dict', default={"type": "NS"}),
        tags=dict(type='list', elements='dict', default=[{}]),
        state=dict(type='str', default='present', choices=['present','absent','gather'])
    )

    choice_map = {
                  'gather': get_ns_record_gather
                  }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Operation failed', meta=result)

if __name__ == '__main__':
    main()
