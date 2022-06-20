from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import *
from ..module_utils.b1ddi import Request, Utilities
import json


EXAMPLES = '''

- name: Gather Host
  b1_ipam_host_gather:
    host: "{{ host }}"
    api_key: "{{ api }}"
    state: gather

'''

RETURN = ''' # '''

def get_host(data):
    '''Fetches the BloxOne DDI IPAM Host object
    '''
    connector = Request(data['host'], data['api_key'])
    endpoint = f'/api/ddi/v1/ipam/host'

    flag=0
    fields=data['fields']
    filters=data['filters']
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
        filters=dict(type='dict', default={}),
        tags=dict(type='list', elements='dict', default=[{}]),
        state=dict(type='str', default='present', choices=['present','absent','gather'])
    )

    choice_map = {
                  'gather': get_host
                  }

    module = AnsibleModule(argument_spec=argument_spec)
    (is_error, has_changed, result) = choice_map.get(module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg='Operation failed', meta=result)

if __name__ == '__main__':
    main()

