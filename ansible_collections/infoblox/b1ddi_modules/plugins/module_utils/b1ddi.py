#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# Authors: Amit Mishra (@amishra2-infoblox), Vedant Sethia (@vedantsethia)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
try: 
    import requests
    import json
    import ipaddress
except:
    raise ImportError("Requests module not found")

__metaclass__ = type

class Request(object):
    '''API Request class for Infoblox BloxOne's CRUD API operations
    '''
    def __init__(self,baseUrl, token):
        '''Initialize the API class with baseUrl and API token
        '''
        self.baseUrl = baseUrl
        self.token = token

    def get(self,endpoint,data={}):
        '''GET API request object
        '''
        try:
            headers = {'Authorization': 'Token {}'.format(self.token)}
            url = '{}{}'.format(self.baseUrl, endpoint)
            result = requests.get(url, json.dumps(data), headers=headers)
        except:
            raise Exception("API request failed")
    
        if result.status_code in [200,201,204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {'status': result.status_code, 'response': result.json()}
            return (True, False, meta)
    
    def create(self,endpoint,data={},body=True):
        '''POST API request object
        '''
        try:
            headers = {'Authorization': 'Token {}'.format(self.token)}
            url = '{}{}'.format(self.baseUrl, endpoint)
            if(body==True):
                result = requests.post(url, json.dumps(data), headers=headers)
            else:
                result = requests.post(url, headers=headers)
        except:
            raise Exception("API request failed")
    
        if result.status_code in [200,201,204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {'status': result.status_code, 'response': result.json()}
            return (True, False, meta)
    
    def update(self,endpoint,data={}):
        '''PATCH API request object
        '''
        try:
            headers = {'Authorization': 'Token {}'.format(self.token)}
            url = '{}{}'.format(self.baseUrl, endpoint)
            result = requests.patch(url, json.dumps(data), headers=headers)
        except:
            raise Exception("API request failed")
    
        if result.status_code in [200,201,204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)            
        else:
            meta = {'status': result.status_code, 'response': result.json()}
            return (True, False, meta)

    def put(self,endpoint,data={}):
        '''PUT API request object
        '''
        try:
            headers = {'Authorization': 'Token {}'.format(self.token)}
            url = '{}{}'.format(self.baseUrl, endpoint)
            result = requests.put(url, json.dumps(data), headers=headers)
        except:
            raise Exception("API request failed")
    
        if result.status_code in [200,201,204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)            
        else:
            meta = {'status': result.status_code, 'response': result.json()}
            return (True, False, meta)
    
    def delete(self,endpoint,data={}, body=False):
        '''DELETE API request object
        '''
        try:
            headers = {'Authorization': 'Token {}'.format(self.token)}
            url = '{}{}'.format(self.baseUrl, endpoint)
            if(body==True):
                result = requests.delete(url, json.dumps(data), headers=headers)
            else:
                result = requests.delete(url, headers=headers)
        except:
            raise Exception("API request failed")
    
        if result.status_code in [200,201,204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)            
        else:
            meta = {'status': result.status_code, 'response': result.json()}
            return (True, False, meta)

class Utilities(object):
    '''Helper Functions for BloxOne DDI object operations
    '''
    def __init__(self):
        '''Initializes the object
        '''
        pass

    def normalize_ip(self, address, cidr=-1):
        '''Validates the IP Address
        '''
        address = address.split('/')
        try:
            ipaddress.ip_address(address[0])
        except:
            return ['','']
        if cidr != -1 and int(cidr) < 32:
            return [address[0],cidr]
        elif len(address) == 2:
            return [address[0],address[1]]
        else:    
            return [address[0],'']

    def flatten_dict_object(self,key,data):
        '''Modify the dictionary input object
        '''
        payload = {}
        for i in data[key]:
            for k,v in i.items():
                payload[k]=v
        return payload
    
    def dhcp_options(self, key, data, dhcp_option_codes):
        """Create a list of DHCP option dicts"""
        payload = []
        for i in data[key]:
            for k, v in i.items():
                dhcp_option = {}
                for item in dhcp_option_codes:
                    if item["name"] == k:
                        dhcp_option_code = item["id"]
                        break
                if dhcp_option_code:
                    dhcp_option["option_code"] = dhcp_option_code
                    dhcp_option["option_value"] = v
                    dhcp_option["type"] = "option"
                    payload.append(dhcp_option)
        return payload

