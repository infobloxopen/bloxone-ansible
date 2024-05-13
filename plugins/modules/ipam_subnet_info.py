#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_subnet_info
short_description: Manage Subnet
description:
    - Manage Subnet
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
        - ID of the Subnet object
    type: str
    returned: Always
results:
    description:
        - Subnet object
    type: list
    elements: dict
    returned: Always
    contains:
        address:
            description: >
                The address of the subnet in the form "a.b.c.d/n" where the "/n" may be omitted. In this case, the CIDR value must be defined in the I(cidr) field. When reading, the I(address) field is always in the form "a.b.c.d".
            type: str
            returned: Always
        asm_config:
            description: >
                The Automated Scope Management configuration for the subnet.
            type: dict
            returned: Always
            contains:
                asm_threshold:
                    description: >
                        ASM shows the number of addresses forecast to be used I(forecast)periodI( days in the future, if it is greater than )asmI(threshold) percent * I(dhcp)totalI( (see )dhcpI(utilization)) then the subnet is flagged.
                    type: int
                    returned: Always
                enable:
                    description: >
                        Indicates if Automated Scope Management is enabled.
                    type: bool
                    returned: Always
                enable_notification:
                    description: >
                        Indicates if ASM should send notifications to the user.
                    type: bool
                    returned: Always
                forecast_period:
                    description: >
                        The forecast period in days.
                    type: int
                    returned: Always
                growth_factor:
                    description: >
                        Indicates the growth in the number or percentage of IP addresses.
                    type: int
                    returned: Always
                growth_type:
                    description: >
                        The type of factor to use: I(percent) or I(count).
                    type: str
                    returned: Always
                history:
                    description: >
                        The minimum amount of history needed before ASM can run on this subnet.
                    type: int
                    returned: Always
                min_total:
                    description: >
                        The minimum size of range needed for ASM to run on this subnet.
                    type: int
                    returned: Always
                min_unused:
                    description: >
                        The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses
                        when making a suggested change..
                    type: int
                    returned: Always
                reenable_date:
                    description: ""
                    type: str
                    returned: Always
        asm_scope_flag:
            description: >
                Set to 1 to indicate that the subnet may run out of addresses.
            type: int
            returned: Always
        cidr:
            description: >
                The CIDR of the subnet. This is required if I(address) does not include CIDR.
            type: int
            returned: Always
        comment:
            description: >
                The description for the subnet. May contain 0 to 1024 characters. Can include UTF-8.
            type: str
            returned: Always
        created_at:
            description: >
                Time when the object has been created.
            type: str
            returned: Always
        ddns_client_update:
            description: >
                Controls who does the DDNS updates.
                
                Valid values are:
                * I(client): DHCP server updates DNS if requested by client.
                * I(server): DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates.
                * I(ignore): DHCP server always updates DNS, even if the client says not to.
                * I(over)clientI(update): Same as I(server). DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates.
                * I(over)noI(update): DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it.
                
                Defaults to I(client).
            type: str
            returned: Always
        ddns_conflict_resolution_mode:
            description: >
                The mode used for resolving conflicts while performing DDNS updates.
                
                Valid values are:
                * I(check)withI(dhcid): It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703.
                * I(no)checkI(with)dhcid_: This will ignore conflict detection but add a DHCID record when creating/updating an entry.
                * I(check)existsI(with)dhcid_: This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry.
                * I(no)checkI(without)dhcid_: This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry.
                
                Defaults to I(check)withI(dhcid).
            type: str
            returned: Always
        ddns_domain:
            description: >
                The domain suffix for DDNS updates. FQDN, may be empty.
                
                Defaults to empty.
            type: str
            returned: Always
        ddns_generate_name:
            description: >
                Indicates if DDNS needs to generate a hostname when not supplied by the client.
                
                Defaults to I(false).
            type: bool
            returned: Always
        ddns_generated_prefix:
            description: >
                The prefix used in the generation of an FQDN.
                
                When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix].
                where address-text is simply the lease IP address converted to a hyphenated string.
                
                Defaults to "myhost".
            type: str
            returned: Always
        ddns_send_updates:
            description: >
                Determines if DDNS updates are enabled at the subnet level.
                Defaults to I(true).
            type: bool
            returned: Always
        ddns_ttl_percent:
            description: >
                DDNS TTL value - to be calculated as a simple percentage of the lease's lifetime, using the parameter's value as the percentage.
                It is specified as a percentage (e.g. 25, 75).
                Defaults to unspecified.
            type: float
            returned: Always
        ddns_update_on_renew:
            description: >
                Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed.
                
                Defaults to I(false).
            type: bool
            returned: Always
        ddns_use_conflict_resolution:
            description: >
                When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request.
                
                When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients.
                
                Defaults to I(true).
            type: bool
            returned: Always
        dhcp_config:
            description: >
                The DHCP configuration of the subnet that controls how leases are issued.
            type: dict
            returned: Always
            contains:
                abandoned_reclaim_time:
                    description: >
                        The abandoned reclaim time in seconds for IPV4 clients.
                    type: int
                    returned: Always
                abandoned_reclaim_time_v6:
                    description: >
                        The abandoned reclaim time in seconds for IPV6 clients.
                    type: int
                    returned: Always
                allow_unknown:
                    description: >
                        Disable to allow leases only for known IPv4 clients, those for which a fixed address is configured.
                    type: bool
                    returned: Always
                allow_unknown_v6:
                    description: >
                        Disable to allow leases only for known IPV6 clients, those for which a fixed address is configured.
                    type: bool
                    returned: Always
                echo_client_id:
                    description: >
                        Enable/disable to include/exclude the client id when responding to discover or request.
                    type: bool
                    returned: Always
                filters:
                    description: >
                        The resource identifier.
                    type: list
                    returned: Always
                filters_v6:
                    description: >
                        The resource identifier.
                    type: list
                    returned: Always
                ignore_client_uid:
                    description: >
                        Enable to ignore the client UID when issuing a DHCP lease. Use this option to prevent assigning two IP addresses for a client which does not have a UID during one phase of PXE boot but acquires one for the other phase.
                    type: bool
                    returned: Always
                ignore_list:
                    description: >
                        The list of clients to ignore requests from.
                    type: list
                    returned: Always
                    elements: dict
                    contains:
                        type:
                            description: >
                                Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:
                                * I(client)hex_,
                                * I(client)text_,
                                * I(hardware).
                            type: str
                            returned: Always
                        value:
                            description: >
                                Value to match.
                            type: str
                            returned: Always
                lease_time:
                    description: >
                        The lease duration in seconds.
                    type: int
                    returned: Always
                lease_time_v6:
                    description: >
                        The lease duration in seconds for IPV6 clients.
                    type: int
                    returned: Always
        dhcp_host:
            description: >
                The resource identifier.
            type: str
            returned: Always
        dhcp_options:
            description: >
                The DHCP options of the subnet. This can either be a specific option or a group of options.
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
        dhcp_utilization:
            description: >
                The utilization of IP addresses within the DHCP ranges of the subnet.
            type: dict
            returned: Always
            contains:
                dhcp_free:
                    description: >
                        The total free IP addresses in the DHCP ranges in the scope of this object. It can be computed as I(dhcp)totalI( - )dhcpI(used).
                    type: str
                    returned: Always
                dhcp_total:
                    description: >
                        The total IP addresses available in the DHCP ranges in the scope of this object.
                    type: str
                    returned: Always
                dhcp_used:
                    description: >
                        The total IP addresses marked as used in the DHCP ranges in the scope of this object.
                    type: str
                    returned: Always
                dhcp_utilization:
                    description: >
                        The percentage of used IP addresses relative to the total IP addresses available in the DHCP ranges in the scope of this object.
                    type: int
                    returned: Always
        disable_dhcp:
            description: >
                Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration.
                
                Defaults to I(false).
            type: bool
            returned: Always
        discovery_attrs:
            description: >
                The discovery attributes for this subnet in JSON format.
            type: dict
            returned: Always
        discovery_metadata:
            description: >
                The discovery metadata for this subnet in JSON format.
            type: dict
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
        hostname_rewrite_char:
            description: >
                The character to replace non-matching characters with, when hostname rewrite is enabled.
                
                Any single ASCII character or no character if the invalid characters should be removed without replacement.
                
                Defaults to "-".
            type: str
            returned: Always
        hostname_rewrite_enabled:
            description: >
                Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match I(hostname)rewriteI(regex) by I(hostname)rewriteI(char).
                
                Defaults to I(false).
            type: bool
            returned: Always
        hostname_rewrite_regex:
            description: >
                The regex bracket expression to match valid characters.
                
                Must begin with "[" and end with "]" and be a compilable POSIX regex.
                
                Defaults to "[^a-zA-Z0-9_.]".
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
                The DHCP inheritance configuration for the subnet.
            type: dict
            returned: Always
            contains:
                asm_config:
                    description: >
                        The inheritance configuration for I(asm)config_ field.
                    type: dict
                    returned: Always
                    contains:
                        asm_enable_block:
                            description: >
                                The block of ASM fields: I(enable), I(enable)notificationI(, )reenableI(date).
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
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
                                    type: dict
                                    returned: Always
                                    contains:
                                        enable:
                                            description: >
                                                Indicates whether Automated Scope Management is enabled or not.
                                            type: bool
                                            returned: Always
                                        enable_notification:
                                            description: >
                                                Indicates whether sending notifications to the users is enabled or not.
                                            type: bool
                                            returned: Always
                                        reenable_date:
                                            description: >
                                                The date at which notifications will be re-enabled automatically.
                                            type: str
                                            returned: Always
                        asm_growth_block:
                            description: >
                                The block of ASM fields: I(growth)factorI(, )growthI(type).
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
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
                                    type: dict
                                    returned: Always
                                    contains:
                                        growth_factor:
                                            description: >
                                                Either the number or percentage of addresses to grow by.
                                            type: int
                                            returned: Always
                                        growth_type:
                                            description: >
                                                The type of factor to use: I(percent) or I(count).
                                            type: str
                                            returned: Always
                        asm_threshold:
                            description: >
                                ASM shows the number of addresses forecast to be used I(forecast)periodI( days in the future, if it is greater than )asmI(threshold)percentI( * )dhcpI(total) (see I(dhcp)utilization_) then the subnet is flagged.
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
                                    type: int
                                    returned: Always
                        forecast_period:
                            description: >
                                The forecast period in days.
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
                                    type: int
                                    returned: Always
                        history:
                            description: >
                                The minimum amount of history needed before ASM can run on this subnet.
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
                                    type: int
                                    returned: Always
                        min_total:
                            description: >
                                The minimum size of range needed for ASM to run on this subnet.
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
                                    type: int
                                    returned: Always
                        min_unused:
                            description: >
                                The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change.
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
                                    type: int
                                    returned: Always
                ddns_client_update:
                    description: >
                        The inheritance configuration for I(ddns)clientI(update) field.
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
                ddns_conflict_resolution_mode:
                    description: >
                        The inheritance configuration for I(ddns)conflictI(resolution)mode_ field.
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
                ddns_enabled:
                    description: >
                        The inheritance configuration for I(ddns)enabled_ field. Only action allowed is 'inherit'.
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
                            type: bool
                            returned: Always
                ddns_hostname_block:
                    description: >
                        The inheritance configuration for I(ddns)generateI(name) and I(ddns)generatedI(prefix) fields.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting.
                                
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
                            type: dict
                            returned: Always
                            contains:
                                ddns_generate_name:
                                    description: >
                                        Indicates if DDNS should generate a hostname when not supplied by the client.
                                    type: bool
                                    returned: Always
                                ddns_generated_prefix:
                                    description: >
                                        The prefix used in the generation of an FQDN.
                                    type: str
                                    returned: Always
                ddns_ttl_percent:
                    description: >
                        The inheritance configuration for I(ddns)ttlI(percent) field.
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
                            type: float
                            returned: Always
                ddns_update_block:
                    description: >
                        The inheritance configuration for I(ddns)sendI(updates) and I(ddns)domain_ fields.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting.
                                
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
                            type: dict
                            returned: Always
                            contains:
                                ddns_domain:
                                    description: >
                                        The domain name for DDNS.
                                    type: str
                                    returned: Always
                                ddns_send_updates:
                                    description: >
                                        Determines if DDNS updates are enabled at this level.
                                    type: bool
                                    returned: Always
                ddns_update_on_renew:
                    description: >
                        The inheritance configuration for I(ddns)updateI(on)renew_ field.
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
                            type: bool
                            returned: Always
                ddns_use_conflict_resolution:
                    description: >
                        The inheritance configuration for I(ddns)useI(conflict)resolution_ field.
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
                            type: bool
                            returned: Always
                dhcp_config:
                    description: >
                        The inheritance configuration for I(dhcp)config_ field.
                    type: dict
                    returned: Always
                    contains:
                        abandoned_reclaim_time:
                            description: >
                                The inheritance configuration for I(abandoned)reclaimI(time) field from I(DHCPConfig) object.
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
                                    type: int
                                    returned: Always
                        abandoned_reclaim_time_v6:
                            description: >
                                The inheritance configuration for I(abandoned)reclaimI(time)v6I( field from )DHCPConfig_ object.
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
                                    type: int
                                    returned: Always
                        allow_unknown:
                            description: >
                                The inheritance configuration for I(allow)unknownI( field from )DHCPConfig_ object.
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
                                    type: bool
                                    returned: Always
                        allow_unknown_v6:
                            description: >
                                The inheritance configuration for I(allow)unknownI(v6) field from I(DHCPConfig) object.
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
                                    type: bool
                                    returned: Always
                        echo_client_id:
                            description: >
                                The inheritance configuration for I(echo)clientI(id) field from I(DHCPConfig) object.
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
                                    type: bool
                                    returned: Always
                        filters:
                            description: >
                                The inheritance configuration for filters field from I(DHCPConfig) object.
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
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
                                        The resource identifier.
                                    type: list
                                    returned: Always
                        filters_v6:
                            description: >
                                The inheritance configuration for I(filters)v6I( field from )DHCPConfig_ object.
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
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
                                        The resource identifier.
                                    type: list
                                    returned: Always
                        ignore_client_uid:
                            description: >
                                The inheritance configuration for I(ignore)clientI(uid) field from I(DHCPConfig) object.
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
                                    type: bool
                                    returned: Always
                        ignore_list:
                            description: >
                                The inheritance configuration for I(ignore)listI( field from )DHCPConfig_ object.
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description: >
                                        The inheritance setting.
                                        
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
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        type:
                                            description: >
                                                Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:
                                                * I(client)hex_,
                                                * I(client)text_,
                                                * I(hardware).
                                            type: str
                                            returned: Always
                                        value:
                                            description: >
                                                Value to match.
                                            type: str
                                            returned: Always
                        lease_time:
                            description: >
                                The inheritance configuration for I(lease)timeI( field from )DHCPConfig_ object.
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
                                    type: int
                                    returned: Always
                        lease_time_v6:
                            description: >
                                The inheritance configuration for I(lease)timeI(v6) field from I(DHCPConfig) object.
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
                                    type: int
                                    returned: Always
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
                hostname_rewrite_block:
                    description: >
                        The inheritance configuration for I(hostname)rewriteI(enabled), I(hostname)rewriteI(regex), and I(hostname)rewriteI(char) fields.
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description: >
                                The inheritance setting.
                                
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
                            type: dict
                            returned: Always
                            contains:
                                hostname_rewrite_char:
                                    description: >
                                        The inheritance configuration for I(hostname)rewriteI(char) field.
                                    type: str
                                    returned: Always
                                hostname_rewrite_enabled:
                                    description: >
                                        The inheritance configuration for I(hostname)rewriteI(enabled) field.
                                    type: bool
                                    returned: Always
                                hostname_rewrite_regex:
                                    description: >
                                        The inheritance configuration for I(hostname)rewriteI(regex) field.
                                    type: str
                                    returned: Always
        name:
            description: >
                The name of the subnet. May contain 1 to 256 characters. Can include UTF-8.
            type: str
            returned: Always
        parent:
            description: >
                The resource identifier.
            type: str
            returned: Always
        protocol:
            description: >
                The type of protocol of the subnet (I(ip4) or I(ip6)).
            type: str
            returned: Always
        rebind_time:
            description: >
                The lease rebind time (T2) in seconds.
            type: int
            returned: Always
        renew_time:
            description: >
                The lease renew time (T1) in seconds.
            type: int
            returned: Always
        space:
            description: >
                The resource identifier.
            type: str
            returned: Always
        tags:
            description: >
                The tags for the subnet in JSON format.
            type: dict
            returned: Always
        threshold:
            description: >
                The IP address utilization threshold settings for the subnet.
            type: dict
            returned: Always
            contains:
                enabled:
                    description: >
                        Indicates whether the utilization threshold for IP addresses is enabled or not.
                    type: bool
                    returned: Always
                high:
                    description: >
                        The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test.
                    type: int
                    returned: Always
                low:
                    description: >
                        The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test.
                    type: int
                    returned: Always
        updated_at:
            description: >
                Time when the object has been updated. Equals to I(created)at_ if not updated after creation.
            type: str
            returned: Always
        usage:
            description: >
                The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:
                usage indicator        | description
                ---------------------- | --------------------------------
                I(IPAM)                 |  Subnet is managed in BloxOne DDI.
                I(DHCP)                 |  Subnet is served by a DHCP Host.
                I(DISCOVERED)           |  Subnet is discovered by some network discovery probe like Network Insight or NetMRI in NIOS.
            type: list
            returned: Always
        utilization:
            description: >
                The IPV4 address utilization statistics of the subnet.
            type: dict
            returned: Always
            contains:
                abandon_utilization:
                    description: >
                        The percentage of abandoned IP addresses relative to the total IP addresses available in the scope of the object.
                    type: int
                    returned: Always
                abandoned:
                    description: >
                        The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client).
                    type: str
                    returned: Always
                dynamic:
                    description: >
                        The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases.
                    type: str
                    returned: Always
                free:
                    description: >
                        The number of IP addresses available in the scope of the object.
                    type: str
                    returned: Always
                static:
                    description: >
                        The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) = I(used) - I(dynamic).
                    type: str
                    returned: Always
                total:
                    description: >
                        The total number of IP addresses available in the scope of the object.
                    type: str
                    returned: Always
                used:
                    description: >
                        The number of IP addresses used in the scope of the object.
                    type: str
                    returned: Always
                utilization:
                    description: >
                        The percentage of used IP addresses relative to the total IP addresses available in the scope of the object.
                    type: int
                    returned: Always
        utilization_v6:
            description: >
                The utilization of IPV6 addresses in the subnet.
            type: dict
            returned: Always
            contains:
                abandoned:
                    description: ""
                    type: str
                    returned: Always
                dynamic:
                    description: ""
                    type: str
                    returned: Always
                static:
                    description: ""
                    type: str
                    returned: Always
                total:
                    description: ""
                    type: str
                    returned: Always
                used:
                    description: ""
                    type: str
                    returned: Always
"""  # noqa: E501

import traceback

from ansible_collections.infoblox.bloxone.plugins.module_utils.bloxone import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from ipam import SubnetApi
except ImportError:
    HAS_BLOXONE_CLIENT = False
    HAS_BLOXONE_CLIENT_IMP_ERR = traceback.format_exc()
else:
    HAS_BLOXONE_CLIENT = True
    HAS_BLOXONE_CLIENT_IMP_ERR = None


def find(module):
    if module.params['id'] is not None:
        try:
            resp = SubnetApi(module.client).read(module.params['id'], inherit="full")
            return [resp.result]
        except NotFoundException as e:
            return None
    else:
        filter = None
        if module.params['filters'] is not None:
            filter = " and ".join(["{0}=='{1}'".format(k, v) for k, v in module.params['filters'].items()])
        elif module.params['filter_query'] is not None:
            filter = module.params['filter_query']

        resp = SubnetApi(module.client).list(filter=filter, inherit="full")
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
