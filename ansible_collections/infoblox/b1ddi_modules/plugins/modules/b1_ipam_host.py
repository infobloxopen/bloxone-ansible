#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: b1_ipam_host
author: "Akhilesh Kabade (@akhilesh-kabade-infoblox), Sriram Kannan(@kannans)"
short_description: Configure Host on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  -  Create, Update and Delete Hosts on Infoblox BloxOne DDI. This module manages the IPAM Host object using BloxOne REST APIs.
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
  addresses:
    description:
      - Configures the name of IP Space and the associated Address for the Host
        When fetching, the address field can be in the form “a.b.c.d”. 
    type: list
    required: true
  name:
    description:
      - Configures the name of IPAM Host to fetch, add, update or remove from the system. User can also update the name as it is possible
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
      - present
      - absent
    required: true
'''

EXAMPLES = '''
   - name: Create Host 
      b1_ipam_host:
        name: "Test-Ansible-host"
        comment: "This is created by QA"
        addresses:
          - "ip_space" : "{{address}}"
        tags:
          - "Org": "Infoblox"
          - "Dept": "Engineering"
        api_key: "{{ api }}"
        host: "{{ host }}"
        state: present

   - name: Update Host 
      b1_ipam_host:
        name: "Test-Ansible-host"
        comment: "This is created by QA"
        addresses:
          - "ip_space" : "{{address}}"
        tags:
          - "Org": "Infoblox"
          - "Dept": "Engineering"
        api_key: "{{ api }}"
        host: "{{ host }}"
        state: present

   - name: Delete Host
      b1_ipam_host:
        name: "host"
        host: "{{ host }}"
        api_key: "{{ api }}"
        state: absent

'''

RETURN = ''' # '''

from ansible.module_utils.basic import *
from ..module_utils.b1ddi import Request, Utilities
import json

def get_host(data):
    '''Fetches the BloxOne DDI Host object
    '''
    connector = Request(data['host'], data['api_key'])
    if data['name'] == '':
        return connector.get('/api/ddi/v1/ipam/host')
    else:
        endpoint = '{}\"{}\"'.format('/api/ddi/v1/ipam/host?_filter=name==',data['name'])
        return connector.get(endpoint)

def update_host(data):
    '''Updates the existing BloxOne DDI Host object
    '''
    connector = Request(data['host'], data['api_key'])
    helper = Utilities()
    if 'new_name' and 'old_name' in data['name']:
        try:
            name = json.loads(data['name'])
        except:
            return(True, False, {'status': '400', 'response': 'Invalid Syntax', 'data':data})
        new_name = name['new_name']
        old_name = name['old_name']
        data['name'] = old_name
    else:
        new_name = data['name']

    reference = get_host(data)
    if('results' in reference[2].keys() and len(reference[2]['results']) > 0):
        ref_id = reference[2]['results'][0]['id']
    else:
        return(True, False, {'status': '400', 'response': 'Host not found', 'data':data})
    payload={}
    payload['name'] = new_name
    payload['comment'] = data['comment'] if 'comment' in data.keys() else ''
    if 'tags' in data.keys():
        payload['tags']=helper.flatten_dict_object('tags',data)
    if "addresses" in data.keys() and data["addresses"] != None:
                    aspace = connector.get("/api/ddi/v1/ipam/ip_space")
                    if (
                        "results" in aspace[2].keys()
                        and len(aspace[2]["results"]) > 0
                    ):
                        payload["addresses"] = helper.hostaddresses(
                            "addresses", data, aspace[2]["results"]
                        )
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Error in fetching addresses",
                                "data": data,
                            },
                        )
    endpoint  = '{}{}'.format('/api/ddi/v1/',ref_id)
    return connector.update(endpoint, payload)
    
def create_host(data):
    '''Creates a new BloxOne DDI Host object
    '''
    connector = Request(data['host'], data['api_key'])
    helper = Utilities()
    if data['name'] != '':
        if 'new_name' in data['name']:
            return update_host(data)
        else:
            host_obj = get_host(data)
            payload={}
            if('results' in host_obj[2].keys() and len(host_obj[2]['results']) > 0):
                return update_host(data)
            else:
                payload['name'] = data['name']
                payload['comment'] = data['comment'] if 'comment' in data.keys() else ''
                if 'tags' in data.keys():
                    payload['tags']=helper.flatten_dict_object('tags',data)
                if "addresses" in data.keys() and data["addresses"] != None:
                    aspace = connector.get("/api/ddi/v1/ipam/ip_space")
                    if (
                        "results" in aspace[2].keys()
                        and len(aspace[2]["results"]) > 0
                    ):
                        payload["addresses"] = helper.hostaddresses(
                            "addresses", data, aspace[2]["results"]
                        )
                    else:
                        return (
                            True,
                            False,
                            {
                                "status": "400",
                                "response": "Error in fetching addresses",
                                "data": data,
                            },
                        )
                return connector.create('/api/ddi/v1/ipam/host', payload)
    else:
        return(True, False, {'status': '400', 'response': 'object name not defined','data':data})                

def delete_host(data):
    '''Delete a BloxOne DDI Host object
    '''
    if data['name'] != '':
        connector = Request(data['host'], data['api_key'])
        host_obj = get_host(data)
        if('results' in host_obj[2].keys() and len(host_obj[2]['results']) > 0):
            ref_id = host_obj[2]['results'][0]['id']
            endpoint = '{}{}'.format('/api/ddi/v1/', ref_id)
            return connector.delete(endpoint)
        else:
            return(True, False, {'status': '400', 'response': 'Object not found','data':data})
    else:
        return(True, False, {'status': '400', 'response': 'object name not defined','data':data})  

def main():
    '''Main entry point for module execution
    '''
    argument_spec = dict(
        name=dict(default='', type='str'),
        addresses=dict(type="list", elements="dict", default=[{}]),
        api_key=dict(required=True, type='str'),
        host=dict(required=True, type='str'),
        comment=dict(type='str'),
        tags=dict(type='list', elements='dict', default=[{}]),
        state=dict(type='str', default='present', choices=['present','absent','get'])
    )

    choice_map = {'present': create_host,
                  'get': get_host,
                  'absent': delete_host}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Operation failed', meta=result)

if __name__ == '__main__':
    main()

