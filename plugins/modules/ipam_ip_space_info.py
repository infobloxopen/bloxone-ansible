#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_ip_space_info
short_description: Retrieves information about existing IP Spaces.
description:
    - Retrieves information about existing IP Spaces.
    - The IP Space object represents an entire address space
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

EXAMPLES = r"""
  - name: Get IP Space information by ID
    infoblox.bloxone.ipam_ip_space_info:
      id: "{{ ip_space_id }}"

  - name: Get IP Space information by filters (e.g. name)
    infoblox.bloxone.ipam_ip_space_info:
      filters:
        name: "my-ip-space"

  - name: Get IP Space information by raw filter query
    infoblox.bloxone.ipam_ip_space_info:
      filter_query: "name=='my-ip-space'"

  - name: Get IP Space information by tag filters
    infoblox.bloxone.ipam_ip_space_info:
      tag_filters:
        location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the IpSpace object
    type: str
    returned: Always
objects:
    description:
        - IpSpace object
    type: list
    elements: dict
    returned: Always
    contains:
        asm_config:
            description:
                - "The Automated Scope Management configuration for the IP space."
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
                    description:
                        - "The date at which notifications will be re-enabled automatically."
                    type: str
                    returned: Always
        asm_scope_flag:
            description:
                - "The number of times the automated scope management usage limits have been exceeded for any of the subnets in this IP space."
            type: int
            returned: Always
        comment:
            description:
                - "The description for the IP space. May contain 0 to 1024 characters. Can include UTF-8."
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
                - "Defaults to &quot;myhost&quot;."
            type: str
            returned: Always
        ddns_send_updates:
            description:
                - "Determines if DDNS updates are enabled at the IP space level. Defaults to I(true)."
            type: bool
            returned: Always
        ddns_ttl_percent:
            description:
                - "DDNS TTL value - to be calculated as a simple percentage of the lease&#x27;s lifetime, using the parameter&#x27;s value as the percentage. It is specified as a percentage (e.g. 25, 75). Defaults to unspecified."
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
                - "The shared DHCP configuration for the IP space that controls how leases are issued."
            type: dict
            returned: Always
            contains:
                abandoned_reclaim_time:
                    description:
                        - "The abandoned reclaim time in seconds for IPV4 clients."
                    type: int
                    returned: Always
                abandoned_reclaim_time_v6:
                    description:
                        - "The abandoned reclaim time in seconds for IPV6 clients."
                    type: int
                    returned: Always
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
                echo_client_id:
                    description:
                        - "Enable/disable to include/exclude the client id when responding to discover or request."
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
        dhcp_options:
            description:
                - "The list of IPv4 DHCP options for IP space. May be either a specific option or a group of options."
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
        dhcp_options_v6:
            description:
                - "The list of IPv6 DHCP options for IP space. May be either a specific option or a group of options."
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
                - "Defaults to &quot;-&quot;."
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
                - "Must begin with &quot;[&quot; and end with &quot;]&quot; and be a compilable POSIX regex."
                - "Defaults to &quot;[^a-zA-Z0-9_.]&quot;."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The inheritance configuration."
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
                        - "The inheritance configuration for I(ddns_client_update) field from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_conflict_resolution_mode) field from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_enabled) field. Only action allowed is &#x27;inherit&#x27;."
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
                        - "The inheritance configuration for I(ddns_generate_name) and I(ddns_generated_prefix) fields from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_ttl_percent) field from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_send_updates) and I(ddns_domain) fields from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_update_on_renew) field from I(IPSpace) object."
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
                        - "The inheritance configuration for I(ddns_use_conflict_resolution) field from I(IPSpace) object."
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
                                - "* I(block): Don&#x27;t use the inherited value."
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
                                        - "* I(block): Don&#x27;t use the inherited value."
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
                dhcp_options_v6:
                    description:
                        - "The inheritance configuration for I(dhcp_options_v6) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(block): Don&#x27;t use the inherited value."
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
                                        - "* I(block): Don&#x27;t use the inherited value."
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
                        - "The inheritance configuration for I(hostname_rewrite_enabled), I(hostname_rewrite_regex), and I(hostname_rewrite_char) fields from I(IPSpace) object."
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
                vendor_specific_option_option_space:
                    description:
                        - "The inheritance configuration for I(vendor_specific_option_option_space) field."
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
                                - "The resource identifier."
                            type: str
                            returned: Always
        name:
            description:
                - "The name of the IP space. Must contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the IP space in JSON format."
            type: dict
            returned: Always
        threshold:
            description:
                - "The utilization threshold settings for the IP space."
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
        utilization:
            description:
                - "The utilization of IPV4 addresses in the IP space."
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
                        - "The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) &#x3D; I(used) - I(dynamic)."
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
                - "The utilization of IPV6 addresses in the IP space."
            type: dict
            returned: Always
            contains:
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
                static:
                    description:
                        - "The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) &#x3D; I(used) - I(dynamic)."
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
        vendor_specific_option_option_space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from ipam import IpSpaceApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class IPSpaceInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(IPSpaceInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = IpSpaceApi(self.client).read(self.params["id"], inherit="full")
            return [resp.result]
        except NotFoundException as e:
            return None

    def find(self):
        if self.params["id"] is not None:
            return self.find_by_id()

        filter_str = None
        if self.params["filters"] is not None:
            filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["filters"].items()])
        elif self.params["filter_query"] is not None:
            filter_str = self.params["filter_query"]

        tag_filter_str = None
        if self.params["tag_filters"] is not None:
            tag_filter_str = " and ".join([f"{k}=='{v}'" for k, v in self.params["tag_filters"].items()])
        elif self.params["tag_filter_query"] is not None:
            tag_filter_str = self.params["tag_filter_query"]

        all_results = []
        offset = 0

        while True:
            try:
                resp = IpSpaceApi(self.client).list(
                    offset=offset, limit=self._limit, filter=filter_str, tfilter=tag_filter_str, inherit="full"
                )
                all_results.extend(resp.results)

                if len(resp.results) < self._limit:
                    break
                offset += self._limit

            except ApiException as e:
                self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        return all_results

    def run_command(self):
        result = dict(objects=[])

        if self.check_mode:
            self.exit_json(**result)

        find_results = self.find()

        all_results = []
        for r in find_results:
            all_results.append(r.model_dump(by_alias=True, exclude_none=True))

        result["objects"] = all_results
        self.exit_json(**result)


def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        id=dict(type="str", required=False),
        filters=dict(type="dict", required=False),
        filter_query=dict(type="str", required=False),
        inherit=dict(type="str", required=False, choices=["full", "partial", "none"], default="full"),
        tag_filters=dict(type="dict", required=False),
        tag_filter_query=dict(type="str", required=False),
    )

    module = IPSpaceInfoModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[
            ["id", "filters", "filter_query"],
            ["id", "tag_filters", "tag_filter_query"],
        ],
    )
    module.run_command()


if __name__ == "__main__":
    main()
