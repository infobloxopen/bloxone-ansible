#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = '''
---
lookup: bloxone
author: "Vedant Sethia (@vedantsethia)"
short_description: Query Infoblox BloxOne DDI objects
version_added: "1.0.1"
description:
  - Uses the BloxOne DDI REST API to fetch BloxOne specified objects.  This lookup
    supports adding additional keywords to filter the return data and specify
    the desired set of returned fields.
requirements:
  - requests

options:
    _terms:
      description: The name of the object to return from BloxOne
      required: True
    fields:
      description: The list of field names to return for the specified object.
    filters:
      description: a dict object that is used to filter the return objects
    provider:
      description: a dict object containing BloxOne host name and API key
'''

EXAMPLES = """
- name: fetch all IP Space objects
  ansible.builtin.set_fact:
    ip_space: "{{ lookup('bloxone', '/ipam/ipspace' , filters={'name': 'vsethia-ip-space'}, fields=['id', 'name', 'comment'] , provider={'host': 'https://csp.infoblox.com', 'api_key': 'bd334826af3daff06e05765f1e444ffa'}) }}"

"""

RETURN = ''' # '''

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError
from ansible.module_utils.basic import *
import requests
import json

def get_object(obj_type, provider ,filters, fields):
    '''Creating the GET API request for lookup
    '''
    try:
        host = provider['host']
        key = provider['api_key']
    except:
        return(True, False, {'status': '400', 'response': 'Invalid Syntax for provider', 'provider':provider})
    endpoint = f'/api/ddi/v1/{obj_type}'
    flag=0
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
            
    # reproduced module_utils. Replace once published
    try:
        headers = {'Authorization': 'Token {}'.format(key)}
        url = '{}{}'.format(host, endpoint)
        result = requests.get(url, headers=headers)
    except:
        raise Exception("API request failed")

    if result.status_code in [200,201,204]:
        return (False, False, result.json())
    elif result.status_code == 401:
        return (True, False, result.content)
    else:
        meta = {'status': result.status_code, 'response': result.json()}
        return (True, False, meta)

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        try:
            obj_type = terms[0]
        except IndexError:
            raise AnsibleError('the object_type must be specified')

        fields = kwargs.pop('fields', None)
        filters = kwargs.pop('filters', {})
        provider = kwargs.pop('provider', {})
        res = get_object(obj_type, provider, filters, fields)
        return res
