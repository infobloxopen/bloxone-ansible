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
                    # Check for and calculate first|last router
                    if k == 'routers':
                        if v == 'first' or v == 'last':
                            v = self.get_router_ip(data, v)
                    dhcp_option["option_value"] = v
                    dhcp_option["type"] = "option"
                    payload.append(dhcp_option)
        return payload
    

    def get_router_ip(self, data, command):
        """Calculate router ip based on subnet"""
        router = None
        if 'address' in data.keys() and data['address']!=None:
            address = self.normalize_address(data['address'])
            subnet = ipaddress.ip_network(address)
            if command == 'first':
                router = str(subnet.network_address + 1)
            elif command == 'last':
                router = str(subnet.network_address - 2)
            else:
                router = None
        else:
            router = None
        
        return router

    
    def normalize_address(self, data_address):
        """Get raw address from address argument"""
        if 'next' in data_address or 'new' in data_address:
            try:
                address_dict = json.loads(data_address.replace("'","\""))
            except:
                address = None
            if 'next_available_subnet' in address_dict.keys():
                address = address_dict['next_available_subnet']['parent_block']
            elif 'old_address' in address_dict.keys():
                address = address_dict['old_address']
            elif 'new_address' in address_dict.keys():
                address = address_dict['new_address']
            else:
                address = None
        else:
            address = data_address
        
        return address

         
    def hostaddresses(self, key, data, aspace):
        """This utility function is used to add address for IPAM host creation/updation"""
        payload = []
        for i in data[key]:
            for k, v in i.items():
                addr = {}
                for item in aspace:
                    if item["name"] == k:
                        ipspace_id = item["id"]
                        break
                if ipspace_id:
                    addr["space"] = ipspace_id
                    addr["address"] = v
                    payload.append(addr)
        return payload

