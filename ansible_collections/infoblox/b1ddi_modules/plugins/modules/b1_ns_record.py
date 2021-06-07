#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = \
    '''
---
module: dns_view_repo
short_description: Manage your repos on Github

EXAMPLES = \
- name: Create ns
  b1_ns:
    name: "{{ id of the zone }}"
    ns_name: "{{ ns name }}"
    ns_server: "{{ ns server }}"
    type: "NS"
    dns_view_auth_key: "{{ api_key }}"
    host: "{{ host_server }}"
    state: present

- name: Delete ns
  b1_ns:
    dns_view_auth_key: "{{ api_key }}"
    name: "{{ id of the PTR record }}"
    host: "{{ host_server }}"
    state: absent
'''

from ansible.module_utils.basic import *
import requests

def dns_ns_presnt(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['host']
    del data['state']
    del data['dns_view_auth_key']
    data.update({'zone': data['name']})
    del data['name']
    data.update({"name_in_zone": data['ns_name']})
    data.update({'rdata': {'dname': data['ns_server'] }})
    del data['ns_server']
    del data['ns_name']
     

    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/record')
    result = requests.post(url, json.dumps(data), headers=headers)
    #print(result.json())
    
    

    if result.status_code == 201:
        return (False, True, result.json())
    if result.status_code == 200:
        return (False, True, result.json())
    if result.status_code == 422:
        return (False, False, result.json())

    # default: something went wrong

    meta = {'status': result.status_code, 'response': result.json(), 'url': url, 'data': data}
    return (True, False, meta)

def dns_ns_find(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['host']
    del data['state']
    del data['dns_view_auth_key']
    id = data['name']
    data.update({"view": data['name']})
    data.update({"name_in_zone": data['fqdn']})
    del data['name']
    del data['fqdn']
    

    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/record')
    result = requests.get(url, json.dumps(data), headers=headers)
    #print(result.json())
   
   

    if result.status_code == 201:
        return (False, True, result.json())
    if result.status_code == 200:
        return (False, True, result.json())
    if result.status_code == 422:
        return (False, False, result.json())

    # default: something went wrong

    meta = {'status': result.status_code, 'response': result.json()}
    return (True, False, meta)

def dns_ns_delete(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['host']
    #del data['state']
    #del data['dns_view_auth_key']
    #id = data['name']
    #data.update({"view": data['name']})
    #del data['name']
    #data.update({'internal_secondaries': [{'host': data['internal_secondaries']}]})


    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}{}'.format(api_url, 'ddi/v1/', data['name'])
    result = requests.delete(url, headers=headers)
    #print(result.json())



    if result.status_code == 201:
        return (False, True, result.json())
    if result.status_code == 200:
        return (False, True, result.json())
    if result.status_code == 422:
        return (False, False, result.json())

    # default: something went wrong

    result = {'status': result.status_code, 'response': result.json(), 'url': url, 'data': data}
    return (True, False, result )

def main():

    fields = {
        'dns_view_auth_key': {'required': True, 'type': 'str'},
        'name': {'required': False, 'type': 'str'},
        'state': {'default': 'present', 'choices': ['present', 'absent',
                 'gather'], 'type': 'str'},
        'ns_name': {'required': False,'type': 'str'},
        'type': {'required': False, 'type': 'str'},
        'ns_server': {'required': False, 'type': 'str'},
        'host': {'required': True, 'type': 'str'}
        }

    choice_map = {'present': dns_ns_presnt,
                  'gather': dns_ns_find,
                  'absent': dns_ns_delete}

    module = AnsibleModule(argument_spec=fields)
    #test = choice_map.get(module.params['state'])

    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        #print("i am not error")
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Error in dns view operation', meta=result)


if __name__ == '__main__':
    main()
