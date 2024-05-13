#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_fixed_address
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
    state:
        description:
            - Indicate desired state of the object
        type: str
        required: false
        choices:
            - present
            - absent
        default: present
    address:
        description: >
            The reserved address.
        type: str
    comment:
        description: >
            The description for the fixed address. May contain 0 to 1024 characters. Can include UTF-8.
        type: str
    dhcp_options:
        description: >
            The list of DHCP options. May be either a specific option or a group of options.
        type: list
        elements: dict
        suboptions:
            group:
                description: >
                    The resource identifier.
                type: str
            option_code:
                description: >
                    The resource identifier.
                type: str
            option_value:
                description: >
                    The option value.
                type: str
            type:
                description: >
                    The type of item.
                    
                    Valid values are:
                    * I(group)
                    * I(option)
                type: str
    disable_dhcp:
        description: >
            Optional. I(true) to disable object. The fixed address is converted to an exclusion when generating configuration.
            
            Defaults to I(false).
        type: bool
    header_option_filename:
        description: >
            The configuration for header option filename field.
        type: str
    header_option_server_address:
        description: >
            The configuration for header option server address field.
        type: str
    header_option_server_name:
        description: >
            The configuration for header option server name field.
        type: str
    hostname:
        description: >
            The DHCP host name associated with this fixed address. It is of FQDN type and it defaults to empty.
        type: str
    inheritance_parent:
        description: >
            The resource identifier.
        type: str
    inheritance_sources:
        description: >
            The inheritance configuration.
        type: dict
        suboptions:
            dhcp_options:
                description: >
                    The inheritance configuration for I(dhcp)options_ field.
                type: dict
                suboptions:
                    action:
                        description: >
                            The inheritance setting.
                            
                            Valid values are:
                            * I(inherit): Use the inherited value.
                            * I(block): Don't use the inherited value.
                            
                            Defaults to I(inherit).
                        type: str
                    value:
                        description: >
                            The inherited DHCP option values.
                        type: list
                        elements: dict
                        suboptions:
                            action:
                                description: >
                                    The inheritance setting.
                                    
                                    Valid values are:
                                    * I(inherit): Use the inherited value.
                                    * I(block): Don't use the inherited value.
                                    
                                    Defaults to I(inherit).
                                type: str
            header_option_filename:
                description: >
                    The inheritance configuration for I(header)optionI(filename) field.
                type: dict
                suboptions:
                    action:
                        description: >
                            The inheritance setting for a field.
                            
                            Valid values are:
                            * I(inherit): Use the inherited value.
                            * I(override): Use the value set in the object.
                            
                            Defaults to I(inherit).
                        type: str
            header_option_server_address:
                description: >
                    The inheritance configuration for I(header)optionI(server)address_ field.
                type: dict
                suboptions:
                    action:
                        description: >
                            The inheritance setting for a field.
                            
                            Valid values are:
                            * I(inherit): Use the inherited value.
                            * I(override): Use the value set in the object.
                            
                            Defaults to I(inherit).
                        type: str
            header_option_server_name:
                description: >
                    The inheritance configuration for I(header)optionI(server)name_ field.
                type: dict
                suboptions:
                    action:
                        description: >
                            The inheritance setting for a field.
                            
                            Valid values are:
                            * I(inherit): Use the inherited value.
                            * I(override): Use the value set in the object.
                            
                            Defaults to I(inherit).
                        type: str
    ip_space:
        description: >
            The resource identifier.
        type: str
    match_type:
        description: >
            Indicates how to match the client:
            * I(mac): match the client MAC address for both IPv4 and IPv6,
            * I(client)textI( or )clientI(hex): match the client identifier for IPv4 only,
            * I(relay)textI( or )relayI(hex): match the circuit ID or remote ID in the DHCP relay agent option (82) for IPv4 only,
            * I(duid): match the DHCP unique identifier, currently match only for IPv6 protocol.
        type: str
    match_value:
        description: >
            The value to match.
        type: str
    name:
        description: >
            The name of the fixed address. May contain 1 to 256 characters. Can include UTF-8.
        type: str
    parent:
        description: >
            The resource identifier.
        type: str
    tags:
        description: >
            The tags for the fixed address in JSON format.
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the FixedAddress object
    type: str
    returned: Always
result:
    description:
        - FixedAddress object
    type: complex
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
    from ipam import FixedAddressApi, FixedAddress
