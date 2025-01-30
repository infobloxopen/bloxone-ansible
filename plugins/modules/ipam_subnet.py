#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_subnet
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
        description:
            - "The address of the subnet in the form \"a.b.c.d/n\" where the \"/n\" may be omitted. In this case, the CIDR value must be defined in the I(cidr) field. When reading, the I(address) field is always in the form \"a.b.c.d\"."
        type: str
    asm_config:
        description:
            - "The Automated Scope Management configuration for the subnet."
        type: dict
        suboptions:
            asm_threshold:
                description:
                    - "ASM shows the number of addresses forecast to be used I(forecast_period) days in the future, if it is greater than I(asm_threshold) percent * I(dhcp_total) (see I(dhcp_utilization)) then the subnet is flagged."
                type: int
            enable:
                description:
                    - "Indicates if Automated Scope Management is enabled."
                type: bool
            enable_notification:
                description:
                    - "Indicates if ASM should send notifications to the user."
                type: bool
            forecast_period:
                description:
                    - "The forecast period in days."
                type: int
            growth_factor:
                description:
                    - "Indicates the growth in the number or percentage of IP addresses."
                type: int
            growth_type:
                description:
                    - "The type of factor to use: I(percent) or I(count)."
                type: str
            history:
                description:
                    - "The minimum amount of history needed before ASM can run on this subnet."
                type: int
            min_total:
                description:
                    - "The minimum size of range needed for ASM to run on this subnet."
                type: int
            min_unused:
                description:
                    - "The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change.."
                type: int
            reenable_date:
                description: ""
                type: str
    cidr:
        description:
            - "The CIDR of the subnet. This is required if I(address) does not include CIDR."
        type: int
    comment:
        description:
            - "The description for the subnet. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    ddns_client_update:
        description:
            - "Controls who does the DDNS updates."
            - "Valid values are:"
            - "* I(client): DHCP server updates DNS if requested by client."
            - "* I(server): DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates."
            - "* I(ignore): DHCP server always updates DNS, even if the client says not to."
            - "* I(over_client_update): Same as I(server). DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates."
            - "* I(over_no_update): DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it."
            - "Defaults to I(client)."
        type: str
    ddns_conflict_resolution_mode:
        description:
            - "The mode used for resolving conflicts while performing DDNS updates."
            - "Valid values are:"
            - "* I(check_with_dhcid): It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703."
            - "* I(no_check_with_dhcid): This will ignore conflict detection but add a DHCID record when creating/updating an entry."
            - "* I(check_exists_with_dhcid): This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry."
            - "* I(no_check_without_dhcid): This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry."
            - "Defaults to I(check_with_dhcid)."
        type: str
    ddns_domain:
        description:
            - "The domain suffix for DDNS updates. FQDN, may be empty."
            - "Defaults to empty."
        type: str
    ddns_generate_name:
        description:
            - "Indicates if DDNS needs to generate a hostname when not supplied by the client."
            - "Defaults to I(false)."
        type: bool
    ddns_generated_prefix:
        description:
            - "The prefix used in the generation of an FQDN."
            - "When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string."
            - "Defaults to \"myhost\"."
        type: str
    ddns_send_updates:
        description:
            - "Determines if DDNS updates are enabled at the subnet level. Defaults to I(true)."
        type: bool
    ddns_ttl_percent:
        description:
            - "DDNS TTL value - to be calculated as a simple percentage of the lease's lifetime, using the parameter's value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified."
        type: float
    ddns_update_on_renew:
        description:
            - "Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed."
            - "Defaults to I(false)."
        type: bool
    ddns_use_conflict_resolution:
        description:
            - "When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request."
            - "When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients."
            - "Defaults to I(true)."
        type: bool
    dhcp_config:
        description:
            - "The DHCP configuration of the subnet that controls how leases are issued."
        type: dict
        suboptions:
            allow_unknown:
                description:
                    - "Disable to allow leases only for known IPv4 clients, those for which a fixed address is configured."
                type: bool
            allow_unknown_v6:
                description:
                    - "Disable to allow leases only for known IPV6 clients, those for which a fixed address is configured."
                type: bool
            filters:
                description:
                    - "The resource identifier."
                type: list
                elements: str
            filters_v6:
                description:
                    - "The resource identifier."
                type: list
                elements: str
            ignore_client_uid:
                description:
                    - "Enable to ignore the client UID when issuing a DHCP lease. Use this option to prevent assigning two IP addresses for a client which does not have a UID during one phase of PXE boot but acquires one for the other phase."
                type: bool
            ignore_list:
                description:
                    - "The list of clients to ignore requests from."
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - "Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:"
                            - "* I(client_hex),"
                            - "* I(client_text),"
                            - "* I(hardware)."
                        type: str
                    value:
                        description:
                            - "Value to match."
                        type: str
            lease_time:
                description:
                    - "The lease duration in seconds."
                type: int
            lease_time_v6:
                description:
                    - "The lease duration in seconds for IPV6 clients."
                type: int
    dhcp_host:
        description:
            - "The resource identifier."
        type: str
    dhcp_options:
        description:
            - "The DHCP options of the subnet. This can either be a specific option or a group of options."
        type: list
        elements: dict
        suboptions:
            group:
                description:
                    - "The resource identifier."
                type: str
            option_code:
                description:
                    - "The resource identifier."
                type: str
            option_value:
                description:
                    - "The option value."
                type: str
            type:
                description:
                    - "The type of item."
                    - "Valid values are:"
                    - "* I(group)"
                    - "* I(option)"
                type: str
    disable_dhcp:
        description:
            - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
            - "Defaults to I(false)."
        type: bool
    header_option_filename:
        description:
            - "The configuration for header option filename field."
        type: str
    header_option_server_address:
        description:
            - "The configuration for header option server address field."
        type: str
    header_option_server_name:
        description:
            - "The configuration for header option server name field."
        type: str
    hostname_rewrite_char:
        description:
            - "The character to replace non-matching characters with, when hostname rewrite is enabled."
            - "Any single ASCII character or no character if the invalid characters should be removed without replacement."
            - "Defaults to \"-\"."
        type: str
    hostname_rewrite_enabled:
        description:
            - "Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match I(hostname_rewrite_regex) by I(hostname_rewrite_char)."
            - "Defaults to I(false)."
        type: bool
    hostname_rewrite_regex:
        description:
            - "The regex bracket expression to match valid characters."
            - "Must begin with \"[\" and end with \"]\" and be a compilable POSIX regex."
            - "Defaults to \"[^a-zA-Z0-9_.]\"."
        type: str
    inheritance_parent:
        description:
            - "The resource identifier."
        type: str
    inheritance_sources:
        description:
            - "The DHCP inheritance configuration for the subnet."
        type: dict
        suboptions:
            asm_config:
                description:
                    - "The inheritance configuration for I(asm_config) field."
                type: dict
                suboptions:
                    asm_enable_block:
                        description:
                            - "The block of ASM fields: I(enable), I(enable_notification), I(reenable_date)."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    asm_growth_block:
                        description:
                            - "The block of ASM fields: I(growth_factor), I(growth_type)."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    asm_threshold:
                        description:
                            - "ASM shows the number of addresses forecast to be used I(forecast_period) days in the future, if it is greater than I(asm_threshold_percent) * I(dhcp_total) (see I(dhcp_utilization)) then the subnet is flagged."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    forecast_period:
                        description:
                            - "The forecast period in days."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    history:
                        description:
                            - "The minimum amount of history needed before ASM can run on this subnet."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    min_total:
                        description:
                            - "The minimum size of range needed for ASM to run on this subnet."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    min_unused:
                        description:
                            - "The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
            ddns_client_update:
                description:
                    - "The inheritance configuration for I(ddns_client_update) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_conflict_resolution_mode:
                description:
                    - "The inheritance configuration for I(ddns_conflict_resolution_mode) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_enabled:
                description:
                    - "The inheritance configuration for I(ddns_enabled) field. Only action allowed is 'inherit'."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_hostname_block:
                description:
                    - "The inheritance configuration for I(ddns_generate_name) and I(ddns_generated_prefix) fields."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_ttl_percent:
                description:
                    - "The inheritance configuration for I(ddns_ttl_percent) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_update_block:
                description:
                    - "The inheritance configuration for I(ddns_send_updates) and I(ddns_domain) fields."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_update_on_renew:
                description:
                    - "The inheritance configuration for I(ddns_update_on_renew) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            ddns_use_conflict_resolution:
                description:
                    - "The inheritance configuration for I(ddns_use_conflict_resolution) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            dhcp_config:
                description:
                    - "The inheritance configuration for I(dhcp_config) field."
                type: dict
                suboptions:
                    abandoned_reclaim_time:
                        description:
                            - "The inheritance configuration for I(abandoned_reclaim_time) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    abandoned_reclaim_time_v6:
                        description:
                            - "The inheritance configuration for I(abandoned_reclaim_time_v6) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    allow_unknown:
                        description:
                            - "The inheritance configuration for I(allow_unknown) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    allow_unknown_v6:
                        description:
                            - "The inheritance configuration for I(allow_unknown_v6) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    echo_client_id:
                        description:
                            - "The inheritance configuration for I(echo_client_id) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    filters:
                        description:
                            - "The inheritance configuration for filters field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                            value:
                                description:
                                    - "The resource identifier."
                                type: list
                                elements: str
                    filters_v6:
                        description:
                            - "The inheritance configuration for I(filters_v6) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                            value:
                                description:
                                    - "The resource identifier."
                                type: list
                                elements: str
                    ignore_client_uid:
                        description:
                            - "The inheritance configuration for I(ignore_client_uid) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    ignore_list:
                        description:
                            - "The inheritance configuration for I(ignore_list) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    lease_time:
                        description:
                            - "The inheritance configuration for I(lease_time) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
                    lease_time_v6:
                        description:
                            - "The inheritance configuration for I(lease_time_v6) field from I(DHCPConfig) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting for a field."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(override): Use the value set in the object."
                                    - "Defaults to I(inherit)."
                                type: str
            dhcp_options:
                description:
                    - "The inheritance configuration for I(dhcp_options) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(block): Don't use the inherited value."
                            - "Defaults to I(inherit)."
                        type: str
                    value:
                        description:
                            - "The inherited DHCP option values."
                        type: list
                        elements: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(block): Don't use the inherited value."
                                    - "Defaults to I(inherit)."
                                type: str
            header_option_filename:
                description:
                    - "The inheritance configuration for I(header_option_filename) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            header_option_server_address:
                description:
                    - "The inheritance configuration for I(header_option_server_address) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            header_option_server_name:
                description:
                    - "The inheritance configuration for I(header_option_server_name) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting for a field."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
            hostname_rewrite_block:
                description:
                    - "The inheritance configuration for I(hostname_rewrite_enabled), I(hostname_rewrite_regex), and I(hostname_rewrite_char) fields."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(override): Use the value set in the object."
                            - "Defaults to I(inherit)."
                        type: str
    name:
        description:
            - "The name of the subnet. May contain 1 to 256 characters. Can include UTF-8."
        type: str
    parent:
        description:
            - "The resource identifier."
        type: str
    rebind_time:
        description:
            - "The lease rebind time (T2) in seconds."
        type: int
    renew_time:
        description:
            - "The lease renew time (T1) in seconds."
        type: int
    space:
        description:
            - "The resource identifier."
        type: str
    tags:
        description:
            - "The tags for the subnet in JSON format."
        type: dict
    threshold:
        description:
            - "The IP address utilization threshold settings for the subnet."
        type: dict
        suboptions:
            enabled:
                description:
                    - "Indicates whether the utilization threshold for IP addresses is enabled or not."
                type: bool
            high:
                description:
                    - "The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                type: int
            low:
                description:
                    - "The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                type: int

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: "Create an ip space"
      infoblox.bloxone.ipam_ip_space:
        name: "my-ip-space"
        state: "present"
      register: ip_space

    - name: "Create a subnet"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0/24"
        space: "{{ ip_space.id }}"
        state: "present"

    - name: "Create a subnet with dhcp_config overridden"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0/24"
        space: "{{ ip_space_id }}"
        state: "present"
        dhcp_config:
            abandoned_reclaim_time: 3600
        inheritance_sources:
            dhcp_config:
                lease_time:
                    action: override

                # The API currently requires all fields inside the inheritance config to be explicitly provided,
                # or it fails with error 'The value of an inheritance action field is not valid'.
                abandoned_reclaim_time:
                    action: inherit
                abandoned_reclaim_time_v6:
                    action: inherit
                allow_unknown:
                      action: inherit
                allow_unknown_v6:
                    action: inherit
                echo_client_id:
                    action: inherit
                filters:
                    action: inherit
                filters_v6:
                    action: inherit
                ignore_client_uid:
                    action: inherit
                ignore_list:
                    action: inherit
                lease_time_v6:
                    action: inherit

    - name: "Delete a subnet"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0"
        cidr: "24"
        space: "{{ ip_space.id }}"
        state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the Subnet object
    type: str
    returned: Always
