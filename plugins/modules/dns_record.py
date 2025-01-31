#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: dns_record
short_description: Manage DNS Resource Record
description:
    - Manage DNS Resource Record
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
            - "The description for the DNS resource record. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    disabled:
        description:
            - "Indicates if the DNS resource record is disabled. A disabled object is effectively non-existent when generating configuration."
            - "Defaults to I(false)."
        type: bool
    inheritance_sources:
        description:
            - "The inheritance configuration of the Record."
        type: dict
        suboptions:
            ttl:
                description: "The TTL inheritance settings for the record. If not set, the record will inherit the TTL from the zone."
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
    name_in_zone:
        description:
            - "The relative owner name to the zone origin. Must be specified for creating the DNS resource record and is read only for other operations."
        type: str
        default: ""
    options:
        description:
            - "The DNS resource record type-specific non-protocol options."
        suboptions:
            address:
                description: 
                    - "For GET operation it contains the IPv4 or IPv6 address represented by the PTR record."
                    - "For POST and PATCH operations it can be used to create/update a PTR record based on the IP address it represents."
                    - "In this case, in addition to the I(address) in the options field, need to specify the I(view) field."
                    - "Applicable for Pointer records."
                type: bool
            create_ptr:
                description: 
                    - "A boolean flag which can be set to I(true) for POST operation to automatically create the corresponding PTR record."
                type: bool
            check_rmz:
                description: 
                    - "A boolean flag which can be set to I(true) for POST operation to check the existence of reverse zone for creating the corresponding PTR record."
                    - "Only applicable if the I(create_ptr) option is set to I(true)."
                type: bool
        type: dict
    rdata:
        description:
            - "The DNS resource record data in JSON format. Certain DNS resource record-specific subfields are required for creating the DNS resource record."
        suboptions: 
            address:
                description: 
                    - "For B(A) Record, the IPv4 address of the host."
                    - "For B(AAAA) Record, the IPv6 address of the host."
                type: str
                required: true
            flags:
                description: 
                    - "For B(CAA) record, it is an unsigned 8-bit integer which specifies the CAA record flags. RFC 6844 defines one (highest) bit in flag octet, remaining bits are deferred for future use. This bit is referenced as Critical. When the bit is set (flag value == 128), issuers must not issue certificates in case CAA records contain unknown property tags."
                    - " Defaults to 0."
                    - "For B(NAPTR) record, a character string containing flags to control aspects of the rewriting and interpretation of the fields in the DNS resource record. The flags that are currently used are:" 
                    - "B(U): Indicates that the output maps to a URI (Uniform Record Identifier)." 
                    - "B(S): Indicates that the output is a domain name that has at least one SRV record. The DNS client must then send a query for the SRV record of the resulting domain name."
                    - "B(A): Indicates that the output is a domain name that has at least one A or AAAA record. The DNS client must then send a query for the A or AAAA record of the resulting domain name."
                    - "B(P): Indicates that the protocol specified in the services field defines the next step or phase."
                type: str
                required: false
            dname:
                description: 
                    - "For B(NS) Record, a domain-name which specifies a host which should be authoritative for the specified class and domain. Can be absolute or relative domain name and include UTF-8" 
                    - "For B(PTR) Record, a domain name which points to some location in the domain name space. Can be absolute or relative domain name and include UTF-8."  
                type: str
                required: true
            preference:
                description: 
                    - "For B(MX) record, an unsigned 16-bit integer which specifies the preference given to this RR among others at the same owner. Lower values are preferred. The range of the value is 0 to 65535."
                    - "For B(NAPTR) record, a 16-bit unsigned integer that specifies the order in which NAPTR records with equal 'order' values should be processed, low numbers being processed before high numbers. This is similar to the preference field in an MX record, and is used so domain administrators can direct clients towards more capable hosts or lighter weight protocols. A client may look at records with higher preference values if it has a good reason to do so such as not understanding the preferred protocol or service. The range of the value is 0 to 65535."
                type: int
                required: true
            tag: 
                description: 
                    - "For B(CAA) record, the CAA record property tag string which indicates the type of CAA record. The following property tags are defined by RFC 6844:"
                    - "I(issue): Used to explicitly authorize CA to issue certificates for the domain in which the property is published."
                    - "I(issuewild): Used to explicitly authorize a single CA to issue wildcard certificates for the domain in which the property is published."
                    - "I(iodef): Used to specify an email address or URL to report invalid certificate requests or issuers' certificate policy violations."
                    - "Note: I(issuewild) type takes precedence over I(issue)."
                type: str
                required: true
            value:
                description: 
                    - "For B(CAA) record, a string which contains the CAA record property value."
                    - "Specifies the CA who is authorized to issue a certificate for the domain if the CAA record property tag is I(issue) or I(issuewild)."
                    - "Specifies the URL/email address to report CAA policy violation for the domain if the CAA record property tag is I(iodef)."
                    - "For B(Generic record), it is a string representing the value for the sub-subfield."
                type: str
                required: true
            cname:
                description: 
                    - "For B(CNAME) record, a domain name which specifies the canonical or primary name for the owner. The owner name is an alias. Can be empty."
                type: str
                required: true
            target:
                description: 
                    - "For B(DNAME) record, the target domain name to which the zone will be mapped. Can be empty."
                    - "For B(SRV) record, the domain name of the target host. There must be one or more address records for this name, the name must not be an alias (in the sense of RFC 1034 or RFC 2181)."
                type: str
                required: true
            dhcid:
                description: 
                    - "For B(DHCID) record, the Base64 encoded string which contains DHCP client information."
                type: str
                required: true
            exchange:
                description: 
                    - "For B(MX) record, a domain name which specifies a host willing to act as a mail exchange for the owner name."
                type: str
                required: true
            order:
                description: 
                    - "For B(NAPTR) record, a 16-bit unsigned integer specifying the order in which the NAPTR records must be processed. Low numbers are processed before high numbers, and once a NAPTR is found whose rule \"matches\" the target, the client must not consider any NAPTRs with a higher value for order (except as noted below for the \"flags\" field. The range of the value is 0 to 65535."
                type: int
                required: true
            regexp:
                description:
                    - "For B(NAPTR) record, a string containing a substitution expression that is applied to the original string held by the client in order to construct the next domain name to lookup."
                    - "Defaults to none."
                type: str
                required: false
            replacement:
                description:
                    - "For B(NAPTR) record, the next name to query for NAPTR, SRV, or address records depending on the value of the I(flags) field. This can be an absolute or relative domain name. Can be empty."
                type: str
                required: true
            services:
                description:
                    - "For B(NAPTR) record, specifies the service(s) available down this rewrite path. It may also specify the particular protocol that is used to talk with a service. A protocol must be specified if the flags field states that the NAPTR is terminal. If a protocol is specified, but the flags field does not state that the NAPTR is terminal, the next lookup must be for a NAPTR. The client may choose not to perform the next lookup if the protocol is unknown, but that behavior must not be relied upon."
                    - "The service field may take any of the values below (using the Augmented BNF of RFC 2234):"
                    - V(service_field = [ [protocol] *("+" rs\)])
                    - V(protocol = ALPHA * 31 ALPHANUM)
                    - V(rs = ALPHA * 31 ALPHANUM)
                    - "The protocol and rs fields are limited to 32 characters and must start with an alphabetic character."
                    - "For example, an optional protocol specification followed by 0 or more resolution services. Each resolution service is indicated by an initial '+' character."
                    - "Note that the empty string is also a valid service field.  This will typically be seen at the beginning of a series of rules, when it is impossible to know what services and protocols will be offered by a particular service."
                    - "The actual format of the service request and response will be determined by the resolution protocol. Protocols need not offer all services.The labels for service requests shall be formed from the set of characters [A-Z0-9]. The case of the alphabetic characters is not significant."
                type: str
                required: true
            expire:
                description:
                    - "For B(SOA) record, the time interval in seconds after which zone data will expire and secondary server stops answering requests for the zone."
                type: int
                required: false
            mname:
                description:
                    - "For B(SOA) record, the domain name for the master server for the zone. Can be absolute or relative domain name."
                type: str
                required: true
            negative_ttl:
                description:
                    - "For B(SOA) record, the time interval in seconds for which name servers can cache negative responses for zone." 
                    -  "Defaults to 900 seconds (15 minutes)."
                type: int
                required: false
            refresh:
                description:
                    - "For B(SOA) record, the time interval in seconds that specifies how often secondary servers need to send a message to the primary server for a zone to check that their data is current, and retrieve fresh data if it is not." 
                    - "Defaults to 10800 seconds (3 hours)."
                type: int
                required: false
            retry:
                description:
                    - "For B(SOA) record, the time interval in seconds for which the secondary server will wait before attempting to recontact the primary server after a connection failure occurs." 
                    - "Defaults to 3600 seconds (1 hour)."
                type: int
                required: false
            rname:
                description:
                    - "For B(SOA) record, the domain name which specifies the mailbox of the person responsible for this zone."
                type: str
                required: false
            serial:
                description:
                    - "For B(SOA) record, an unsigned 32-bit integer that specifies the serial number of the zone. Used to indicate that zone data was updated, so the secondary name server can initiate zone transfer. The range of the value is 0 to 4294967295."
                type: int
                required: false
            port:
                description:
                    - "For B(SRV) record, an unsigned 16-bit integer which specifies the port on this target host of this service. The range of the value is 0 to 65535. This is often as specified in Assigned Numbers but need not be."
                type: int
                required: true
            priority:
                description:
                    - "For B(SRV) record, an unsigned 16-bit integer which specifies the priority of this target host. The range of the value is 0 to 65535. A client must attempt to contact the target host with the lowest-numbered priority it can reach. Target hosts with the same priority should be tried in an order defined by the I(weight) field."
                type: int
                required: true
            weight:
                description:
                    - "For B(SRV) record, an unsigned 16-bit integer which specifies a relative weight for entries with the same priority. The range of the value is 0 to 65535."
                    - "Larger weights should be given a proportionately higher probability of being selected. Domain administrators should use weight 0 when there is not any server selection to do, to make the RR easier to read for humans (less noisy). In the presence of records containing weights greater than 0, records with weight 0 should have a very small chance of being selected."
                    - "In the absence of a protocol whose specification calls for the use of other weighting information, a client arranges the SRV RRs of the same priority in the order in which target hosts, specified by the SRV RRs, will be contacted."
                    -  "Defaults to 0."
                type: int
                required: false
            text:
                description:
                    - "For B(TXT) record, the semantics of the text depends on the domain where it is found."
                type: str
                required: true
            type:
                description: 
                    - "For B(Generic record), the following types are supported:"
                    - "8BIT: Unsigned 8-bit integer."
                    - "16BIT: Unsigned 16-bit integer."
                    - "32BIT: Unsigned 32-bit integer."
                    - "IPV6: IPv6 address. For example, \"abcd:123::abcd\"."
                    - "IPV4: IPv4 address. For example, \"1.1.1.1\"."
                    - "DomainName: Domain name (absolute or relative)."
                    - "TEXT: ASCII text."
                    - "BASE64: Base64 encoded binary data."
                    - "HEX: Hex encoded binary data."
                    - "PRESENTATION: Presentation is a standard textual form of record data, as shown in a standard master zone file."
                    - "For example, an IPSEC RDATA could be specified using the PRESENTATION type field whose value is V(\"10 1 2 192.0.2.38 AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\"), instead of a sequence of the following subfields:"
                    - "8BIT: value=10"
                    - "8BIT: value=1"
                    - "8BIT: value=2"
                    - "IPV4: value=\"192.0.2.38\""
                    - "BASE64 (without length_kind sub-subfield): value=\"AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\""
                    - "If type is PRESENTATION, only one struct subfield can be specified."
                type: str
                required: true
            length_kind:
                description:
                    - "For B(Generic record), a string indicating the size in bits of a sub-subfield that is prepended to the value and encodes the length of the value."
                    - "Valid values are:"
                    - "8: If type is ASCII or BASE64."
                    - "16: If type is HEX."
                    - "Defaults to none."
                    - "B(Required only for few types.)"
                type: str
                required: false                            
        type: dict
        required: true
    tags:
        description:
            - "The tags for the DNS resource record in JSON format."
        type: dict
    ttl:
        description:
            - "The record time to live value in seconds. The range of this value is 0 to 2147483647."
            - "Defaults to TTL value from the SOA record of the zone."
        type: int
    type:
        description:
          - "The DNS resource record type specified in the textual mnemonic format or in the \"TYPEnnn\" format where \"nnn\" indicates the numeric type value."
          - V(Value      | Numeric Type  |   Description)
          - V(A          |       1       |   Address record)
          - V(AAAA       |      28       |   IPv6 Address record)
          - V(CAA        |     257       |   Certification Authority Authorization record)
          - V(CNAME      |       5       |   Canonical Name record)
          - V(DNAME      |      39       |   Delegation Name record)
          - V(DHCID      |      49       |   DHCP Identifier record)
          - V(HTTPS      |      65       |   HTTPS Record)
          - V(MX         |      15       |   Mail Exchanger record)
          - V(NAPTR      |      35       |   Naming Authority Pointer record)
          - V(NS         |       2       |   Name Server record)
          - V(PTR        |      12       |   Pointer record)
          - V(SOA        |       6       |   Start of Authority record)
          - V(SRV        |      33       |   Service record)
          - V(SVCB       |      64       |   Service Binding Record)
          - V(TXT        |      16       |   Text record)
          - V(IBMETA     |   65536       |   Infoblox meta records, not valid for DNS protocol (read-only\))
        type: str
        required: true
    zone:
        description:
            - "The resource identifier."
        type: str
        required: true

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
    - name: Create a View (required as parent)
      infoblox.bloxone.dns_view:
        name: "{{ dns_view_name }}"
        state: present
      register: _view 
        
    - name: Create an Auth Zone (required as parent) 
      infoblox.bloxone.dns_auth_zone:
        fqdn: "example_zone"
        primary_type: "cloud"
        view: "{{ _view.id }}"
        state: "present"
      register: _auth_zone
    
    - name: Create an A Record in an Auth Zone
      infoblox.bloxone.dns_record:
        zone: "{{ _auth_zone.id }}"
        comment: "Example A Record"
        rdata:
            address: "192.168.10.10"
        type: "A"
        state: "present"        
        
    - name: Create an A Record with Name in Zone and Zone
      infoblox.bloxone.dns_record:
        zone: "{{ _auth_zone.id }}"
        name_in_zone: "example_a_record"
        comment: "Example A Record"
        ttl: 3600
        disabled: true
        rdata:  
            address: "192.168.10.10"
        type: "A"
        tags:
            location: "site-1"
        state: "present"
        
    - name: Delete the A Record
      infoblox.bloxone.dns_record:
        zone: "{{ _auth_zone.id }}"
        name_in_zone: "example_a_record"
        rdata:
            address: "192.168.10.10"
        type: "A"
        state: "absent"
