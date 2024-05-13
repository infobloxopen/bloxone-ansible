#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_fixed_address_info
short_description: Manage FixedAddress
description:
    - Manage FixedAddress
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    filters:
        description:
            - Filter dict to filter objects
        type: dict
        required: false
    filter_query:
        description:
            - Filter query to filter objects
        type: str
        required: false
    inherit:
        description:
            - Return inheritance information
        type: str
        required: false
        choices:
            - full
            - partial
            - none
        default: full
    tag_filters:
        description:
            - Filter dict to filter objects by tags
        type: dict
        required: false
    tag_filter_query:
        description:
            - Filter query to filter objects by tags
        type: str
        required: false

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the FixedAddress object
    type: str
    returned: Always
results:
    description:
        - FixedAddress object
    type: list
    elements: dict
    returned: Always
    contains:
        address:
            description: >
                The reserved address.
            type: str
            returned: Always
        comment:
            description: >
                The description for the fixed address. May contain 0 to 1024 characters. Can include UTF-8.
            type: str
            returned: Always
        created_at:
            description: >
                Time when the object has been created.
            type: str
            returned: Always
        dhcp_options:
            description: >
                The list of DHCP options. May be either a specific option or a group of options.
            type: list
            returned: Always
            elements: dict
            contains:
                group:
                    description: >
                        The resource identifier.
                    type: str
                    returned: Always
                option_code:
                    description: >
                        The resource identifier.
                    type: str
                    returned: Always
                option_value:
                    description: >
                        The option value.
                    type: str
                    returned: Always
                type:
                    description: >
                        The type of item.
                        
                        Valid values are:
                        * I(group)
                        * I(option)
                    type: str
                    returned: Always
        disable_dhcp:
            description: >
                Optional. I(true) to disable object. The fixed address is converted to an exclusion when generating configuration.
                
                Defaults to I(false).
            type: bool
            returned: Always
        header_option_filename:
            description: >
                The configuration for header option filename field.
            type: str
            returned: Always
        header_option_server_address:
            description: >
                The configuration for header option server address field.
            type: str
            returned: Always
        header_option_server_name:
            description: >
                The configuration for header option server name field.
            type: str
            returned: Always
        hostname:
            description: >
                The DHCP host name associated with this fixed address. It is of FQDN type and it defaults to empty.
            type: str
            returned: Always
        id:
            description: >
                The resource identifier.
            type: str
            returned: Always
        inheritance_assigned_hosts:
            description: >
                The list of the inheritance assigned hosts of the object.
            type: list
            returned: Always
            elements: dict
            contains:
                display_name:
                    description: >
                        The human-readable display name for the host referred to by I(ophid).
                    type: str
                    returned: Always
                host:
                    description: >
                        The resource identifier.
                    type: str
                    returned: Always
                ophid:
                    description: >
                        The on-prem host ID.
                    type: str
                    returned: Always
        inheritance_parent:
            description: >
                The resource identifier.
            type: str
            returned: Always
        inheritance_sources:
            description: >
                The inheritance configuration.
            type: dict
            returned: Always
            contains:
                dhcp_options:
                    description: >
                        The inheritance configuration for I(dhcp)options_ field.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting.
                                
                                Valid values are:
                                * I(inherit): Use the inherited value.
                                * I(block): Don't use the inherited value.
                                
                                Defaults to I(inherit).
                            type: str
                            returned: Always
                        value:
                            description: >
                                The inherited DHCP option values.
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
                                        Valid values are:
                                        * I(inherit): Use the inherited value.
                                        * I(block): Don't use the inherited value.
                                        
                                        Defaults to I(inherit).
                                    type: str
                                    returned: Always
                                display_name:
                                    description: >
                                        The human-readable display name for the object referred to by I(source).
                                    type: str
                                    returned: Always
                                source:
                                    description: >
                                        The resource identifier.
                                    type: str
                                    returned: Always
                                value:
                                    description: >
                                        The inherited value for the DHCP option.
                                    type: dict
                                    returned: Always
                                    contains:
                                        option:
                                            description: >
                                                Option inherited from the ancestor.
                                            type: dict
                                            returned: Always
                                            contains:
                                                group:
                                                    description: >
                                                        The resource identifier.
                                                    type: str
                                                    returned: Always
                                                option_code:
                                                    description: >
                                                        The resource identifier.
                                                    type: str
                                                    returned: Always
                                                option_value:
                                                    description: >
                                                        The option value.
                                                    type: str
                                                    returned: Always
                                                type:
                                                    description: >
                                                        The type of item.
                                                        
                                                        Valid values are:
                                                        * I(group)
                                                        * I(option)
                                                    type: str
                                                    returned: Always
                                        overriding_group:
                                            description: >
                                                The resource identifier.
                                            type: str
                                            returned: Always
                header_option_filename:
                    description: >
                        The inheritance configuration for I(header)optionI(filename) field.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting for a field.
                                
                                Valid values are:
                                * I(inherit): Use the inherited value.
                                * I(override): Use the value set in the object.
                                
                                Defaults to I(inherit).
                            type: str
                            returned: Always
                        display_name:
                            description: >
                                The human-readable display name for the object referred to by I(source).
                            type: str
                            returned: Always
                        source:
                            description: >
                                The resource identifier.
                            type: str
                            returned: Always
                        value:
                            description: >
                                The inherited value.
                            type: str
                            returned: Always
                header_option_server_address:
                    description: >
                        The inheritance configuration for I(header)optionI(server)address_ field.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting for a field.
                                
                                Valid values are:
                                * I(inherit): Use the inherited value.
                                * I(override): Use the value set in the object.
                                
                                Defaults to I(inherit).
                            type: str
                            returned: Always
                        display_name:
                            description: >
                                The human-readable display name for the object referred to by I(source).
                            type: str
                            returned: Always
                        source:
                            description: >
                                The resource identifier.
                            type: str
                            returned: Always
                        value:
                            description: >
                                The inherited value.
                            type: str
                            returned: Always
                header_option_server_name:
                    description: >
                        The inheritance configuration for I(header)optionI(server)name_ field.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting for a field.
                                
                                Valid values are:
                                * I(inherit): Use the inherited value.
                                * I(override): Use the value set in the object.
                                
                                Defaults to I(inherit).
                            type: str
                            returned: Always
                        display_name:
                            description: >
                                The human-readable display name for the object referred to by I(source).
                            type: str
                            returned: Always
                        source:
                            description: >
                                The resource identifier.
                            type: str
                            returned: Always
                        value:
                            description: >
                                The inherited value.
                            type: str
                            returned: Always
        ip_space:
            description: >
                The resource identifier.
            type: str
            returned: Always
        match_type:
            description: >
                Indicates how to match the client:
                * I(mac): match the client MAC address for both IPv4 and IPv6,
                * I(client)textI( or )clientI(hex): match the client identifier for IPv4 only,
                * I(relay)textI( or )relayI(hex): match the circuit ID or remote ID in the DHCP relay agent option (82) for IPv4 only,
                * I(duid): match the DHCP unique identifier, currently match only for IPv6 protocol.
            type: str
            returned: Always
        match_value:
            description: >
                The value to match.
            type: str
            returned: Always
        name:
            description: >
                The name of the fixed address. May contain 1 to 256 characters. Can include UTF-8.
            type: str
            returned: Always
        parent:
            description: >
                The resource identifier.
            type: str
            returned: Always
        tags:
            description: >
                The tags for the fixed address in JSON format.
            type: dict
            returned: Always
        updated_at:
            description: >
                Time when the object has been updated. Equals to I(created)at_ if not updated after creation.
            type: str
            returned: Always
