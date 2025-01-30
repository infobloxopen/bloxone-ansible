#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_server_info
short_description: Retrieve a Server ( DNS Config Profile )
description:
    - Retrieves information about DNS Config Profiles.
    - A Server (DNS Config Profile) is a named configuration profile that can be shared for specified list of hosts.
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
  - name: Get DNS Server information by ID
    infoblox.bloxone.dns_server_info:
      id: "{{ dns_server_id }}"

  - name: Get DNS Server information by filters (e.g. name)
    infoblox.bloxone.dns_server_info:
      filters:
        name: "example_server"

  - name: Get DNS Server information by raw filter query
    infoblox.bloxone.dns_server_info:
      filter_query: "name=='example_server'"

  - name: Get DNS Server information by tag filters
    infoblox.bloxone.dns_server_info:
      tag_filters:
        location: "site-1"
"""

RETURN = r"""
id:
    description:
        - ID of the Server object
    type: str
    returned: Always
objects:
    description:
        - Server object
    type: list
    elements: dict
    returned: Always
    contains:
        add_edns_option_in_outgoing_query:
            description:
                - "I(add_edns_option_in_outgoing_query) adds client IP, MAC address and view name into outgoing recursive query. Defaults to I(false)."
            type: bool
            returned: Always
        auto_sort_views:
            description:
                - "Optional. Controls manual/automatic views ordering."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        comment:
            description:
                - "Optional. Comment for configuration."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        custom_root_ns:
            description:
                - "Optional. List of custom root nameservers. The order does not matter."
                - "Error if empty while I(custom_root_ns_enabled) is I(true). Error if there are duplicate items in the list."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "IPv4 address."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "FQDN."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN in punycode."
                    type: str
                    returned: Always
        custom_root_ns_enabled:
            description:
                - "Optional. I(true) to use custom root nameservers instead of the default ones."
                - "The I(custom_root_ns) is validated when enabled."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        dnssec_enable_validation:
            description:
                - "Optional. I(true) to perform DNSSEC validation. Ignored if I(dnssec_enabled) is I(false)."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        dnssec_enabled:
            description:
                - "Optional. Master toggle for all DNSSEC processing. Other I(dnssec)*_ configuration is unused if this is disabled."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        dnssec_root_keys:
            description:
                - "DNSSEC root keys. The root keys are not configurable."
                - "A default list is provided by cloud management and included here for config generation."
            type: list
            returned: Always
            elements: dict
            contains:
                algorithm:
                    description: 
                        - "Specifies the cryptographic algorithm used for DNSSEC. Supported values and their corresponding mappings are as follows."
                        - "RSAMD5 (1)"
                        - "DH (2)"
                        - "DSA (3)"
                        - "RSASHA1 (5)"
                        - "DSANSEC3SHA1 (6)"
                        - "RSASHA1NSEC3SHA1 (7)"
                        - "RSASHA256 (8)"
                        - "RSASHA512 (10)"
                        - "ECDSAP256SHA256 (13)"
                        - "ECDSAP384SHA384 (14)"
                        - "**Deprecated Algorithms:**"
                        - "RSAMD5 (1)"
                        - "DSA (3)"
                        - "DSANSEC3SHA1 (6)"
                    type: int
                    returned: Always
                protocol_zone:
                    description:
                        - "Zone FQDN in punycode."
                    type: str
                    returned: Always
                public_key:
                    description:
                        - "DNSSEC key data. Non-empty, valid base64 string."
                    type: str
                    returned: Always
                sep:
                    description:
                        - "Optional. Secure Entry Point flag."
                        - "Defaults to I(true)."
                    type: bool
                    returned: Always
                zone:
                    description:
                        - "Zone FQDN."
                    type: str
                    returned: Always
        dnssec_trust_anchors:
            description:
                - "Optional. DNSSEC trust anchors."
                - "Error if there are list items with duplicate (I(zone), I(sep), I(algorithm)) combinations."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                algorithm:
                    description: 
                        - "Specifies the cryptographic algorithm used for DNSSEC. Supported values and their corresponding mappings are as follows."
                        - "RSAMD5 (1)"
                        - "DH (2)"
                        - "DSA (3)"
                        - "RSASHA1 (5)"
                        - "DSANSEC3SHA1 (6)"
                        - "RSASHA1NSEC3SHA1 (7)"
                        - "RSASHA256 (8)"
                        - "RSASHA512 (10)"
                        - "ECDSAP256SHA256 (13)"
                        - "ECDSAP384SHA384 (14)"
                        - "**Deprecated Algorithms:**"
                        - "RSAMD5 (1)"
                        - "DSA (3)"
                        - "DSANSEC3SHA1 (6)"
                    type: int
                    returned: Always
                protocol_zone:
                    description:
                        - "Zone FQDN in punycode."
                    type: str
                    returned: Always
                public_key:
                    description:
                        - "DNSSEC key data. Non-empty, valid base64 string."
                    type: str
                    returned: Always
                sep:
                    description:
                        - "Optional. Secure Entry Point flag."
                        - "Defaults to I(true)."
                    type: bool
                    returned: Always
                zone:
                    description:
                        - "Zone FQDN."
                    type: str
                    returned: Always
        dnssec_validate_expiry:
            description:
                - "Optional. I(true) to reject expired DNSSEC keys. Ignored if either I(dnssec_enabled) or I(dnssec_enable_validation) is I(false)."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        ecs_enabled:
            description:
                - "Optional. I(true) to enable EDNS client subnet for recursive queries. Other I(ecs)*_ fields are ignored if this field is not enabled."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        ecs_forwarding:
            description:
                - "Optional. I(true) to enable ECS options in outbound queries. This functionality has additional overhead so it is disabled by default."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        ecs_prefix_v4:
            description:
                - "Optional. Maximum scope length for v4 ECS."
                - "Unsigned integer, min 1 max 24"
                - "Defaults to 24."
            type: int
            returned: Always
        ecs_prefix_v6:
            description:
                - "Optional. Maximum scope length for v6 ECS."
                - "Unsigned integer, min 1 max 56"
                - "Defaults to 56."
            type: int
            returned: Always
        ecs_zones:
            description:
                - "Optional. List of zones where ECS queries may be sent."
                - "Error if empty while I(ecs_enabled) is I(true). Error if there are duplicate FQDNs in the list."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access control for zone."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Zone FQDN."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "Zone FQDN in punycode."
                    type: str
                    returned: Always
        filter_aaaa_acl:
            description:
                - "Optional. Specifies a list of client addresses for which AAAA filtering is to be applied."
                - "Defaults to I(empty)."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        filter_aaaa_on_v4:
            description:
                - "I(filter_aaaa_on_v4) allows named to omit some IPv6 addresses when responding to IPv4 clients."
                - "Allowed values:"
                - "* I(yes),"
                - "* I(no),"
                - "* I(break_dnssec)."
                - "Defaults to I(no)"
            type: str
            returned: Always
        forwarders:
            description:
                - "Optional. List of forwarders."
                - "Error if empty while I(forwarders_only) or I(use_root_forwarders_for_local_resolution_with_b1td) is I(true). Error if there are items in the list with duplicate addresses."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Server IP address."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Server FQDN."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "Server FQDN in punycode."
                    type: str
                    returned: Always
        forwarders_only:
            description:
                - "Optional. I(true) to only forward."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        gss_tsig_enabled:
            description:
                - "I(gss_tsig_enabled) enables/disables GSS-TSIG signed dynamic updates."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "Optional. Inheritance configuration."
            type: dict
            returned: Always
            contains:
                add_edns_option_in_outgoing_query:
                    description:
                        - "Field config for I(add_edns_option_in_outgoing_query) field from I(Server) object."
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
                custom_root_ns_block:
                    description:
                        - "Optional. Field config for I(custom_root_ns_block) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: dict
                            returned: Always
                            contains:
                                custom_root_ns:
                                    description:
                                        - "Optional. Field config for I(custom_root_ns) field."
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        address:
                                            description:
                                                - "IPv4 address."
                                            type: str
                                            returned: Always
                                        fqdn:
                                            description:
                                                - "FQDN."
                                            type: str
                                            returned: Always
                                        protocol_fqdn:
                                            description:
                                                - "FQDN in punycode."
                                            type: str
                                            returned: Always
                                custom_root_ns_enabled:
                                    description:
                                        - "Optional. Field config for I(custom_root_ns_enabled) field."
                                    type: bool
                                    returned: Always
                dnssec_validation_block:
                    description:
                        - "Optional. Field config for I(dnssec_validation_block) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: dict
                            returned: Always
                            contains:
                                dnssec_enable_validation:
                                    description:
                                        - "Optional. Field config for I(dnssec_enable_validation) field."
                                    type: bool
                                    returned: Always
                                dnssec_enabled:
                                    description:
                                        - "Optional. Field config for I(dnssec_enabled) field."
                                    type: bool
                                    returned: Always
                                dnssec_trust_anchors:
                                    description:
                                        - "Optional. Field config for I(dnssec_trust_anchors) field."
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        algorithm:
                                            description: 
                                                - "Specifies the cryptographic algorithm used for DNSSEC. Supported values and their corresponding mappings are as follows."
                                                - "RSAMD5 (1)"
                                                - "DH (2)"
                                                - "DSA (3)"
                                                - "RSASHA1 (5)"
                                                - "DSANSEC3SHA1 (6)"
                                                - "RSASHA1NSEC3SHA1 (7)"
                                                - "RSASHA256 (8)"
                                                - "RSASHA512 (10)"
                                                - "ECDSAP256SHA256 (13)"
                                                - "ECDSAP384SHA384 (14)"
                                                - "**Deprecated Algorithms:**"
                                                - "RSAMD5 (1)"
                                                - "DSA (3)"
                                                - "DSANSEC3SHA1 (6)"
                                            type: int
                                            returned: Always
                                        protocol_zone:
                                            description:
                                                - "Zone FQDN in punycode."
                                            type: str
                                            returned: Always
                                        public_key:
                                            description:
                                                - "DNSSEC key data. Non-empty, valid base64 string."
                                            type: str
                                            returned: Always
                                        sep:
                                            description:
                                                - "Optional. Secure Entry Point flag."
                                                - "Defaults to I(true)."
                                            type: bool
                                            returned: Always
                                        zone:
                                            description:
                                                - "Zone FQDN."
                                            type: str
                                            returned: Always
                                dnssec_validate_expiry:
                                    description:
                                        - "Optional. Field config for I(dnssec_validate_expiry) field."
                                    type: bool
                                    returned: Always
                ecs_block:
                    description:
                        - "Optional. Field config for I(ecs_block) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: dict
                            returned: Always
                            contains:
                                ecs_enabled:
                                    description:
                                        - "Optional. Field config for I(ecs_enabled) field."
                                    type: bool
                                    returned: Always
                                ecs_forwarding:
                                    description:
                                        - "Optional. Field config for I(ecs_forwarding) field."
                                    type: bool
                                    returned: Always
                                ecs_prefix_v4:
                                    description:
                                        - "Optional. Field config for I(ecs_prefix_v4) field."
                                    type: int
                                    returned: Always
                                ecs_prefix_v6:
                                    description:
                                        - "Optional. Field config for I(ecs_prefix_v6) field."
                                    type: int
                                    returned: Always
                                ecs_zones:
                                    description:
                                        - "Optional. Field config for I(ecs_zones) field."
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        access:
                                            description:
                                                - "Access control for zone."
                                                - "Allowed values:"
                                                - "* I(allow),"
                                                - "* I(deny)."
                                            type: str
                                            returned: Always
                                        fqdn:
                                            description:
                                                - "Zone FQDN."
                                            type: str
                                            returned: Always
                                        protocol_fqdn:
                                            description:
                                                - "Zone FQDN in punycode."
                                            type: str
                                            returned: Always
                filter_aaaa_acl:
                    description:
                        - "Optional. Field config for I(filter_aaaa_acl) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                access:
                                    description:
                                        - "Access permission for I(element)."
                                        - "Allowed values:"
                                        - "* I(allow),"
                                        - "* I(deny)."
                                    type: str
                                    returned: Always
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                address:
                                    description:
                                        - "Optional. Data for I(ip) I(element)."
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                        - "* I(tsig_key)."
                                    type: str
                                    returned: Always
                                tsig_key:
                                    description:
                                        - "Optional. TSIG key."
                                        - "Must be empty if I(element) is not I(tsig_key)."
                                    type: dict
                                    returned: Always
                                    contains:
                                        algorithm:
                                            description:
                                                - "TSIG key algorithm."
                                                - "Possible values:"
                                                - "* I(hmac_sha256),"
                                                - "* I(hmac_sha1),"
                                                - "* I(hmac_sha224),"
                                                - "* I(hmac_sha384),"
                                                - "* I(hmac_sha512)."
                                            type: str
                                            returned: Always
                                        comment:
                                            description:
                                                - "Comment for TSIG key."
                                            type: str
                                            returned: Always
                                        key:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                                        name:
                                            description:
                                                - "TSIG key name, FQDN."
                                            type: str
                                            returned: Always
                                        protocol_name:
                                            description:
                                                - "TSIG key name in punycode."
                                            type: str
                                            returned: Always
                                        secret:
                                            description:
                                                - "TSIG key secret, base64 string."
                                            type: str
                                            returned: Always
                filter_aaaa_on_v4:
                    description:
                        - "Optional. Field config for I(filter_aaaa_on_v4) field from I(Server) object."
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
                forwarders_block:
                    description:
                        - "Optional. Field config for I(forwarders_block) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: dict
                            returned: Always
                            contains:
                                forwarders:
                                    description:
                                        - "Optional. Field config for I(forwarders) field from."
                                    type: list
                                    returned: Always
                                    elements: dict
                                    contains:
                                        address:
                                            description:
                                                - "Server IP address."
                                            type: str
                                            returned: Always
                                        fqdn:
                                            description:
                                                - "Server FQDN."
                                            type: str
                                            returned: Always
                                        protocol_fqdn:
                                            description:
                                                - "Server FQDN in punycode."
                                            type: str
                                            returned: Always
                                forwarders_only:
                                    description:
                                        - "Optional. Field config for I(forwarders_only) field."
                                    type: bool
                                    returned: Always
                                use_root_forwarders_for_local_resolution_with_b1td:
                                    description:
                                        - "Optional. Field config for I(use_root_forwarders_for_local_resolution_with_b1td) field."
                                    type: bool
                                    returned: Always
                gss_tsig_enabled:
                    description:
                        - "Optional. Field config for I(gss_tsig_enabled) field from I(Server) object."
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
                kerberos_keys:
                    description:
                        - "Optional. Field config for I(kerberos_keys) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                algorithm:
                                    description:
                                        - "Encryption algorithm of the key in accordance with RFC 3961."
                                    type: str
                                    returned: Always
                                domain:
                                    description:
                                        - "Kerberos realm of the principal."
                                    type: str
                                    returned: Always
                                key:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                principal:
                                    description:
                                        - "Kerberos principal associated with key."
                                    type: str
                                    returned: Always
                                uploaded_at:
                                    description:
                                        - "Upload time for the key."
                                    type: str
                                    returned: Always
                                version:
                                    description:
                                        - "The version number (KVNO) of the key."
                                    type: int
                                    returned: Always
                lame_ttl:
                    description:
                        - "Optional. Field config for I(lame_ttl) field from I(Server) object."
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
                log_query_response:
                    description:
                        - "Optional. Field config for I(log_queries_response) field from I(Server) object."
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
                match_recursive_only:
                    description:
                        - "Optional. Field config for I(match_recursive_only) field from I(Server) object."
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
                max_cache_ttl:
                    description:
                        - "Optional. Field config for I(max_cache_ttl) field from I(Server) object."
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
                max_negative_ttl:
                    description:
                        - "Optional. Field config for I(max_negative_ttl) field from I(Server) object."
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
                minimal_responses:
                    description:
                        - "Optional. Field config for I(minimal_responses) field from I(Server) object."
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
                notify:
                    description:
                        - "Field config for I(notify) field from I(Server) object."
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
                query_acl:
                    description:
                        - "Optional. Field config for I(query_acl) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                access:
                                    description:
                                        - "Access permission for I(element)."
                                        - "Allowed values:"
                                        - "* I(allow),"
                                        - "* I(deny)."
                                    type: str
                                    returned: Always
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                address:
                                    description:
                                        - "Optional. Data for I(ip) I(element)."
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                        - "* I(tsig_key)."
                                    type: str
                                    returned: Always
                                tsig_key:
                                    description:
                                        - "Optional. TSIG key."
                                        - "Must be empty if I(element) is not I(tsig_key)."
                                    type: dict
                                    returned: Always
                                    contains:
                                        algorithm:
                                            description:
                                                - "TSIG key algorithm."
                                                - "Possible values:"
                                                - "* I(hmac_sha256),"
                                                - "* I(hmac_sha1),"
                                                - "* I(hmac_sha224),"
                                                - "* I(hmac_sha384),"
                                                - "* I(hmac_sha512)."
                                            type: str
                                            returned: Always
                                        comment:
                                            description:
                                                - "Comment for TSIG key."
                                            type: str
                                            returned: Always
                                        key:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                                        name:
                                            description:
                                                - "TSIG key name, FQDN."
                                            type: str
                                            returned: Always
                                        protocol_name:
                                            description:
                                                - "TSIG key name in punycode."
                                            type: str
                                            returned: Always
                                        secret:
                                            description:
                                                - "TSIG key secret, base64 string."
                                            type: str
                                            returned: Always
                query_port:
                    description:
                        - "Optional. Field config for I(query_port) field from I(Server) object."
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
                recursion_acl:
                    description:
                        - "Optional. Field config for I(recursion_acl) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                access:
                                    description:
                                        - "Access permission for I(element)."
                                        - "Allowed values:"
                                        - "* I(allow),"
                                        - "* I(deny)."
                                    type: str
                                    returned: Always
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                address:
                                    description:
                                        - "Optional. Data for I(ip) I(element)."
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                        - "* I(tsig_key)."
                                    type: str
                                    returned: Always
                                tsig_key:
                                    description:
                                        - "Optional. TSIG key."
                                        - "Must be empty if I(element) is not I(tsig_key)."
                                    type: dict
                                    returned: Always
                                    contains:
                                        algorithm:
                                            description:
                                                - "TSIG key algorithm."
                                                - "Possible values:"
                                                - "* I(hmac_sha256),"
                                                - "* I(hmac_sha1),"
                                                - "* I(hmac_sha224),"
                                                - "* I(hmac_sha384),"
                                                - "* I(hmac_sha512)."
                                            type: str
                                            returned: Always
                                        comment:
                                            description:
                                                - "Comment for TSIG key."
                                            type: str
                                            returned: Always
                                        key:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                                        name:
                                            description:
                                                - "TSIG key name, FQDN."
                                            type: str
                                            returned: Always
                                        protocol_name:
                                            description:
                                                - "TSIG key name in punycode."
                                            type: str
                                            returned: Always
                                        secret:
                                            description:
                                                - "TSIG key secret, base64 string."
                                            type: str
                                            returned: Always
                recursion_enabled:
                    description:
                        - "Optional. Field config for I(recursion_enabled) field from I(Server) object."
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
                recursive_clients:
                    description:
                        - "Optional. Field config for I(recursive_clients) field from I(Server) object."
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
                resolver_query_timeout:
                    description:
                        - "Optional. Field config for I(resolver_query_timeout) field from I(Server) object."
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
                secondary_axfr_query_limit:
                    description:
                        - "Optional. Field config for I(secondary_axfr_query_limit) field from I(Server) object."
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
                secondary_soa_query_limit:
                    description:
                        - "Optional. Field config for I(secondary_soa_query_limit) field from I(Server) object."
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
                sort_list:
                    description:
                        - "Optional. Field config for I(sort_list) field from _Server object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                    type: str
                                    returned: Always
                                prioritized_networks:
                                    description:
                                        - "Optional. The prioritized networks. If empty, the value of I(source) or networks from I(acl) is used."
                                    type: list
                                    returned: Always
                                source:
                                    description:
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                synthesize_address_records_from_https:
                    description:
                        - "Field config for I(synthesize_address_records_from_https) field from I(Server) object."
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
                transfer_acl:
                    description:
                        - "Optional. Field config for I(transfer_acl) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                access:
                                    description:
                                        - "Access permission for I(element)."
                                        - "Allowed values:"
                                        - "* I(allow),"
                                        - "* I(deny)."
                                    type: str
                                    returned: Always
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                address:
                                    description:
                                        - "Optional. Data for I(ip) I(element)."
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                        - "* I(tsig_key)."
                                    type: str
                                    returned: Always
                                tsig_key:
                                    description:
                                        - "Optional. TSIG key."
                                        - "Must be empty if I(element) is not I(tsig_key)."
                                    type: dict
                                    returned: Always
                                    contains:
                                        algorithm:
                                            description:
                                                - "TSIG key algorithm."
                                                - "Possible values:"
                                                - "* I(hmac_sha256),"
                                                - "* I(hmac_sha1),"
                                                - "* I(hmac_sha224),"
                                                - "* I(hmac_sha384),"
                                                - "* I(hmac_sha512)."
                                            type: str
                                            returned: Always
                                        comment:
                                            description:
                                                - "Comment for TSIG key."
                                            type: str
                                            returned: Always
                                        key:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                                        name:
                                            description:
                                                - "TSIG key name, FQDN."
                                            type: str
                                            returned: Always
                                        protocol_name:
                                            description:
                                                - "TSIG key name in punycode."
                                            type: str
                                            returned: Always
                                        secret:
                                            description:
                                                - "TSIG key secret, base64 string."
                                            type: str
                                            returned: Always
                update_acl:
                    description:
                        - "Optional. Field config for I(update_acl) field from I(Server) object."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                            type: str
                            returned: Always
                        display_name:
                            description:
                                - "Human-readable display name for the object referred to by I(source)."
                            type: str
                            returned: Always
                        source:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "Inherited value."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                access:
                                    description:
                                        - "Access permission for I(element)."
                                        - "Allowed values:"
                                        - "* I(allow),"
                                        - "* I(deny)."
                                    type: str
                                    returned: Always
                                acl:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                address:
                                    description:
                                        - "Optional. Data for I(ip) I(element)."
                                        - "Must be empty if I(element) is not I(ip)."
                                    type: str
                                    returned: Always
                                element:
                                    description:
                                        - "Type of element."
                                        - "Allowed values:"
                                        - "* I(any),"
                                        - "* I(ip),"
                                        - "* I(acl),"
                                        - "* I(tsig_key)."
                                    type: str
                                    returned: Always
                                tsig_key:
                                    description:
                                        - "Optional. TSIG key."
                                        - "Must be empty if I(element) is not I(tsig_key)."
                                    type: dict
                                    returned: Always
                                    contains:
                                        algorithm:
                                            description:
                                                - "TSIG key algorithm."
                                                - "Possible values:"
                                                - "* I(hmac_sha256),"
                                                - "* I(hmac_sha1),"
                                                - "* I(hmac_sha224),"
                                                - "* I(hmac_sha384),"
                                                - "* I(hmac_sha512)."
                                            type: str
                                            returned: Always
                                        comment:
                                            description:
                                                - "Comment for TSIG key."
                                            type: str
                                            returned: Always
                                        key:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
                                        name:
                                            description:
                                                - "TSIG key name, FQDN."
                                            type: str
                                            returned: Always
                                        protocol_name:
                                            description:
                                                - "TSIG key name in punycode."
                                            type: str
                                            returned: Always
                                        secret:
                                            description:
                                                - "TSIG key secret, base64 string."
                                            type: str
                                            returned: Always
                use_forwarders_for_subzones:
                    description:
                        - "Optional. Field config for I(use_forwarders_for_subzones) field from I(Server) object."
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
        kerberos_keys:
            description:
                - "I(kerberos_keys) contains a list of keys for GSS-TSIG signed dynamic updates."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                algorithm:
                    description:
                        - "Encryption algorithm of the key in accordance with RFC 3961."
                    type: str
                    returned: Always
                domain:
                    description:
                        - "Kerberos realm of the principal."
                    type: str
                    returned: Always
                key:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                principal:
                    description:
                        - "Kerberos principal associated with key."
                    type: str
                    returned: Always
                uploaded_at:
                    description:
                        - "Upload time for the key."
                    type: str
                    returned: Always
                version:
                    description:
                        - "The version number (KVNO) of the key."
                    type: int
                    returned: Always
        lame_ttl:
            description:
                - "Optional. Unused in the current on-prem DNS server implementation."
                - "Unsigned integer, min 0 max 3600 (1h)."
                - "Defaults to 600."
            type: int
            returned: Always
        log_query_response:
            description:
                - "Optional. Control DNS query/response logging functionality."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        match_recursive_only:
            description:
                - "Optional. If I(true) only recursive queries from matching clients access the view."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        max_cache_ttl:
            description:
                - "Optional. Seconds to cache positive responses."
                - "Unsigned integer, min 1 max 604800 (7d)."
                - "Defaults to 604800 (7d)."
            type: int
            returned: Always
        max_negative_ttl:
            description:
                - "Optional. Seconds to cache negative responses."
                - "Unsigned integer, min 1 max 604800 (7d)."
                - "Defaults to 10800 (3h)."
            type: int
            returned: Always
        minimal_responses:
            description:
                - "Optional. When enabled, the DNS server will only add records to the authority and additional data sections when they are required."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        name:
            description:
                - "Name of configuration."
            type: str
            returned: Always
        notify:
            description:
                - "I(notify) all external secondary DNS servers."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        query_acl:
            description:
                - "Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        query_port:
            description:
                - "Optional. Source port for outbound DNS queries. When set to 0 the port is unspecified and the implementation may randomize it using any available ports."
                - "Defaults to 0."
            type: int
            returned: Always
        recursion_acl:
            description:
                - "Optional. Clients must match this ACL to make recursive queries. If this ACL is empty, then the I(query_acl) field will be used instead."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        recursion_enabled:
            description:
                - "Optional. I(true) to allow recursive DNS queries."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        recursive_clients:
            description:
                - "Optional. Defines the number of simultaneous recursive lookups the server will perform on behalf of its clients."
                - "Defaults to 1000."
            type: int
            returned: Always
        resolver_query_timeout:
            description:
                - "Optional. Seconds before a recursive query times out."
                - "Unsigned integer, min 10 max 30."
                - "Defaults to 10."
            type: int
            returned: Always
        secondary_axfr_query_limit:
            description:
                - "Optional. Maximum concurrent inbound AXFRs. When set to 0 a host-dependent default will be used."
                - "Defaults to 0."
            type: int
            returned: Always
        secondary_soa_query_limit:
            description:
                - "Optional. Maximum concurrent outbound SOA queries. When set to 0 a host-dependent default will be used."
                - "Defaults to 0."
            type: int
            returned: Always
        sort_list:
            description:
                - "Optional. Specifies a sorted network list for A/AAAA records in DNS query response."
                - "Defaults to I(empty)."
            type: list
            returned: Always
            elements: dict
            contains:
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                    type: str
                    returned: Always
                prioritized_networks:
                    description:
                        - "Optional. The prioritized networks. If empty, the value of I(source) or networks from I(acl) is used."
                    type: list
                    returned: Always
                source:
                    description:
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
        synthesize_address_records_from_https:
            description:
                - "I(synthesize_address_records_from_https) enables/disables creation of A/AAAA records from HTTPS RR Defaults to I(false)."
            type: bool
            returned: Always
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
        transfer_acl:
            description:
                - "Optional. Clients must match this ACL to receive zone transfers."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        update_acl:
            description:
                - "Optional. Specifies which hosts are allowed to issue Dynamic DNS updates for authoritative zones of I(primary_type) I(cloud)."
                - "Defaults to empty."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "Access permission for I(element)."
                        - "Allowed values:"
                        - "* I(allow),"
                        - "* I(deny)."
                    type: str
                    returned: Always
                acl:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                address:
                    description:
                        - "Optional. Data for I(ip) I(element)."
                        - "Must be empty if I(element) is not I(ip)."
                    type: str
                    returned: Always
                element:
                    description:
                        - "Type of element."
                        - "Allowed values:"
                        - "* I(any),"
                        - "* I(ip),"
                        - "* I(acl),"
                        - "* I(tsig_key)."
                    type: str
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Must be empty if I(element) is not I(tsig_key)."
                    type: dict
                    returned: Always
                    contains:
                        algorithm:
                            description:
                                - "TSIG key algorithm."
                                - "Possible values:"
                                - "* I(hmac_sha256),"
                                - "* I(hmac_sha1),"
                                - "* I(hmac_sha224),"
                                - "* I(hmac_sha384),"
                                - "* I(hmac_sha512)."
                            type: str
                            returned: Always
                        comment:
                            description:
                                - "Comment for TSIG key."
                            type: str
                            returned: Always
                        key:
                            description:
                                - "The resource identifier."
                            type: str
                            returned: Always
                        name:
                            description:
                                - "TSIG key name, FQDN."
                            type: str
                            returned: Always
                        protocol_name:
                            description:
                                - "TSIG key name in punycode."
                            type: str
                            returned: Always
                        secret:
                            description:
                                - "TSIG key secret, base64 string."
                            type: str
                            returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        use_forwarders_for_subzones:
            description:
                - "Optional. Use default forwarders to resolve queries for subzones."
                - "Defaults to I(true)."
            type: bool
            returned: Always
        use_root_forwarders_for_local_resolution_with_b1td:
            description:
                - "I(use_root_forwarders_for_local_resolution_with_b1td) allows DNS recursive queries sent to root forwarders for local resolution when deployed alongside BloxOne Thread Defense. Defaults to I(false)."
            type: bool
            returned: Always
        views:
            description:
                - "Optional. Ordered list of I(dns/display_view) objects served by any of I(dns/host) assigned to a particular DNS Config Profile. Automatically determined. Allows re-ordering only."
            type: list
            returned: Always
            elements: dict
            contains:
                comment:
                    description:
                        - "DNS view description."
                    type: str
                    returned: Always
                name:
                    description:
                        - "DNS view name."
                    type: str
                    returned: Always
                view:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_config import ServerApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class ServerInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(ServerInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = ServerApi(self.client).read(self.params["id"], inherit="full")
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
                resp = ServerApi(self.client).list(
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

    module = ServerInfoModule(
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
