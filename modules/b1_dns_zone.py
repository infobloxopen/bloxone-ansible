#!/usr/local/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = \
    '''
---
module: dns_view_repo
short_description: Manage your repos on Github
'''

EXAMPLES = \
    '''
- name: Create dns primary zone
  b1_dns_zone:
     name: "{{ name of the zone }}"
     fqdn: "{{ FQDN of the zone }}"
     internal_secondaries: "dns/host/{{ HOST_ID }}"
     primary_type: "cloud"
     dns_view_auth_key: "{{ api_key }}"
     host: "{{ host_server }}"
     state: present

- name: Delete zone
  b1_dns_zone:
    dns_view_auth_key: "{{ api_key }}"
    name: "{{ fqdn of zone }}"
    host: "{{ host_server }}"
    state: absent
'''

from ansible.module_utils.basic import *
import requests

def dns_zone_presnet(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['host']
    del data['state']
    del data['dns_view_auth_key']
    id = data['name']
    del data['id'] 
    data.update({"view": data['name']})
    del data['name']
    data.update({'internal_secondaries': [{'host': data['internal_secondaries']}]})


    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/auth_zone')
    result = requests.post(url, json.dumps(data), headers=headers)



    if result.status_code == 201:
        return (False, True, result.json())
    if result.status_code == 200:
        return (False, True, result.json())
    if result.status_code == 422:
        return (False, False, result.json())

    # default: something went wrong

    meta = {'status': result.status_code, 'response': result.json(), 'data': data }
    return (True, False, meta)


def dns_host_find(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['host']
    del data['state']
    del data['dns_view_auth_key']
    id = data['name']
    data.update({"view": data['name']})
    del data['name']
    data.update({'internal_secondaries': [{'host': data['internal_secondaries']}]})
     

    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'host_app/v1/on_prem_hosts')
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

def dns_zone_find(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"
    del data['state']
    del data['host']
    del data['dns_view_auth_key']
    id = data['name']
    data.update({"view": data['name']})
    del data['name']
    data.update({'internal_secondaries': [{'host': data['internal_secondaries']}]})


    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/auth_zone')
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

def dns_zone_delete(data):

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

    result = {'status': result.status_code, 'response': result.json(), 'url': url}
    return (True, False, result )

def main():

    fields = {
        'dns_view_auth_key': {'required': True, 'type': 'str'},
        'name': {'required': False, 'type': 'str'},
        'state': {'default': 'present', 'choices': ['present', 'absent',
                 'gather','gather_host'], 'type': 'str'},
        'fqdn': {'required': False,'type': 'str'},
         'id': {'required': False,'type': 'str'},
        'primary_type': {'required': False, 'type': 'str'},
        'internal_secondaries': {'required': False, 'type': 'str'},
        'host': {'required': True, 'type': 'str'}
        }

    choice_map = {'present': dns_zone_presnet,
                  'gather': dns_zone_find,
                  'gather_host': dns_host_find,
                  'absent': dns_zone_delete }

    module = AnsibleModule(argument_spec=fields)

    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Error in dns view operation', meta=result)


if __name__ == '__main__':
    main()