"""  # noqa: E501

RETURN = r"""
id:
    description:
        - ID of the Record object
    type: str
    returned: Always
item:
    description:
        - Record object
    type: complex
    returned: Always
    contains:
        absolute_name_spec:
            description:
                - "Synthetic field, used to determine I(zone) and/or I(name_in_zone) field for records."
            type: str
            returned: Always
        absolute_zone_name:
            description:
                - "The absolute domain name of the zone where this record belongs."
            type: str
            returned: Always
        comment:
            description:
                - "The description for the DNS resource record. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        created_at:
            description:
                - "The timestamp when the object has been created."
            type: str
            returned: Always
        delegation:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        disabled:
            description:
                - "Indicates if the DNS resource record is disabled. A disabled object is effectively non-existent when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        dns_absolute_name_spec:
            description:
                - "The DNS protocol textual representation of I(absolute_name_spec)."
            type: str
            returned: Always
        dns_absolute_zone_name:
            description:
                - "The DNS protocol textual representation of the absolute domain name of the zone where this record belongs."
            type: str
            returned: Always
        dns_name_in_zone:
            description:
                - "The DNS protocol textual representation of the relative owner name for the DNS zone."
            type: str
            returned: Always
        dns_rdata:
            description:
                - "The DNS protocol textual representation of the DNS resource record data."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The inheritance configuration of the Record"
            type: dict
            returned: Always
            contains:
                ttl:
                    description: "The TTL inheritance settings for the record. If not set, the record will inherit the TTL from the zone."
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
        ipam_host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        name_in_zone:
            description:
                - "The relative owner name to the zone origin. Must be specified for creating the DNS resource record and is read only for other operations."
            type: str
            returned: Always
        options:
            description:
                - "The DNS resource record type-specific non-protocol options."
            contains:
                address:
                    description: 
                        - "For GET operation it contains the IPv4 or IPv6 address represented by the PTR record."
                        - "For POST and PATCH operations it can be used to create/update a PTR record based on the IP address it represents."
                        - "In this case, in addition to the I(address) in the options field, need to specify the I(view) field."
                        - "Applicable for Pointer records."
                    type: bool
                    returned: Always
                create_ptr:
                    description: 
                        - "A boolean flag which can be set to I(true) for POST operation to automatically create the corresponding PTR record."
                    type: bool
                    returned: Always
                check_rmz:
                    description: 
                        - "A boolean flag which can be set to I(true) for POST operation to check the existence of reverse zone for creating the corresponding PTR record."
                        - "Only applicable if the I(create_ptr) option is set to I(true)."
                    type: bool
                    returned: Always
            type: dict
        provider_metadata:
            description:
                - "external DNS provider metadata."
            type: dict
            returned: Always
        rdata:
            description:
                - "The DNS resource record data in JSON format. Certain DNS resource record-specific subfields are required for creating the DNS resource record."
            contains: 
                address:
                    description: 
                        - "For B(A) Record, the IPv4 address of the host."
                        - "For B(AAAA) Record, the IPv6 address of the host."
                    type: str
                    returned: Always
                flags:
                    description: 
                        - "For B(CAA) record, it is an unsigned 8-bit integer which specifies the CAA record flags. RFC 6844 defines one (highest) bit in flag octet, remaining bits are deferred for future use. This bit is referenced as Critical. When the bit is set (flag value == 128), issuers must not issue certificates in case CAA records contain unknown property tags."
                        - " Defaults to 0."
                        - "For B(NAPTR) record, a character string containing flags to control aspects of the rewriting and interpretation of the fields in the DNS resource record. The flags that are currently used are:" 
                        - "B(U): Indicates that the output maps to a URI (Uniform Record Identifier)." 
                        - "B(S): Indicates that the output is a domain name that has at least one SRV record. The DNS client must then send a query for the SRV record of the resulting domain name."
                        - "B(A): Indicates that the output is a domain name that has at least one A or AAAA record. The DNS client must then send a query for the A or AAAA record of the resulting domain name."
                        - "B(P): Indicates that the protocol specified in the services field defines the next step or phase."
                    type: str
                    returned: Always
                dname:
                    description: 
                        - "For B(NS) Record, a domain-name which specifies a host which should be authoritative for the specified class and domain. Can be absolute or relative domain name and include UTF-8" 
                        - "For B(PTR) Record, a domain name which points to some location in the domain name space. Can be absolute or relative domain name and include UTF-8."  
                    type: str
                    returned: Always
                preference:
                    description: 
                        - "For B(MX) record, an unsigned 16-bit integer which specifies the preference given to this RR among others at the same owner. Lower values are preferred. The range of the value is 0 to 65535."
                        - "For B(NAPTR) record, a 16-bit unsigned integer that specifies the order in which NAPTR records with equal 'order' values should be processed, low numbers being processed before high numbers. This is similar to the preference field in an MX record, and is used so domain administrators can direct clients towards more capable hosts or lighter weight protocols. A client may look at records with higher preference values if it has a good reason to do so such as not understanding the preferred protocol or service. The range of the value is 0 to 65535."
                    type: int
                    returned: Always
                tag: 
                    description: 
                        - "For B(CAA) record, the CAA record property tag string which indicates the type of CAA record. The following property tags are defined by RFC 6844:"
                        - "I(issue): Used to explicitly authorize CA to issue certificates for the domain in which the property is published."
                        - "I(issuewild): Used to explicitly authorize a single CA to issue wildcard certificates for the domain in which the property is published."
                        - "I(iodef): Used to specify an email address or URL to report invalid certificate requests or issuers' certificate policy violations."
                        - "Note: I(issuewild) type takes precedence over I(issue)."
                    type: str
                    returned: Always
                value:
                    description: 
                        - "For B(CAA) record, a string which contains the CAA record property value."
                        - "Specifies the CA who is authorized to issue a certificate for the domain if the CAA record property tag is I(issue) or I(issuewild)."
                        - "Specifies the URL/email address to report CAA policy violation for the domain if the CAA record property tag is I(iodef)."
                        - "For B(Generic record), it is a string representing the value for the sub-subfield."
                    type: str
                    returned: Always
                cname:
                    description: 
                        - "For B(CNAME) record, a domain name which specifies the canonical or primary name for the owner. The owner name is an alias. Can be empty."
                    type: str
                    returned: Always
                target:
                    description: 
                        - "For B(DNAME) record, the target domain name to which the zone will be mapped. Can be empty."
                        - "For B(SRV) record, the domain name of the target host. There must be one or more address records for this name, the name must not be an alias (in the sense of RFC 1034 or RFC 2181)."
                    type: str
                    returned: Always
                dhcid:
                    description: 
                        - "For B(DHCID) record, the Base64 encoded string which contains DHCP client information."
                    type: str
                    returned: Always
                exchange:
                    description: 
                        - "For B(MX) record, a domain name which specifies a host willing to act as a mail exchange for the owner name."
                    type: str
                    returned: Always
                order:
                    description: 
                        - "For B(NAPTR) record, a 16-bit unsigned integer specifying the order in which the NAPTR records must be processed. Low numbers are processed before high numbers, and once a NAPTR is found whose rule \"matches\" the target, the client must not consider any NAPTRs with a higher value for order (except as noted below for the \"flags\" field. The range of the value is 0 to 65535."
                    type: int
                    returned: Always
                regexp:
                    description:
                        - "For B(NAPTR) record, a string containing a substitution expression that is applied to the original string held by the client in order to construct the next domain name to lookup."
                        - "Defaults to none."
                    type: str
                    returned: Always
                replacement:
                    description:
                        - "For B(NAPTR) record, the next name to query for NAPTR, SRV, or address records depending on the value of the I(flags) field. This can be an absolute or relative domain name. Can be empty."
                    type: str
                    returned: Always
                services:
                    description:
                        - "For B(NAPTR) record, specifies the service(s) available down this rewrite path. It may also specify the particular protocol that is used to talk with a service. A protocol must be specified if the flags field states that the NAPTR is terminal. If a protocol is specified, but the flags field does not state that the NAPTR is terminal, the next lookup must be for a NAPTR. The client may choose not to perform the next lookup if the protocol is unknown, but that behavior must not be relied upon."
                        - "The service field may take any of the values below (using the Augmented BNF of RFC 2234):"
                        - V(service_field = [ [protocol] *("+" rs\)])
                        - V(protocol = ALPHA * 31 ALPHANUM)
                        - V(rs = ALPHA * 31 ALPHANUM)
                        - "The protocol and rs fields are limited to 32 characters and must start with an alphabetic character."
                        - "For example, an optional protocol specification followed by 0 or more resolution services. Each resolution service is indicated by an initial '+' character."
                        - "Note that the empty string is also a valid service field.  This will typically be seen at the beginning of a series of rules, when it is impossible to know what services and protocols will be offered by a particular service."
                        - "The actual format of the service request and response will be determined by the resolution protocol. Protocols need not offer all services.The labels for service requests shall be formed from the set of characters [A-Z0-9]. The case of the alphabetic characters is not significant."
                    type: str
                    returned: Always
                expire:
                    description:
                        - "For B(SOA) record, the time interval in seconds after which zone data will expire and secondary server stops answering requests for the zone."
                    type: int
                    returned: Always
                mname:
                    description:
                        - "For B(SOA) record, the domain name for the master server for the zone. Can be absolute or relative domain name."
                    type: str
                    returned: Always
                negative_ttl:
                    description:
                        - "For B(SOA) record, the time interval in seconds for which name servers can cache negative responses for zone." 
                        -  "Defaults to 900 seconds (15 minutes)."
                    type: int
                    returned: Always
                refresh:
                    description:
                        - "For B(SOA) record, the time interval in seconds that specifies how often secondary servers need to send a message to the primary server for a zone to check that their data is current, and retrieve fresh data if it is not." 
                        - "Defaults to 10800 seconds (3 hours)."
                    type: int
                    returned: Always
                retry:
                    description:
                        - "For B(SOA) record, the time interval in seconds for which the secondary server will wait before attempting to recontact the primary server after a connection failure occurs." 
                        - "Defaults to 3600 seconds (1 hour)."
                    type: int
                    returned: Always
                rname:
                    description:
                        - "For B(SOA) record, the domain name which specifies the mailbox of the person responsible for this zone."
                    type: str
                    returned: Always
                serial:
                    description:
                        - "For B(SOA) record, an unsigned 32-bit integer that specifies the serial number of the zone. Used to indicate that zone data was updated, so the secondary name server can initiate zone transfer. The range of the value is 0 to 4294967295."
                    type: int
                    returned: Always
                port:
                    description:
                        - "For B(SRV) record, an unsigned 16-bit integer which specifies the port on this target host of this service. The range of the value is 0 to 65535. This is often as specified in Assigned Numbers but need not be."
                    type: int
                    returned: Always
                priority:
                    description:
                        - "For B(SRV) record, an unsigned 16-bit integer which specifies the priority of this target host. The range of the value is 0 to 65535. A client must attempt to contact the target host with the lowest-numbered priority it can reach. Target hosts with the same priority should be tried in an order defined by the I(weight) field."
                    type: int
                    returned: Always
                weight:
                    description:
                        - "For B(SRV) record, an unsigned 16-bit integer which specifies a relative weight for entries with the same priority. The range of the value is 0 to 65535."
                        - "Larger weights should be given a proportionately higher probability of being selected. Domain administrators should use weight 0 when there is not any server selection to do, to make the RR easier to read for humans (less noisy). In the presence of records containing weights greater than 0, records with weight 0 should have a very small chance of being selected."
                        - "In the absence of a protocol whose specification calls for the use of other weighting information, a client arranges the SRV RRs of the same priority in the order in which target hosts, specified by the SRV RRs, will be contacted."
                        -  "Defaults to 0."
                    type: int
                    returned: Always
                text:
                    description:
                        - "For B(TXT) record, the semantics of the text depends on the domain where it is found."
                    type: str
                    returned: Always
                type:
                    description: 
                        - "For B(Generic record), the following types are supported:"
                        - "8BIT: Unsigned 8-bit integer."
                        - "16BIT: Unsigned 16-bit integer."
                        - "32BIT: Unsigned 32-bit integer."
                        - "IPV6: IPv6 address. For example, \"abcd:123::abcd\"."
                        - "IPV4: IPv4 address. For example, \"1.1.1.1\"."
                        - "DomainName: Domain name (absolute or relative)."
                        - "TEXT: ASCII text."
                        - "BASE64: Base64 encoded binary data."
                        - "HEX: Hex encoded binary data."
                        - "PRESENTATION: Presentation is a standard textual form of record data, as shown in a standard master zone file."
                        - "For example, an IPSEC RDATA could be specified using the PRESENTATION type field whose value is V(\"10 1 2 192.0.2.38 AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\"), instead of a sequence of the following subfields:"
                        - "8BIT: value=10"
                        - "8BIT: value=1"
                        - "8BIT: value=2"
                        - "IPV4: value=\"192.0.2.38\""
                        - "BASE64 (without length_kind sub-subfield): value=\"AQNRU3mG7TVTO2BkR47usntb102uFJtugbo6BSGvgqt4AQ==\""
                        - "If type is PRESENTATION, only one struct subfield can be specified."
                    type: str
                    returned: Always
                length_kind:
                    description:
                        - "For B(Generic record), a string indicating the size in bits of a sub-subfield that is prepended to the value and encodes the length of the value."
                        - "Valid values are:"
                        - "8: If type is ASCII or BASE64."
                        - "16: If type is HEX."
                        - "Defaults to none."
                        - "B(Required only for few types.)"
                    type: str
                    returned: Always           
            type: dict
        source:
            description:
                - "The DNS resource record type-specific non-protocol source. The source is a combination of indicators, each tracking how the DNS resource record appeared in the system. Listed below are source indicators with their meaning:"
            contains:
                STATIC:
                  description: 
                    - "Record was created manually by API call to I(dns/record). Valid for all record types except I(SOA)."
                  type: str
                  returned: Always
                SYSTEM:
                  description: 
                    - "Record was created automatically based on name server assignment. Valid for I(SOA), I(NS), I(A), I(AAAA), and I(PTR) record types."
                  type: str
                  returned: Always
                DYNAMIC:
                  description: 
                    - "Record was created dynamically by performing dynamic update. Valid for all record types except I(SOA)."
                  type: str
                  returned: Always
                DELEGATED:
                  description: 
                    - "Record was created automatically based on delegation servers assignment. Always extends the I(SYSTEM) bit. Valid for I(NS), I(A), I(AAAA), and I(PTR) record types."
                  type: str
                  returned: Always
                DTC:
                  description: 
                    - "Record was created automatically based on the DTC configuration. Always extends the I(SYSTEM) bit. Valid only for I(IBMETA) record type with I(LBDN) subtype."
                  type: str
                  returned: Always
                STATIC, SYSTEM:
                  description: 
                    - "Record was created manually by API call but it is obfuscated by record generated based on name server assignment."
                  type: str
                  returned: Always
                DYNAMIC, SYSTEM:
                  description: 
                    - "Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment."
                  type: str
                  returned: Always
                DELEGATED, SYSTEM:
                  description: 
                    - "Record was created automatically based on delegation servers assignment. I(SYSTEM) will always accompany I(DELEGATED)."
                  type: str
                  returned: Always
                DTC, SYSTEM:
                  description: 
                    - "Record was created automatically based on the DTC configuration. I(SYSTEM) will always accompany I(DTC)."
                  type: str
                  returned: Always
                STATIC, SYSTEM, DELEGATED:
                  description: 
                    - "Record was created manually by API call but it is obfuscated by record generated based on name server assignment as a result of creating a delegation."
                  type: str
                  returned: Always
                DYNAMIC, SYSTEM, DELEGATED:
                  description: 
                    - "Record was created dynamically by DDNS but it is obfuscated by record generated based on name server assignment as a result of creating a delegation."
                  type: str
                  returned: Always
            type: list
        subtype:
            description:
                - "The DNS resource record subtype specified in the textual mnemonic format. Valid only in case I(type) is I(IBMETA)."
                - V(Value      |  Numeric Type       |   Description)
                - V(  0        |  Default value      |               )
                - V(  1        |       1             |   LBDN record)
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the DNS resource record in JSON format."
            type: dict
            returned: Always
        ttl:
            description:
                - "The record time to live value in seconds. The range of this value is 0 to 2147483647."
                - "Defaults to TTL value from the SOA record of the zone."
            type: int
            returned: Always
        type:
            description:
              - "The DNS resource record type specified in the textual mnemonic format or in the \"TYPEnnn\" format where \"nnn\" indicates the numeric type value."
              - V(Value      | Numeric Type  |   Description)
              - V(A          |       1       |   Address record)
              - V(AAAA       |      28       |   IPv6 Address record)
              - V(CAA        |     257       |   Certification Authority Authorization record)
              - V(CNAME      |       5       |   Canonical Name record)
              - V(DNAME      |      39       |   Delegation Name record)
              - V(DHCID      |      49       |   DHCP Identifier record)
              - V(HTTPS      |      65       |   HTTPS Record)
              - V(MX         |      15       |   Mail Exchanger record)
              - V(NAPTR      |      35       |   Naming Authority Pointer record)
              - V(NS         |       2       |   Name Server record)
              - V(PTR        |      12       |   Pointer record)
              - V(SOA        |       6       |   Start of Authority record)
              - V(SRV        |      33       |   Service record)
              - V(SVCB       |      64       |   Service Binding Record)
              - V(TXT        |      16       |   Text record)
              - V(IBMETA     |   65536       |   Infoblox meta records, not valid for DNS protocol (read-only\))
            type: str
            returned: Always
        updated_at:
            description:
                - "The timestamp when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        view:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        view_name:
            description:
                - "The display name of the DNS view that contains the parent zone of the DNS resource record."
            type: str
            returned: Always
        zone:
            description:
                - "The resource identifier."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from dns_data import Record, RecordApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class RecordModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(RecordModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Record.from_dict(self._payload_params)
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
                resp = RecordApi(self.client).read(self.params["id"], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"zone=='{self.params['zone']}' and type=='{self.params['type']}' and name_in_zone=='{self.params['name_in_zone']}'"

            resp = RecordApi(self.client).list(filter=filter, inherit="full")

            if len(resp.results) == 0:
                return None

            for index, val in enumerate(resp.results):
                if getattr(val, "rdata") != self.params["rdata"]:
                    return resp.results.pop(index)

            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Record: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = RecordApi(self.client).create(body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["type", "zone"])

        resp = RecordApi(self.client).update(id=self.existing.id, body=update_body, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        RecordApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Record created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Record updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Record deleted"

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
        inheritance_sources=dict(
            type="dict",
            options=dict(
                ttl=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                    ),
                ),
            ),
        ),
        name_in_zone=dict(type="str", default=""),
        options=dict(type="dict"),
        rdata=dict(type="dict", required=True),
        tags=dict(type="dict"),
        ttl=dict(type="int"),
        type=dict(type="str", required=True),
        zone=dict(type="str", required=True),
    )

    module = RecordModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["rdata", "type", "zone"])],
        required_by={"name_in_zone": "zone"},
    )

    type = module.params["type"]
    name_in_zone = module.params["name_in_zone"]
    if type in ["CNAME", "NS", "PTR"] and not name_in_zone:
        module.fail_json(msg=f"'name_in_zone' is required for resource record 'type' '{type}'.")

    module.run_command()


if __name__ == "__main__":
    main()