item:
    description:
        - Subnet object
    type: complex
    returned: Always
    contains:
        address:
            description:
                - "The address of the subnet in the form \"a.b.c.d/n\" where the \"/n\" may be omitted. In this case, the CIDR value must be defined in the I(cidr) field. When reading, the I(address) field is always in the form \"a.b.c.d\"."
            type: str
            returned: Always
        asm_config:
            description:
                - "The Automated Scope Management configuration for the subnet."
            type: dict
            returned: Always
            contains:
                asm_threshold:
                    description:
                        - "ASM shows the number of addresses forecast to be used I(forecast_period) days in the future, if it is greater than I(asm_threshold) percent * I(dhcp_total) (see I(dhcp_utilization)) then the subnet is flagged."
                    type: int
                    returned: Always
                enable:
                    description:
                        - "Indicates if Automated Scope Management is enabled."
                    type: bool
                    returned: Always
                enable_notification:
                    description:
                        - "Indicates if ASM should send notifications to the user."
                    type: bool
                    returned: Always
                forecast_period:
                    description:
                        - "The forecast period in days."
                    type: int
                    returned: Always
                growth_factor:
                    description:
                        - "Indicates the growth in the number or percentage of IP addresses."
                    type: int
                    returned: Always
                growth_type:
                    description:
                        - "The type of factor to use: I(percent) or I(count)."
                    type: str
                    returned: Always
                history:
                    description:
                        - "The minimum amount of history needed before ASM can run on this subnet."
                    type: int
                    returned: Always
                min_total:
                    description:
                        - "The minimum size of range needed for ASM to run on this subnet."
                    type: int
                    returned: Always
                min_unused:
                    description:
                        - "The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change.."
                    type: int
                    returned: Always
                reenable_date:
                    description: ""
                    type: str
                    returned: Always
        asm_scope_flag:
            description:
                - "Set to 1 to indicate that the subnet may run out of addresses."
            type: int
            returned: Always
        cidr:
            description:
                - "The CIDR of the subnet. This is required if I(address) does not include CIDR."
            type: int
            returned: Always
        comment:
            description:
                - "The description for the subnet. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        ddns_client_update:
            description:
                - "Controls who does the DDNS updates."
                - "Valid values are:"
                - "* I(client): DHCP server updates DNS if requested by client."
                - "* I(server): DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates."
                - "* I(ignore): DHCP server always updates DNS, even if the client says not to."
                - "* I(over_client_update): Same as I(server). DHCP server always updates DNS, overriding an update request from the client, unless the client requests no updates."
                - "* I(over_no_update): DHCP server updates DNS even if the client requests that no updates be done. If the client requests to do the update, DHCP server allows it."
                - "Defaults to I(client)."
            type: str
            returned: Always
        ddns_conflict_resolution_mode:
            description:
                - "The mode used for resolving conflicts while performing DDNS updates."
                - "Valid values are:"
                - "* I(check_with_dhcid): It includes adding a DHCID record and checking that record via conflict detection as per RFC 4703."
                - "* I(no_check_with_dhcid): This will ignore conflict detection but add a DHCID record when creating/updating an entry."
                - "* I(check_exists_with_dhcid): This will check if there is an existing DHCID record but does not verify the value of the record matches the update. This will also update the DHCID record for the entry."
                - "* I(no_check_without_dhcid): This ignores conflict detection and will not add a DHCID record when creating/updating a DDNS entry."
                - "Defaults to I(check_with_dhcid)."
            type: str
            returned: Always
        ddns_domain:
            description:
                - "The domain suffix for DDNS updates. FQDN, may be empty."
                - "Defaults to empty."
            type: str
            returned: Always
        ddns_generate_name:
            description:
                - "Indicates if DDNS needs to generate a hostname when not supplied by the client."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        ddns_generated_prefix:
            description:
                - "The prefix used in the generation of an FQDN."
                - "When generating a name, DHCP server will construct the name in the format: [ddns-generated-prefix]-[address-text].[ddns-qualifying-suffix]. where address-text is simply the lease IP address converted to a hyphenated string."
                - "Defaults to \"myhost\"."
            type: str
            returned: Always
        ddns_send_updates:
            description:
                - "Determines if DDNS updates are enabled at the subnet level. Defaults to I(true)."
            type: bool
            returned: Always
        ddns_ttl_percent:
            description:
                - "DDNS TTL value - to be calculated as a simple percentage of the lease's lifetime, using the parameter's value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified."
            type: float
            returned: Always
        ddns_update_on_renew:
            description:
                - "Instructs the DHCP server to always update the DNS information when a lease is renewed even if its DNS information has not changed."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        ddns_use_conflict_resolution:
            description:
                - "When true, DHCP server will apply conflict resolution, as described in RFC 4703, when attempting to fulfill the update request."
                - "When false, DHCP server will simply attempt to update the DNS entries per the request, regardless of whether or not they conflict with existing entries owned by other DHCP4 clients."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        dhcp_config:
            description:
                - "The DHCP configuration of the subnet that controls how leases are issued."
            type: dict
            returned: Always
            contains:
                allow_unknown:
                    description:
                        - "Disable to allow leases only for known IPv4 clients, those for which a fixed address is configured."
                    type: bool
                    returned: Always
                allow_unknown_v6:
                    description:
                        - "Disable to allow leases only for known IPV6 clients, those for which a fixed address is configured."
                    type: bool
                    returned: Always
                filters:
                    description:
                        - "The resource identifier."
                    type: list
                    returned: Always
                filters_v6:
                    description:
                        - "The resource identifier."
                    type: list
                    returned: Always
                ignore_client_uid:
                    description:
                        - "Enable to ignore the client UID when issuing a DHCP lease. Use this option to prevent assigning two IP addresses for a client which does not have a UID during one phase of PXE boot but acquires one for the other phase."
                    type: bool
                    returned: Always
                ignore_list:
                    description:
                        - "The list of clients to ignore requests from."
                    type: list
                    returned: Always
                    elements: dict
                    contains:
                        type:
                            description:
                                - "Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:"
                                - "* I(client_hex),"
                                - "* I(client_text),"
                                - "* I(hardware)."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Value to match."
                            type: str
                            returned: Always
                lease_time:
                    description:
                        - "The lease duration in seconds."
                    type: int
                    returned: Always
                lease_time_v6:
                    description:
                        - "The lease duration in seconds for IPV6 clients."
                    type: int
                    returned: Always
        dhcp_host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        dhcp_options:
            description:
                - "The DHCP options of the subnet. This can either be a specific option or a group of options."
            type: list
            returned: Always
            elements: dict
            contains:
                group:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_code:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_value:
                    description:
                        - "The option value."
                    type: str
                    returned: Always
                type:
                    description:
                        - "The type of item."
                        - "Valid values are:"
                        - "* I(group)"
                        - "* I(option)"
                    type: str
                    returned: Always
        dhcp_utilization:
            description:
                - "The utilization of IP addresses within the DHCP ranges of the subnet."
            type: dict
            returned: Always
            contains:
                dhcp_free:
                    description:
                        - "The total free IP addresses in the DHCP ranges in the scope of this object. It can be computed as I(dhcp_total) - I(dhcp_used)."
                    type: str
                    returned: Always
                dhcp_total:
                    description:
                        - "The total IP addresses available in the DHCP ranges in the scope of this object."
                    type: str
                    returned: Always
                dhcp_used:
                    description:
                        - "The total IP addresses marked as used in the DHCP ranges in the scope of this object."
                    type: str
                    returned: Always
                dhcp_utilization:
                    description:
                        - "The percentage of used IP addresses relative to the total IP addresses available in the DHCP ranges in the scope of this object."
                    type: int
                    returned: Always
        disable_dhcp:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        discovery_attrs:
            description:
                - "The discovery attributes for this subnet in JSON format."
            type: dict
            returned: Always
        discovery_metadata:
            description:
                - "The discovery metadata for this subnet in JSON format."
            type: dict
            returned: Always
        header_option_filename:
            description:
                - "The configuration for header option filename field."
            type: str
            returned: Always
        header_option_server_address:
            description:
                - "The configuration for header option server address field."
            type: str
            returned: Always
        header_option_server_name:
            description:
                - "The configuration for header option server name field."
            type: str
            returned: Always
        hostname_rewrite_char:
            description:
                - "The character to replace non-matching characters with, when hostname rewrite is enabled."
                - "Any single ASCII character or no character if the invalid characters should be removed without replacement."
                - "Defaults to \"-\"."
            type: str
            returned: Always
        hostname_rewrite_enabled:
            description:
                - "Indicates if client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match I(hostname_rewrite_regex) by I(hostname_rewrite_char)."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        hostname_rewrite_regex:
            description:
                - "The regex bracket expression to match valid characters."
                - "Must begin with \"[\" and end with \"]\" and be a compilable POSIX regex."
                - "Defaults to \"[^a-zA-Z0-9_.]\"."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_assigned_hosts:
            description:
                - "The list of the inheritance assigned hosts of the object."
            type: list
            returned: Always
            elements: dict
            contains:
                display_name:
                    description:
                        - "The human-readable display name for the host referred to by I(ophid)."
                    type: str
                    returned: Always
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                ophid:
                    description:
                        - "The on-prem host ID."
                    type: str
                    returned: Always
        inheritance_parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The DHCP inheritance configuration for the subnet."
            type: dict
            returned: Always
            contains:
                asm_config:
                    description:
                        - "The inheritance configuration for I(asm_config) field."
                    type: dict
                    returned: Always
                    contains:
                        asm_enable_block:
                            description:
                                - "The block of ASM fields: I(enable), I(enable_notification), I(reenable_date)."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: dict
                                    returned: Always
                                    contains:
                                        enable:
                                            description:
                                                - "Indicates whether Automated Scope Management is enabled or not."
                                            type: bool
                                            returned: Always
                                        enable_notification:
                                            description:
                                                - "Indicates whether sending notifications to the users is enabled or not."
                                            type: bool
                                            returned: Always
                                        reenable_date:
                                            description:
                                                - "The date at which notifications will be re-enabled automatically."
                                            type: str
                                            returned: Always
                        asm_growth_block:
                            description:
                                - "The block of ASM fields: I(growth_factor), I(growth_type)."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: dict
                                    returned: Always
                                    contains:
                                        growth_factor:
                                            description:
                                                - "Either the number or percentage of addresses to grow by."
                                            type: int
                                            returned: Always
                                        growth_type:
                                            description:
                                                - "The type of factor to use: I(percent) or I(count)."
                                            type: str
                                            returned: Always
                        asm_threshold:
                            description:
                                - "ASM shows the number of addresses forecast to be used I(forecast_period) days in the future, if it is greater than I(asm_threshold_percent) * I(dhcp_total) (see I(dhcp_utilization)) then the subnet is flagged."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        forecast_period:
                            description:
                                - "The forecast period in days."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        history:
                            description:
                                - "The minimum amount of history needed before ASM can run on this subnet."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        min_total:
                            description:
                                - "The minimum size of range needed for ASM to run on this subnet."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        min_unused:
                            description:
                                - "The minimum percentage of addresses that must be available outside of the DHCP ranges and fixed addresses when making a suggested change."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                ddns_client_update:
                    description:
                        - "The inheritance configuration for I(ddns_client_update) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: str
                            returned: Always
                ddns_conflict_resolution_mode:
                    description:
                        - "The inheritance configuration for I(ddns_conflict_resolution_mode) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: str
                            returned: Always
                ddns_enabled:
                    description:
                        - "The inheritance configuration for I(ddns_enabled) field. Only action allowed is 'inherit'."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: bool
                            returned: Always
                ddns_hostname_block:
                    description:
                        - "The inheritance configuration for I(ddns_generate_name) and I(ddns_generated_prefix) fields."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: dict
                            returned: Always
                            contains:
                                ddns_generate_name:
                                    description:
                                        - "Indicates if DDNS should generate a hostname when not supplied by the client."
                                    type: bool
                                    returned: Always
                                ddns_generated_prefix:
                                    description:
                                        - "The prefix used in the generation of an FQDN."
                                    type: str
                                    returned: Always
                ddns_ttl_percent:
                    description:
                        - "The inheritance configuration for I(ddns_ttl_percent) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: float
                            returned: Always
                ddns_update_block:
                    description:
                        - "The inheritance configuration for I(ddns_send_updates) and I(ddns_domain) fields."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: dict
                            returned: Always
                            contains:
                                ddns_domain:
                                    description:
                                        - "The domain name for DDNS."
                                    type: str
                                    returned: Always
                                ddns_send_updates:
                                    description:
                                        - "Determines if DDNS updates are enabled at this level."
                                    type: bool
                                    returned: Always
                ddns_update_on_renew:
                    description:
                        - "The inheritance configuration for I(ddns_update_on_renew) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: bool
                            returned: Always
                ddns_use_conflict_resolution:
                    description:
                        - "The inheritance configuration for I(ddns_use_conflict_resolution) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: bool
                            returned: Always
                dhcp_config:
                    description:
                        - "The inheritance configuration for I(dhcp_config) field."
                    type: dict
                    returned: Always
                    contains:
                        abandoned_reclaim_time:
                            description:
                                - "The inheritance configuration for I(abandoned_reclaim_time) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        abandoned_reclaim_time_v6:
                            description:
                                - "The inheritance configuration for I(abandoned_reclaim_time_v6) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        allow_unknown:
                            description:
                                - "The inheritance configuration for I(allow_unknown) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: bool
                                    returned: Always
                        allow_unknown_v6:
                            description:
                                - "The inheritance configuration for I(allow_unknown_v6) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: bool
                                    returned: Always
                        echo_client_id:
                            description:
                                - "The inheritance configuration for I(echo_client_id) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: bool
                                    returned: Always
                        filters:
                            description:
                                - "The inheritance configuration for filters field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The resource identifier."
                                    type: list
                                    returned: Always
                        filters_v6:
                            description:
                                - "The inheritance configuration for I(filters_v6) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The resource identifier."
                                    type: list
                                    returned: Always
                        ignore_client_uid:
                            description:
                                - "The inheritance configuration for I(ignore_client_uid) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: bool
                                    returned: Always
                        ignore_list:
                            description:
                                - "The inheritance configuration for I(ignore_list) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        type:
                                            description:
                                                - "Type of ignore matching: client to ignore by client identifier (client hex or client text) or hardware to ignore by hardware identifier (MAC address). It can have one of the following values:"
                                                - "* I(client_hex),"
                                                - "* I(client_text),"
                                                - "* I(hardware)."
                                            type: str
                                            returned: Always
                                        value:
                                            description:
                                                - "Value to match."
                                            type: str
                                            returned: Always
                        lease_time:
                            description:
                                - "The inheritance configuration for I(lease_time) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                        lease_time_v6:
                            description:
                                - "The inheritance configuration for I(lease_time_v6) field from I(DHCPConfig) object."
                            type: dict
                            returned: Always
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting for a field."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(override): Use the value set in the object."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value."
                                    type: int
                                    returned: Always
                dhcp_options:
                    description:
                        - "The inheritance configuration for I(dhcp_options) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(block): Don't use the inherited value."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited DHCP option values."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(block): Don't use the inherited value."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value for the DHCP option."
                                    type: dict
                                    returned: Always
                                    contains:
                                        option:
                                            description:
                                                - "Option inherited from the ancestor."
                                            type: dict
                                            returned: Always
                                            contains:
                                                group:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_code:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_value:
                                                    description:
                                                        - "The option value."
                                                    type: str
                                                    returned: Always
                                                type:
                                                    description:
                                                        - "The type of item."
                                                        - "Valid values are:"
                                                        - "* I(group)"
                                                        - "* I(option)"
                                                    type: str
                                                    returned: Always
                                        overriding_group:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                header_option_filename:
                    description:
                        - "The inheritance configuration for I(header_option_filename) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: str
                            returned: Always
                header_option_server_address:
                    description:
                        - "The inheritance configuration for I(header_option_server_address) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: str
                            returned: Always
                header_option_server_name:
                    description:
                        - "The inheritance configuration for I(header_option_server_name) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting for a field."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: str
                            returned: Always
                hostname_rewrite_block:
                    description:
                        - "The inheritance configuration for I(hostname_rewrite_enabled), I(hostname_rewrite_regex), and I(hostname_rewrite_char) fields."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(override): Use the value set in the object."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "The human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited value."
                            type: dict
                            returned: Always
                            contains:
                                hostname_rewrite_char:
                                    description:
                                        - "The inheritance configuration for I(hostname_rewrite_char) field."
                                    type: str
                                    returned: Always
                                hostname_rewrite_enabled:
                                    description:
                                        - "The inheritance configuration for I(hostname_rewrite_enabled) field."
                                    type: bool
                                    returned: Always
                                hostname_rewrite_regex:
                                    description:
                                        - "The inheritance configuration for I(hostname_rewrite_regex) field."
                                    type: str
                                    returned: Always
        name:
            description:
                - "The name of the subnet. May contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol:
            description:
                - "The type of protocol of the subnet (I(ip4) or I(ip6))."
            type: str
            returned: Always
        rebind_time:
            description:
                - "The lease rebind time (T2) in seconds."
            type: int
            returned: Always
        renew_time:
            description:
                - "The lease renew time (T1) in seconds."
            type: int
            returned: Always
        space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the subnet in JSON format."
            type: dict
            returned: Always
        threshold:
            description:
                - "The IP address utilization threshold settings for the subnet."
            type: dict
            returned: Always
            contains:
                enabled:
                    description:
                        - "Indicates whether the utilization threshold for IP addresses is enabled or not."
                    type: bool
                    returned: Always
                high:
                    description:
                        - "The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
                low:
                    description:
                        - "The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        usage:
            description:
                - "The usage is a combination of indicators, each tracking a specific associated use. Listed below are usage indicators with their meaning:"
                - "* I(IPAM): Subnet is managed in BloxOne DDI."
                - "* I(DHCP): Subnet is served by a DHCP Host."
                - "* I(DISCOVERED): Subnet is discovered by some network discovery probe like Network Insight or NetMRI in NIOS."
            type: list
            returned: Always
        utilization:
            description:
                - "The IPV4 address utilization statistics of the subnet."
            type: dict
            returned: Always
            contains:
                abandon_utilization:
                    description:
                        - "The percentage of abandoned IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
                abandoned:
                    description:
                        - "The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client)."
                    type: str
                    returned: Always
                dynamic:
                    description:
                        - "The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases."
                    type: str
                    returned: Always
                free:
                    description:
                        - "The number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                static:
                    description:
                        - "The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) = I(used) - I(dynamic)."
                    type: str
                    returned: Always
                total:
                    description:
                        - "The total number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                used:
                    description:
                        - "The number of IP addresses used in the scope of the object."
                    type: str
                    returned: Always
                utilization:
                    description:
                        - "The percentage of used IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
        utilization_v6:
            description:
                - "The utilization of IPV6 addresses in the subnet."
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

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from ipam import Subnet, SubnetApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class SubnetModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(SubnetModule, self).__init__(*args, **kwargs)

        if "/" in self.params["address"]:
            self.params["address"], netmask = self.params["address"].split("/")
            self.params["cidr"] = int(netmask)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Subnet.from_dict(self._payload_params)

        # Unset unsupported DHCP configuration attributes
        if self._payload.dhcp_config:
            self._payload.dhcp_config.abandoned_reclaim_time = None
            self._payload.dhcp_config.abandoned_reclaim_time_v6 = None
            self._payload.dhcp_config.echo_client_id = None

        self._existing = None

    @property
    def existing(self):
        return self._existing

    @existing.setter
    def existing(self, value):
        self._existing = value

    @property
    def payload_params(self):
        return self._payload_params

    @property
    def payload(self):
        return self._payload

    def payload_changed(self):
        if self.existing is None:
            # if existing is None, then it is a create operation
            return True

        return self.is_changed(self.existing.model_dump(by_alias=True, exclude_none=True), self.payload_params)

    def find(self):
        if self.params["id"] is not None:
            try:
                resp = SubnetApi(self.client).read(self.params["id"], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"address=='{self.params['address']}' and space=='{self.params['space']}' and cidr=={self.params['cidr']}"
            resp = SubnetApi(self.client).list(filter=filter, inherit="full")
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Subnet: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = SubnetApi(self.client).create(body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["address", "space", "cidr"])

        resp = SubnetApi(self.client).update(id=self.existing.id, body=update_body, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        SubnetApi(self.client).delete(self.existing.id)

    def run_command(self):
        result = dict(changed=False, object={}, id=None)

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            self.existing = self.find()
            item = {}
            if self.params["state"] == "present" and self.existing is None:
                item = self.create()
                result["changed"] = True
                result["msg"] = "Subnet created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Subnet updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Subnet deleted"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result["diff"] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result["object"] = item
            result["id"] = (
                self.existing.id if self.existing is not None else item["id"] if (item and "id" in item) else None
            )
        except ApiException as e:
            self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        self.exit_json(**result)


def main():
    module_args = dict(
        id=dict(type="str", required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        address=dict(type="str"),
        asm_config=dict(
            type="dict",
            options=dict(
                asm_threshold=dict(type="int"),
                enable=dict(type="bool"),
                enable_notification=dict(type="bool"),
                forecast_period=dict(type="int"),
                growth_factor=dict(type="int"),
                growth_type=dict(type="str"),
                history=dict(type="int"),
                min_total=dict(type="int"),
                min_unused=dict(type="int"),
                reenable_date=dict(type="str"),
            ),
        ),
        cidr=dict(type="int"),
        comment=dict(type="str"),
        ddns_client_update=dict(type="str"),
        ddns_conflict_resolution_mode=dict(type="str"),
        ddns_domain=dict(type="str"),
        ddns_generate_name=dict(type="bool"),
        ddns_generated_prefix=dict(type="str"),
        ddns_send_updates=dict(type="bool"),
        ddns_ttl_percent=dict(type="float"),
        ddns_update_on_renew=dict(type="bool"),
        ddns_use_conflict_resolution=dict(type="bool"),
        dhcp_config=dict(
            type="dict",
            options=dict(
                allow_unknown=dict(type="bool"),
                allow_unknown_v6=dict(type="bool"),
                filters=dict(type="list", elements="str"),
                filters_v6=dict(type="list", elements="str"),
                ignore_client_uid=dict(type="bool"),
                ignore_list=dict(
                    type="list",
                    elements="dict",
                    options=dict(
                        type=dict(type="str"),
                        value=dict(type="str"),
                    ),
                ),
                lease_time=dict(type="int"),
                lease_time_v6=dict(type="int"),
            ),
        ),
        dhcp_host=dict(type="str"),
        dhcp_options=dict(
            type="list",
            elements="dict",
            options=dict(
                group=dict(type="str"),
                option_code=dict(type="str"),
                option_value=dict(type="str"),
                type=dict(type="str"),
            ),
        ),
        disable_dhcp=dict(type="bool"),
        header_option_filename=dict(type="str"),
        header_option_server_address=dict(type="str"),
        header_option_server_name=dict(type="str"),
        hostname_rewrite_char=dict(type="str"),
        hostname_rewrite_enabled=dict(type="bool"),
        hostname_rewrite_regex=dict(type="str"),
        inheritance_parent=dict(type="str"),
        inheritance_sources=dict(
            type="dict",
            options=dict(
                asm_config=dict(
                    type="dict",
                    options=dict(
                        asm_enable_block=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        asm_growth_block=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        asm_threshold=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        forecast_period=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        history=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        min_total=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        min_unused=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                    ),
                ),
                ddns_client_update=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_conflict_resolution_mode=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_enabled=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_hostname_block=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_ttl_percent=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_update_block=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_update_on_renew=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                ddns_use_conflict_resolution=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                dhcp_config=dict(
                    type="dict",
                    options=dict(
                        abandoned_reclaim_time=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        abandoned_reclaim_time_v6=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        allow_unknown=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        allow_unknown_v6=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        echo_client_id=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        filters=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                                value=dict(type="list", elements="str"),
                            ),
                        ),
                        filters_v6=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                                value=dict(type="list", elements="str"),
                            ),
                        ),
                        ignore_client_uid=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        ignore_list=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        lease_time=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        lease_time_v6=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                    ),
                ),
                dhcp_options=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                        value=dict(
                            type="list",
                            elements="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                    ),
                ),
                header_option_filename=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                header_option_server_address=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                header_option_server_name=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                hostname_rewrite_block=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
            ),
        ),
        name=dict(type="str"),
        parent=dict(type="str"),
        rebind_time=dict(type="int"),
        renew_time=dict(type="int"),
        space=dict(type="str"),
        tags=dict(type="dict"),
        threshold=dict(
            type="dict",
            options=dict(
                enabled=dict(type="bool"),
                high=dict(type="int"),
                low=dict(type="int"),
            ),
        ),
    )

    module = SubnetModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["address", "space"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
