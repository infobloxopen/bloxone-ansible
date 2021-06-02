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

- name: Create dns view
  b1_dns_record:
     name: "{{ Name of the view }}"
     dns_view_auth_key: "{{ api_key }}"
     state: present
     host: "{{ host_server }}"

- name: Delete dns view
  b1_dns_record:
    name: "{{ Name of the view }}"
    dns_view_auth_key: "{{ api_key }}"
    state: absent
    host: "{{ host_server }}"
'''

from ansible.module_utils.basic import *
import requests


def dns_view_present(data):

    api_key = data['dns_view_auth_key']
    api_url = data['host'] + "/api/"

    del data['state']
    del data['dns_view_auth_key']
    del data['host']

    headers = {'Authorization': 'token {}'.format(api_key)}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/view')
    result = requests.post(url, json.dumps(data), headers=headers)
    #print(result.json())

    if result.status_code == 201:
        return (False, True, result.json())
    if result.status_code == 200:
        return (False, True, result.json())
    if result.status_code == 422:
        return (False, False, result.json())

    # default: something went wrong

    result = {'status': result.status_code, 'response': result.json()}
    return (True, False, result)


def dns_view_absent(data=None):
    api_url = data['host'] + "/api/"
    del data['host']
    headers = {'Authorization': 'token {}'.format(data['dns_view_auth_key'])}
    url = '{}{}{}'.format(api_url, 'ddi/v1/', data['name'])
    #url = '{}{}'.format(api_url, 'ddi/v1/', data['name'])
    result = requests.delete(url, headers=headers)
    print(url)

    if result.status_code == 200:
        return (False, True, {'status': 'SUCCESS'})
    if result.status_code == 404:
        result = {'status': result.status_code, 'data': result.json()}
        return (False, False, result)
    else:
        result = {'status': result.status_code, 'data': result.json(), 'url': url, 'id': data['name']}
        return (True, False, result)


def dns_view_find(data=None):

    #print(data)
    api_url = data['host'] + "/api/"
    del data['host']

    headers = {'Authorization': 'token {}'.format(data['dns_view_auth_key'])}
    url = '{}{}'.format(api_url, 'ddi/v1/dns/view')
    #url = 'https://env-6.test.infoblox.com/api/ddi/v1/dns/view'
    result = requests.get(url, headers=headers)


    print(type(result))

    if result.status_code == 200:
       print(" i am BEST")

        #return (False, True, {'status': 'SUCCESS'})

       result1 = result.json()
       #print(type(result1.values()))
       print(type(result1))
       result2=json.dumps(result1)
       print(type(result2))
       #for item in result2:
       #  print(item)
       #result2 = eval(result2)
       #print(result2)
       #print(result3)


       return (False, False, result1)
    if result.status_code == 401:
       print("I am in ERROR")
       result = {'status': result.status_code, 'data': result.json()}
       #return (False, False, result)

    print(" i am BEST2")
    result = {'status': result.status_code, 'response': result.json(), 'data': data}
    return (True, False, result)



def main():

    fields = {
        'dns_view_auth_key': {'required': True, 'type': 'str'},
        'name': {'required': True, 'type': 'str'},
        'state': {'default': 'present', 'choices': ['present', 'absent',
                 'gather', 'present_zone', 'absent_zone' ], 'type': 'str'},
        'host': {'required': True, 'type': 'str'}
        }

    choice_map = {'present': dns_view_present,
                  'gather': dns_view_find,
                   'absent': dns_view_absent }

    module = AnsibleModule(argument_spec=fields)
    test = choice_map.get(module.params['state'])

    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Error in dns view operation', meta=result)


if __name__ == '__main__':
    main()
