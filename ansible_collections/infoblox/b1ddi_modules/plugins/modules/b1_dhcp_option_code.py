#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: b1_dhcp_option_code
author: "Akhilesh Kabade (@akhilesh-kabade-infoblox), Sriram Kannan(@kannans)"
short_description: Configure DHCP Option Code on Infoblox BloxOne DDI
version_added: "1.0.1"
description:
  -  Create, Update and Delete DHCP Option Code on Infoblox BloxOne DDI. This module manages the IPAM Host object using BloxOne REST APIs.
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
      - Configures the name of the Option Code to fetch, add, update or remove from the system. 
    type: str
    required: true
  type:
    description:
      - Configures the type of the Option Code.
    type: str
    required: true
  Code:
    description:
      - Option Code value.
    type: str
    required: true
  option_space:
    description:
      - Name of the Option Space.
    type: str
    required: true
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
   - name: Create Option Code
     b1_dhcp_option_code:
        name: "test"
        type: "address4"
        code: 25
        comment: "This is a test DHCP Option Code to validate Infoblox Ansible Collection"
        option_space: "test1" 
        api_key: "{{ api }}"
        host: "{{ host }}"
        state: present

   - name: Update Option Code
     b1_dhcp_option_code:
        name: '{"new_name":"test","old_name":"test1"}'
        type: "address4"
        code: 25
        comment: "Updating Option Code"
        option_space: "test1" 
        api_key: "{{ api }}"
        host: "{{ host }}"
        state: present

   - name: Delete Option Code
     b1_dhcp_option_code:
        name: "abcde"
        host: "{{ host }}"
        api_key: "{{ api }}"
        state: absent

'''

RETURN = ''' # '''

from ansible.module_utils.basic import *
from ..module_utils.b1ddi import Request, Utilities
import json

def get_option_code(data):
    '''Fetches the BloxOne DDI DHCP Option Code object
    '''
    connector = Request(data['host'], data['api_key'])
    if data['name'] == '':
        return connector.get('/api/ddi/v1/dhcp/option_code')
    else:
        endpoint = '{}\"{}\"'.format('/api/ddi/v1/dhcp/option_code?_filter=name==',data['name'])
        return connector.get(endpoint)

def update_option_code(data):
    '''Updates the existing BloxOne DDI DHCP Option Code object
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

    if "option_space" in data.keys() and data["option_space"] != None:
        endpoint = '{}\"{}\"'.format('/api/ddi/v1/dhcp/option_space?_filter=name==',data['option_space'])
        ospace = connector.get(endpoint)
        if ('results' in ospace[2].keys() and len(ospace[2]['results']) > 0):
            ref_id = ospace[2]['results'][0]['id']
        else:
            return (True,False,{ "status": "400", "response": "Error in fetching option_space","data": data})

        endpoint1 = '{}\"{}\"{}\"{}\"'.format('/api/ddi/v1/dhcp/option_code?_filter=name==',data['name'],'&_option_space==',ref_id)
        oc_obj = connector.get(endpoint1)
    
    if('results' in oc_obj[2].keys() and len(oc_obj[2]['results']) > 0):
        ref_id = oc_obj[2]['results'][0]['id']
    else:
        return(True, False, {'status': '400', 'response': 'Option Code not found', 'data':data})
    payload={}
    payload['name'] = new_name
    if 'type' in data.keys():
      payload['type'] = data['type']
    if 'code' in data.keys():
      payload['code'] = data['code']
    if 'comment' in data.keys():
      payload['comment']= data['comment']
    payload['option_space'] = ospace[2]['results'][0]['id']
        
    endpoint  = '{}{}'.format('/api/ddi/v1/',ref_id)
    return connector.update(endpoint, payload)
    
def create_option_code(data):
    '''Creates a new BloxOne DDI DHCP Option COde object
    '''
    connector = Request(data['host'], data['api_key'])
    helper = Utilities()
    if data['name'] != '':
        if 'new_name' in data['name']:
            return update_option_code(data)
        else:
            if "option_space" in data.keys() and data["option_space"] != None:
                endpoint = '{}\"{}\"'.format('/api/ddi/v1/dhcp/option_space?_filter=name==',data['option_space'])
                ospace = connector.get(endpoint)
                if ('results' in ospace[2].keys() and len(ospace[2]['results']) > 0):
                    ref_id = ospace[2]['results'][0]['id']
                else:
                    return (True,False,
                            {
                                "status": "400",
                                "response": "Error in fetching option_space",
                                "data": data,
                            },
                        )

            endpoint1 = '{}\"{}\"{}\"{}\"'.format('/api/ddi/v1/dhcp/option_code?_filter=name==',data['name'],'&_option_space==',ref_id)
            oc_obj = connector.get(endpoint1)
            
            if('results' in oc_obj[2].keys() and len(oc_obj[2]['results']) > 0):
                return update_option_code(data)
            else:
                payload={}
                if 'name' not in data.keys() or 'type' not in data.keys() or 'code' not in data.keys():
                    return(True, False, {'status': '400', 'response': 'invalid input','data':data})
                if (data['name'] == '' or data['type']=='' or data['code']==''):
                    return(True, False, {'status': '400', 'response': 'invalid input','data':data})
                payload['name'] = data['name']
                payload['type'] = data['type'] 
                payload['code'] = data['code'] 
                payload['comment']= data['comment'] if 'comment' in data.keys() else ''
                
                payload['option_space'] = ospace[2]['results'][0]['id']
                        
                   
                return connector.create('/api/ddi/v1/dhcp/option_code', payload)
    else:
        return(True, False, {'status': '400', 'response': 'object name not defined','data':data})                

def delete_option_code(data):
    '''Delete a BloxOne DDI DHCP Option Code object
    '''
    if data['name'] != '':
        connector = Request(data['host'], data['api_key'])
        oc_obj = get_option_code(data)
        if('results' in oc_obj[2].keys() and len(oc_obj[2]['results']) > 0):
            ref_id = oc_obj[2]['results'][0]['id']
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
        type=dict(default='', type='str'),
        code=dict(default='', type='int'),
        comment=dict(default='', type='str'),
        option_space=dict(default='', type='str'),   
        api_key=dict(required=True, type='str'),
        host=dict(required=True, type='str'),
        state=dict(type='str', default='present', choices=['present','absent','get'])
    )

    choice_map = {'present': create_option_code,
                  'get': get_option_code,
                  'absent': delete_option_code}

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Operation failed', meta=result)

if __name__ == '__main__':
    main()