"""  # noqa: E501

import traceback

from ansible_collections.infoblox.bloxone.plugins.module_utils.bloxone import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from ipam import FixedAddressApi
except ImportError:
    HAS_BLOXONE_CLIENT = False
    HAS_BLOXONE_CLIENT_IMP_ERR = traceback.format_exc()
else:
    HAS_BLOXONE_CLIENT = True
    HAS_BLOXONE_CLIENT_IMP_ERR = None


def find(module):
    if module.params['id'] is not None:
        try:
            resp = FixedAddressApi(module.client).read(module.params['id'], inherit="full")
            return [resp.result]
        except NotFoundException as e:
            return None
    else:
        filter = None
        if module.params['filters'] is not None:
            filter = " and ".join(["{0}=='{1}'".format(k, v) for k, v in module.params['filters'].items()])
        elif module.params['filter_query'] is not None:
            filter = module.params['filter_query']

        resp = FixedAddressApi(module.client).list(filter=filter, inherit="full")
        return resp.results


def run_command():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type='str', required=False),
        filters=dict(type='dict', required=False),
        filter_query=dict(type='str', required=False),
        inherit=dict(type='str', required=False, choices=["full", "partial", "none"], default="full"),
        tag_filters=dict(type='dict', required=False),
        tag_filter_query=dict(type='str', required=False),
        api_key=dict(type='str', required=True, no_log=True),
        csp_url=dict(type='str', default="https://csp.infoblox.com"),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        results=[]
    )

    # the BloxoneAnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = BloxoneAnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,

        mutually_exclusive=[
            ['id', 'filters', 'filter_query'],
            ['id', 'tag_filters', 'tag_filter_query'],
        ]
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # based on the state that is passed in, we will execute the appropriate
    # functions
    try:
        results = find(module)
        result['results'] = results.model_dump(by_alias=True, exclude_none=True)
    except ApiException as e:
        module.fail_json(msg="Failed to execute command: {0} {1} {2}".format(e.status, e.reason, e.body))

    # in the event of a successful module execution, you will want to
    # simple BloxoneAnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_command()


if __name__ == '__main__':
    main()
