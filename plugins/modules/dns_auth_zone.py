#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_auth_zone
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
    state:
        description:
            - Indicate desired state of the object
        type: str
        required: false
        choices:
            - present
            - absent
        default: present
    comment:
        description:
            - "Optional. Comment for zone configuration."
        type: str
    disabled:
        description:
            - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
        type: bool
    external_primaries:
        description:
            - "Optional. DNS primaries external to BloxOne DDI. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "Optional. Required only if I(type) is I(server). IP Address of nameserver."
                type: str
            fqdn:
                description:
                    - "Optional. Required only if I(type) is I(server). FQDN of nameserver."
                type: str
            nsg:
                description:
                    - "The resource identifier."
                type: str
            tsig_enabled:
                description:
                    - "Optional. If enabled, secondaries will use the configured TSIG key when requesting a zone transfer from this primary."
                type: bool
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Error if empty while I(tsig_enabled) is I(true)."
                type: dict
                suboptions:
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
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
            type:
                description:
                    - "Allowed values:"
                    - "* I(nsg),"
                    - "* I(primary)."
                type: str
    external_secondaries:
        description:
            - "DNS secondaries external to BloxOne DDI. Order is not significant."
        type: list
        elements: dict
        suboptions:
            address:
                description:
                    - "IP Address of nameserver."
                type: str
            fqdn:
                description:
                    - "FQDN of nameserver."
                type: str
            stealth:
                description:
                    - "If enabled, the NS record and glue record will NOT be automatically generated according to secondaries nameserver assignment."
                    - "Default: I(false)"
                type: bool
            tsig_enabled:
                description:
                    - "If enabled, secondaries will use the configured TSIG key when requesting a zone transfer."
                    - "Default: I(false)"
                type: bool
            tsig_key:
                description:
                    - "TSIG key."
                    - "Error if empty while I(tsig_enabled) is I(true)."
                type: dict
                suboptions:
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
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
    fqdn:
        description:
            - "Zone FQDN. The FQDN supplied at creation will be converted to canonical form."
            - "Read-only after creation."
        type: str
    gss_tsig_enabled:
        description:
            - "I(gss_tsig_enabled) enables/disables GSS-TSIG signed dynamic updates."
            - "Defaults to I(false)."
        type: bool
    inheritance_sources:
        description:
            - "Optional. Inheritance configuration."
        type: dict
        suboptions:
            gss_tsig_enabled:
                description:
                    - "Optional. Field config for I(gss_tsig_enabled) field from I(AuthZone) object."
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
            notify:
                description:
                    - "Field config for I(notify) field from I(AuthZone) object."
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
            query_acl:
                description:
                    - "Optional. Field config for I(query_acl) field from I(AuthZone) object."
                type: dict
                suboptions:
                    action:
                        description:
                            - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                        type: str
            transfer_acl:
                description:
                    - "Optional. Field config for I(transfer_acl) field from I(AuthZone) object."
                type: dict
                suboptions:
                    action:
                        description:
                            - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                        type: str
            update_acl:
                description:
                    - "Optional. Field config for I(update_acl) field from I(AuthZone) object."
                type: dict
                suboptions:
                    action:
                        description:
                            - "Optional. Inheritance setting for a field. Defaults to I(inherit)."
                        type: str
            use_forwarders_for_subzones:
                description:
                    - "Optional. Field config for I(use_forwarders_for_subzones) field from I(AuthZone) object."
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
            zone_authority:
                description:
                    - "Optional. Field config for I(zone_authority) field from I(AuthZone) object."
                type: dict
                suboptions:
                    default_ttl:
                        description:
                            - "Optional. Field config for I(default_ttl) field from I(ZoneAuthority) object."
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
                    expire:
                        description:
                            - "Optional. Field config for I(expire) field from I(ZoneAuthority) object."
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
                    mname_block:
                        description:
                            - "Optional. Field config for I(mname) block from I(ZoneAuthority) object."
                        type: dict
                        suboptions:
                            action:
                                description:
                                    - "Defaults to I(inherit)."
                                type: str
                    negative_ttl:
                        description:
                            - "Optional. Field config for I(negative_ttl) field from I(ZoneAuthority) object."
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
                    protocol_rname:
                        description:
                            - "Optional. Field config for I(protocol_rname) field from I(ZoneAuthority) object."
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
                    refresh:
                        description:
                            - "Optional. Field config for I(refresh) field from I(ZoneAuthority) object."
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
                    retry:
                        description:
                            - "Optional. Field config for I(retry) field from I(ZoneAuthority) object."
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
                    rname:
                        description:
                            - "Optional. Field config for I(rname) field from I(ZoneAuthority) object."
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
    initial_soa_serial:
        description:
            - "On-create-only. SOA serial is allowed to be set when the authoritative zone is created."
        type: int
    internal_secondaries:
        description:
            - "Optional. BloxOne DDI hosts acting as internal secondaries. Order is not significant."
        type: list
        elements: dict
        suboptions:
            host:
                description:
                    - "The resource identifier."
                type: str
    notify:
        description:
            - "Also notify all external secondary DNS servers if enabled."
            - "Defaults to I(false)."
        type: bool
    nsgs:
        description:
            - "The resource identifier."
        type: list
        elements: str
    parent:
        description:
            - "The resource identifier."
        type: str
    primary_type:
        description:
            - "Primary type for an authoritative zone. Read only after creation. Allowed values:"
            - "* I(external): zone data owned by an external nameserver,"
            - "* I(cloud): zone data is owned by a BloxOne DDI host."
        type: str
    query_acl:
        description:
            - "Optional. Clients must match this ACL to make authoritative queries. Also used for recursive queries if that ACL is unset."
            - "Defaults to empty."
        type: list
        elements: dict
        suboptions:
            access:
                description:
                    - "Access permission for I(element)."
                    - "Allowed values:"
                    - "* I(allow),"
                    - "* I(deny)."
                type: str
            acl:
                description:
                    - "The resource identifier."
                type: str
            address:
                description:
                    - "Optional. Data for I(ip) I(element)."
                    - "Must be empty if I(element) is not I(ip)."
                type: str
            element:
                description:
                    - "Type of element."
                    - "Allowed values:"
                    - "* I(any),"
                    - "* I(ip),"
                    - "* I(acl),"
                    - "* I(tsig_key)."
                type: str
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Must be empty if I(element) is not I(tsig_key)."
                type: dict
                suboptions:
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
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
    tags:
        description:
            - "Tagging specifics."
        type: dict
    transfer_acl:
        description:
            - "Optional. Clients must match this ACL to receive zone transfers."
        type: list
        elements: dict
        suboptions:
            access:
                description:
                    - "Access permission for I(element)."
                    - "Allowed values:"
                    - "* I(allow),"
                    - "* I(deny)."
                type: str
            acl:
                description:
                    - "The resource identifier."
                type: str
            address:
                description:
                    - "Optional. Data for I(ip) I(element)."
                    - "Must be empty if I(element) is not I(ip)."
                type: str
            element:
                description:
                    - "Type of element."
                    - "Allowed values:"
                    - "* I(any),"
                    - "* I(ip),"
                    - "* I(acl),"
                    - "* I(tsig_key)."
                type: str
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Must be empty if I(element) is not I(tsig_key)."
                type: dict
                suboptions:
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
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
    update_acl:
        description:
            - "Optional. Specifies which hosts are allowed to submit Dynamic DNS updates for authoritative zones of I(primary_type) I(cloud)."
            - "Defaults to empty."
        type: list
        elements: dict
        suboptions:
            access:
                description:
                    - "Access permission for I(element)."
                    - "Allowed values:"
                    - "* I(allow),"
                    - "* I(deny)."
                type: str
            acl:
                description:
                    - "The resource identifier."
                type: str
            address:
                description:
                    - "Optional. Data for I(ip) I(element)."
                    - "Must be empty if I(element) is not I(ip)."
                type: str
            element:
                description:
                    - "Type of element."
                    - "Allowed values:"
                    - "* I(any),"
                    - "* I(ip),"
                    - "* I(acl),"
                    - "* I(tsig_key)."
                type: str
            tsig_key:
                description:
                    - "Optional. TSIG key."
                    - "Must be empty if I(element) is not I(tsig_key)."
                type: dict
                suboptions:
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
                    comment:
                        description:
                            - "Comment for TSIG key."
                        type: str
                    key:
                        description:
                            - "The resource identifier."
                        type: str
                    name:
                        description:
                            - "TSIG key name, FQDN."
                        type: str
                    secret:
                        description:
                            - "TSIG key secret, base64 string."
                        type: str
    use_forwarders_for_subzones:
        description:
            - "Optional. Use default forwarders to resolve queries for subzones."
            - "Defaults to I(true)."
        type: bool
    view:
        description:
            - "The resource identifier."
        type: str
        required: true
    zone_authority:
        description:
            - "Optional. ZoneAuthority."
        type: dict
        suboptions:
            default_ttl:
                description:
                    - "Optional. ZoneAuthority default ttl for resource records in zone (value in seconds)."
                    - "Defaults to 28800."
                type: int
            expire:
                description:
                    - "Optional. ZoneAuthority expire time in seconds."
                    - "Defaults to 2419200."
                type: int
            mname:
                description:
                    - "Defaults to empty."
                type: str
            negative_ttl:
                description:
                    - "Optional. ZoneAuthority negative caching (minimum) ttl in seconds."
                    - "Defaults to 900."
                type: int
            refresh:
                description:
                    - "Optional. ZoneAuthority refresh."
                    - "Defaults to 10800."
                type: int
            retry:
                description:
                    - "Optional. ZoneAuthority retry."
                    - "Defaults to 3600."
                type: int
            rname:
                description:
                    - "Optional. ZoneAuthority rname."
                    - "Defaults to empty."
                type: str
            use_default_mname:
                description:
                    - "Optional. Use default value for master name server."
                    - "Defaults to true."
                type: bool

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create an Auth Zone
    infoblox.bloxone.dns_auth_zone:
      name: "example_zone"
      state: "present"

  - name: Create an Auth Zone with Additional Fields
    infoblox.bloxone.dns_auth_zone:
      name: "example_zone"
      comment: "Example Auth Zone"
      query_acl:
        - access: "allow"
          element: "ip"
          address: "192.168.11.11"
      gss_tsig_enabled: true
      notify: true
      state: "present"
      tags:
        location: "my-location"

  - name: Delete the Zone
    infoblox.bloxone.dns_auth_zone:
      name: "example_zone"
      state: "absent"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the AuthZone object
    type: str
    returned: Always
