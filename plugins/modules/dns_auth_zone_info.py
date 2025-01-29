#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_auth_zone_info
short_description: Manage AuthZone
description:
    - Manage AuthZone
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
  - name: Get Auth Zone information by ID
    infoblox.bloxone.dns_auth_zone_info:
      id: "{{ auth_zone_id }}"

  - name: Get Auth Zone information by filters (e.g. name)
    infoblox.bloxone.dns_auth_zone_info:
      filters:
        fqdn: "example_zone"

  - name: Get Auth Zone information by raw filter query
    infoblox.bloxone.dns_auth_zone_info:
      filter_query: "name=='example_zone'"

  - name: Get Auth Zone information by tag filters
    infoblox.bloxone.dns_auth_zone_info:
      tag_filters:
        location: "site-1"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the AuthZone object
    type: str
    returned: Always
objects:
    description:
        - AuthZone object
    type: list
    elements: dict
    returned: Always
    contains:
        comment:
            description:
                - "Optional. Comment for zone configuration."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        disabled:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
            type: bool
            returned: Always
        external_primaries:
            description:
                - "Optional. DNS primaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "Optional. Required only if I(type) is I(server). IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "Optional. Required only if I(type) is I(server). FQDN of nameserver."
                    type: str
                    returned: Always
                nsg:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                tsig_enabled:
                    description:
                        - "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "Optional. TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
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
                type:
                    description:
                        - "Allowed values:"
                        - "* I(nsg),"
                        - "* I(primary)."
                    type: str
                    returned: Always
        external_providers:
            description:
                - "list of external providers for the auth zone."
            type: list
            returned: Always
            elements: dict
            contains:
                id:
                    description:
                        - "The identifier of the external provider."
                    type: str
                    returned: Always
                name:
                    description:
                        - "The name of the external provider."
                    type: str
                    returned: Always
                type:
                    description:
                        - "Defines the type of external provider. Allowed values:"
                        - "* I(bloxone_ddi): host type is BloxOne DDI,"
                        - "* I(microsoft_azure): host type is Microsoft Azure,"
                        - "* I(amazon_web_service): host type is Amazon Web Services,"
                        - "* I(microsoft_active_directory): host type is Microsoft Active Directory,"
                        - "* I(google_cloud_platform): host type is Google Cloud Platform."
                    type: str
                    returned: Always
        external_secondaries:
            description:
                - "DNS secondaries external to BloxOne DDI. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                address:
                    description:
                        - "IP Address of nameserver."
                    type: str
                    returned: Always
                fqdn:
                    description:
                        - "FQDN of nameserver."
                    type: str
                    returned: Always
                protocol_fqdn:
                    description:
                        - "FQDN of nameserver in punycode."
                    type: str
                    returned: Always
                stealth:
                    description:
                        - "If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_enabled:
                    description:
                        - "If enabled, secondaries will use the configured TSIG key when requesting a zone transfer."
                        - "Default: I(false)"
                    type: bool
                    returned: Always
                tsig_key:
                    description:
                        - "TSIG key."
                        - "Error if empty while I(tsig_enabled) is I(true)."
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
        fqdn:
            description:
                - "Zone FQDN. The FQDN supplied at creation will be converted to canonical form."
                - "Read-only after creation."
            type: str
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
        inheritance_sources:
            description:
                - "Optional. Inheritance configuration."
            type: dict
            returned: Always
            contains:
                gss_tsig_enabled:
                    description:
                        - "Optional. Field config for I(gss_tsig_enabled) field from I(AuthZone) object."
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
                        - "Field config for I(notify) field from I(AuthZone) object."
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
                        - "Optional. Field config for I(query_acl) field from I(AuthZone) object."
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
                transfer_acl:
                    description:
                        - "Optional. Field config for I(transfer_acl) field from I(AuthZone) object."
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
                        - "Optional. Field config for I(update_acl) field from I(AuthZone) object."
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
                        - "Optional. Field config for I(use_forwarders_for_subzones) field from I(AuthZone) object."
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
                zone_authority:
                    description:
                        - "Optional. Field config for I(zone_authority) field from I(AuthZone) object."
                    type: dict
                    returned: Always
                    contains:
                        default_ttl:
                            description:
                                - "Optional. Field config for I(default_ttl) field from I(ZoneAuthority) object."
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
                        expire:
                            description:
                                - "Optional. Field config for I(expire) field from I(ZoneAuthority) object."
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
                        mname_block:
                            description:
                                - "Optional. Field config for I(mname) block from I(ZoneAuthority) object."
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
                                        mname:
                                            description:
                                                - "Defaults to empty."
                                            type: str
                                            returned: Always
                                        protocol_mname:
                                            description:
                                                - "Optional. Master name server in punycode."
                                                - "Defaults to empty."
                                            type: str
                                            returned: Always
                                        use_default_mname:
                                            description:
                                                - "Optional. Use default value for master name server."
                                                - "Defaults to true."
                                            type: bool
                                            returned: Always
                        negative_ttl:
                            description:
                                - "Optional. Field config for I(negative_ttl) field from I(ZoneAuthority) object."
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
                        protocol_rname:
                            description:
                                - "Optional. Field config for I(protocol_rname) field from I(ZoneAuthority) object."
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
                        refresh:
                            description:
                                - "Optional. Field config for I(refresh) field from I(ZoneAuthority) object."
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
                        retry:
                            description:
                                - "Optional. Field config for I(retry) field from I(ZoneAuthority) object."
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
                        rname:
                            description:
                                - "Optional. Field config for I(rname) field from I(ZoneAuthority) object."
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
        initial_soa_serial:
            description:
                - "On-create-only. SOA serial is allowed to be set when the authoritative zone is created."
            type: int
            returned: Always
        internal_secondaries:
            description:
                - "Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant."
            type: list
            returned: Always
            elements: dict
            contains:
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        mapped_subnet:
            description:
                - "Reverse zone network address in the following format: &quot;ip-address/cidr&quot;. Defaults to empty."
            type: str
            returned: Always
        mapping:
            description:
                - "Zone mapping type. Allowed values:"
                - "* I(forward),"
                - "* I(ipv4_reverse)."
                - "* I(ipv6_reverse)."
                - "Defaults to forward."
            type: str
            returned: Always
        notify:
            description:
                - "Also notify all external secondary DNS servers if enabled."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        nsgs:
            description:
                - "The resource identifier."
            type: list
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        primary_type:
            description:
                - "Primary type for an authoritative zone. Read only after creation. Allowed values:"
                - "* I(external): zone data owned by an external nameserver,"
                - "* I(cloud): zone data is owned by a BloxOne DDI host."
            type: str
            returned: Always
        protocol_fqdn:
            description:
                - "Zone FQDN in punycode."
            type: str
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
        tags:
            description:
                - "Tagging specifics."
            type: dict
            returned: Always
        transfer_acl:
            description:
                - "Optional. Clients must match this ACL to receive zone transfers."
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
                - "Optional. Specifies which hosts are allowed to submit Dynamic DNS updates for authoritative zones of I(primary_type) I(cloud)."
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
        view:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        warnings:
            description:
                - "The list of an auth zone warnings."
            type: list
            returned: Always
            elements: dict
            contains:
                message:
                    description:
                        - "Warning message."
                    type: str
                    returned: Always
                name:
                    description:
                        - "Name of a warning."
                    type: str
                    returned: Always
        zone_authority:
            description:
                - "Optional. ZoneAuthority."
            type: dict
            returned: Always
            contains:
                default_ttl:
                    description:
                        - "Optional. ZoneAuthority default ttl for resource records in zone (value in seconds)."
                        - "Defaults to 28800."
                    type: int
                    returned: Always
                expire:
                    description:
                        - "Optional. ZoneAuthority expire time in seconds."
                        - "Defaults to 2419200."
                    type: int
                    returned: Always
                mname:
                    description:
                        - "Defaults to empty."
                    type: str
                    returned: Always
                negative_ttl:
                    description:
                        - "Optional. ZoneAuthority negative caching (minimum) ttl in seconds."
                        - "Defaults to 900."
                    type: int
                    returned: Always
                protocol_mname:
                    description:
                        - "Optional. ZoneAuthority master name server in punycode."
                        - "Defaults to empty."
                    type: str
                    returned: Always
                protocol_rname:
                    description:
                        - "Optional. A domain name which specifies the mailbox of the person responsible for this zone."
                        - "Defaults to empty."
                    type: str
                    returned: Always
                refresh:
                    description:
                        - "Optional. ZoneAuthority refresh."
                        - "Defaults to 10800."
                    type: int
                    returned: Always
                retry:
                    description:
                        - "Optional. ZoneAuthority retry."
                        - "Defaults to 3600."
                    type: int
                    returned: Always
                rname:
                    description:
                        - "Optional. ZoneAuthority rname."
                        - "Defaults to empty."
                    type: str
                    returned: Always
                use_default_mname:
                    description:
                        - "Optional. Use default value for master name server."
                        - "Defaults to true."
                    type: bool
                    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from dns_config import AuthZoneApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AuthZoneInfoModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AuthZoneInfoModule, self).__init__(*args, **kwargs)
        self._existing = None
        self._limit = 1000

    def find_by_id(self):
        try:
            resp = AuthZoneApi(self.client).read(self.params["id"], inherit="full")
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
                resp = AuthZoneApi(self.client).list(
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

    module = AuthZoneInfoModule(
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
