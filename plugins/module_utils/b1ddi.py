# -*- coding: utf-8 -*-
# Copyright (c) 2021 Infoblox, Inc.
# Authors: Amit Mishra (@amishra2-infoblox), Vedant Sethia (@vedantsethia)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

import ipaddress
import json
import traceback

try:
    import requests
except ImportError:
    HAS_REQUESTS_LIB = False
    REQUESTS_LIB_IMP_ERR = traceback.format_exc()
else:
    HAS_REQUESTS_LIB = True
    REQUESTS_LIB_IMP_ERR = None

__metaclass__ = type


class Request(object):
    """API Request class for Infoblox BloxOne's CRUD API operations"""

    def __init__(self, baseUrl, token):
        """Initialize the API class with baseUrl and API token"""
        self.baseUrl = baseUrl
        self.token = token

        if not HAS_REQUESTS_LIB:
            raise ImportError('Missing required library "requests"') from REQUESTS_LIB_IMP_ERR

    def get(self, endpoint, data=None):
        """GET API request object"""
        if data is None:
            data = {}
        try:
            headers = {"Authorization": f"Token {self.token}"}
            url = f"{self.baseUrl}{endpoint}"
            result = requests.get(url, json.dumps(data), headers=headers)
        except Exception:
            raise Exception("API request failed")

        if result.status_code in [200, 201, 204]:
            return (False, False, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {"status": result.status_code, "response": result.json()}
            return (True, False, meta)

    def create(self, endpoint, data=None, body=True):
        """POST API request object"""
        if data is None:
            data = {}
        try:
            headers = {"Authorization": f"Token {self.token}"}
            url = f"{self.baseUrl}{endpoint}"
            if body:
                result = requests.post(url, json.dumps(data), headers=headers)
            else:
                result = requests.post(url, headers=headers)
        except Exception:
            raise Exception("API request failed")

        if result.status_code in [200, 201, 204]:
            return (False, True, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {"status": result.status_code, "response": result.json()}
            return (True, False, meta)

    def update(self, endpoint, data=None):
        """PATCH API request object"""
        if data is None:
            data = {}
        try:
            headers = {"Authorization": f"Token {self.token}"}
            url = f"{self.baseUrl}{endpoint}"
            result = requests.patch(url, json.dumps(data), headers=headers)
        except Exception:
            raise Exception("API request failed")

        if result.status_code in [200, 201, 204]:
            return (False, True, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {"status": result.status_code, "response": result.json()}
            return (True, False, meta)

    def put(self, endpoint, data=None):
        """PUT API request object"""
        if data is None:
            data = {}
        try:
            headers = {"Authorization": f"Token {self.token}"}
            url = f"{self.baseUrl}{endpoint}"
            result = requests.put(url, json.dumps(data), headers=headers)
        except Exception:
            raise Exception("API request failed")

        if result.status_code in [200, 201, 204]:
            return (False, True, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {"status": result.status_code, "response": result.json()}
            return (True, False, meta)

    def delete(self, endpoint, body=False):
        """DELETE API request object"""
        try:
            headers = {"Authorization": f"Token {self.token}"}
            url = f"{self.baseUrl}{endpoint}"
            if body:
                result = requests.delete(url, headers=headers)
            else:
                result = requests.delete(url, headers=headers)
        except Exception:
            raise Exception("API request failed")

        if result.status_code in [200, 201, 204]:
            return (False, True, result.json())
        elif result.status_code == 401:
            return (True, False, result.content)
        else:
            meta = {"status": result.status_code, "response": result.json()}
            return (True, False, meta)


class Utilities(object):
    """Helper Functions for BloxOne DDI object operations"""

    def __init__(self):
        """Initializes the object"""
        pass

    def normalize_ip(self, address, cidr=-1):
        """Validates the IP Address"""
        address = address.split("/")
        try:
            ipaddress.ip_address(address[0])
        except ValueError:
            return ["", ""]
        if cidr != -1 and int(cidr) < 32:
            return [address[0], cidr]
        elif len(address) == 2:
            return [address[0], address[1]]
        else:
            return [address[0], ""]

    def flatten_dict_object(self, key, data):
        """Modify the dictionary input object"""
        payload = {}
        for i in data[key]:
            for k, v in i.items():
                payload[k] = v
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
                    if k == "routers":
                        if v == "first" or v == "last":
                            v = self.get_router_ip(data, v)
                    dhcp_option["option_value"] = v
                    dhcp_option["type"] = "option"
                    payload.append(dhcp_option)
        return payload

    def get_router_ip(self, data, command):
        """Calculate router ip based on subnet"""
        router = None
        if "address" in data.keys() and data["address"] is not None:
            address = self.normalize_address(data["address"])
            subnet = ipaddress.ip_network(address)
            if command == "first":
                router = str(subnet.network_address + 1)
            elif command == "last":
                router = str(subnet.network_address - 2)
            else:
                router = None
        else:
            router = None

        return router

    def normalize_address(self, data_address):
        """Get raw address from address argument"""
        if "next" in data_address or "new" in data_address:
            try:
                address_dict = json.loads(data_address.replace("'", '"'))
            except TypeError:
                return None
            if "next_available_subnet" in address_dict.keys():
                address = address_dict["next_available_subnet"]["parent_block"]
            elif "old_address" in address_dict.keys():
                address = address_dict["old_address"]
            elif "new_address" in address_dict.keys():
                address = address_dict["new_address"]
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