item:
    description:
        - AuthZone object
    type: complex
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
    from dns_config import AuthZone, AuthZoneApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class AuthZoneModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(AuthZoneModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = AuthZone.from_dict(self._payload_params)
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
                resp = AuthZoneApi(self.client).read(self.params["id"], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"fqdn=='{self.params['fqdn']}' and view=='{self.params['view']}'"
            resp = AuthZoneApi(self.client).list(filter=filter, inherit="full")
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple AuthZone: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = AuthZoneApi(self.client).create(body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["fqdn", "primary_type", "view"])

        resp = AuthZoneApi(self.client).update(id=self.existing.id, body=update_body, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        AuthZoneApi(self.client).delete(self.existing.id)

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
                result["msg"] = "AuthZone created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "AuthZone updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "AuthZone deleted"

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
        comment=dict(type="str"),
        disabled=dict(type="bool"),
        external_primaries=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
                nsg=dict(type="str"),
                tsig_enabled=dict(type="bool"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
                type=dict(type="str"),
            ),
        ),
        external_secondaries=dict(
            type="list",
            elements="dict",
            options=dict(
                address=dict(type="str"),
                fqdn=dict(type="str"),
                stealth=dict(type="bool"),
                tsig_enabled=dict(type="bool"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
            ),
        ),
        fqdn=dict(type="str"),
        gss_tsig_enabled=dict(type="bool"),
        inheritance_sources=dict(
            type="dict",
            options=dict(
                gss_tsig_enabled=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                notify=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                query_acl=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                transfer_acl=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                update_acl=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                use_forwarders_for_subzones=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
                zone_authority=dict(
                    type="dict",
                    options=dict(
                        default_ttl=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        expire=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        mname_block=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        negative_ttl=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        protocol_rname=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        refresh=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        retry=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                        rname=dict(
                            type="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        initial_soa_serial=dict(type="int"),
        internal_secondaries=dict(
            type="list",
            elements="dict",
            options=dict(
                host=dict(type="str"),
            ),
        ),
        notify=dict(type="bool"),
        nsgs=dict(type="list", elements="str"),
        parent=dict(type="str"),
        primary_type=dict(type="str"),
        query_acl=dict(
            type="list",
            elements="dict",
            options=dict(
                access=dict(type="str"),
                acl=dict(type="str"),
                address=dict(type="str"),
                element=dict(type="str"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
            ),
        ),
        tags=dict(type="dict"),
        transfer_acl=dict(
            type="list",
            elements="dict",
            options=dict(
                access=dict(type="str"),
                acl=dict(type="str"),
                address=dict(type="str"),
                element=dict(type="str"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
            ),
        ),
        update_acl=dict(
            type="list",
            elements="dict",
            options=dict(
                access=dict(type="str"),
                acl=dict(type="str"),
                address=dict(type="str"),
                element=dict(type="str"),
                tsig_key=dict(
                    type="dict",
                    no_log=True,
                    options=dict(
                        algorithm=dict(type="str"),
                        comment=dict(type="str"),
                        key=dict(type="str", no_log=True),
                        name=dict(type="str"),
                        secret=dict(type="str", no_log=True),
                    ),
                ),
            ),
        ),
        use_forwarders_for_subzones=dict(type="bool"),
        view=dict(type="str", required=True),
        zone_authority=dict(
            type="dict",
            options=dict(
                default_ttl=dict(type="int"),
                expire=dict(type="int"),
                mname=dict(type="str"),
                negative_ttl=dict(type="int"),
                refresh=dict(type="int"),
                retry=dict(type="int"),
                rname=dict(type="str"),
                use_default_mname=dict(type="bool"),
            ),
        ),
    )

    module = AuthZoneModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["fqdn", "primary_type", "view"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