except ImportError:
    HAS_BLOXONE_CLIENT = False
    HAS_BLOXONE_CLIENT_IMP_ERR = traceback.format_exc()
else:
    HAS_BLOXONE_CLIENT = True
    HAS_BLOXONE_CLIENT_IMP_ERR = None


class FixedAddressModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(FixedAddressModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._payload_params = None
        self._payload = None

    @property
    def existing(self):
        if self._existing:
            return self._existing

        self._existing = self.find()
        return self._existing

    @property
    def payload_params(self):
        if self._payload_params:
            return self._payload_params

        exclude = ['state', 'csp_url', 'api_key', 'id']
        # remove none values or if key is not in __props__ of FixedAddress
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        return self._payload_params

    @property
    def payload(self):
        if self._payload:
            return self._payload

        self._payload = FixedAddress.from_dict(self.payload_params)
        return self._payload

    def payload_changed(self):
        if self.existing is None:
            # if existing is None, then it is a create operation
            return True

        return self.is_changed(self.existing.model_dump(by_alias=True, exclude_none=True), self.payload_params)

    def find(self):
        if self.params['id'] is not None:
            try:
                resp = FixedAddressApi(self.client).read(self.params['id'], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params['state'] == 'absent':
                    return None
                raise e
        else :
            filter = "address=='{0}' and ip_space=='{1}'".format(self.params['address'], self.params['ip_space'])
            resp = FixedAddressApi(self.client).list(filter=filter, inherit="full")
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg="Found multiple FixedAddress: {0}".format(resp.results))
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = FixedAddressApi(self.client).create(body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        resp = FixedAddressApi(self.client).update(id=self.existing.id, body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        FixedAddressApi(self.client).delete(self.existing.id)

    def run_command(self):
        # seed the result dict in the object
        # we primarily care about changed and state
        # changed is if this module effectively modified the target
        # state will include any data that you want your module to pass back
        # for consumption, for example, in a subsequent task
        result = dict(
            changed=False,
            result={},
            id=None
        )

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            item = {}
            if self.params['state'] == 'present' and self.existing is None:
                item = self.create()
                result['changed'] = True
                result['msg'] = "FixedAddress created"
            elif self.params['state'] == 'present' and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result['changed'] = True
                    result['msg'] = "FixedAddress updated"
            elif self.params['state'] == 'absent' and self.existing is not None:
                self.delete()
                result['changed'] = True
                result['msg'] = "FixedAddress deleted"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result['diff'] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result.update(item)
        except ApiException as e:
            self.fail_json(msg="Failed to execute command: {0} {1} {2}".format(e.status, e.reason, e.body))

        # in the event of a successful module execution, you will want to
        # simple BloxoneAnsibleModule.exit_json(), passing the key/value results
        self.exit_json(**result)


def main():
    object_args = dict(
        address=dict(type='str'),
        comment=dict(type='str'),
        dhcp_options=dict(type='list', elements='dict', options=dict(
            group=dict(type='str'),
            option_code=dict(type='str'),
            option_value=dict(type='str'),
            type=dict(type='str'),
        )),
        disable_dhcp=dict(type='bool'),
        header_option_filename=dict(type='str'),
        header_option_server_address=dict(type='str'),
        header_option_server_name=dict(type='str'),
        hostname=dict(type='str'),
        inheritance_parent=dict(type='str'),
        inheritance_sources=dict(type='dict', options=dict(
            dhcp_options=dict(type='dict', options=dict(
                action=dict(type='str'),
                value=dict(type='list', elements='dict', options=dict(
                    action=dict(type='str'),
                )),
            )),
            header_option_filename=dict(type='dict', options=dict(
                action=dict(type='str'),
            )),
            header_option_server_address=dict(type='dict', options=dict(
                action=dict(type='str'),
            )),
            header_option_server_name=dict(type='dict', options=dict(
                action=dict(type='str'),
            )),
        )),
        ip_space=dict(type='str'),
        match_type=dict(type='str'),
        match_value=dict(type='str'),
        name=dict(type='str'),
        parent=dict(type='str'),
        tags=dict(type='dict'),
    )

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type='str', required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        api_key=dict(type='str', required=True, no_log=True),
        csp_url=dict(type='str', default="https://csp.infoblox.com"),
    )
    module_args.update(object_args)

    c = FixedAddressModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[('state', 'present', ['address', 'ip_space', 'match_type', 'match_value'])],
    )
    c.run_command()


if __name__ == '__main__':
    main()
