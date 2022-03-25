# Infoblox BloxOne Collection for Ansible

About 
=====
Infoblox BloxOne Ansible Collection (`infoblox.b1ddi_modules`) allows you to automate your DDI (DHCP, DNS and IPAM) objects hosted in the BloxOne platform. It thus enables the management of DDI objects using Ansibe automation. BloxOne ansible collection provides modules and plugins through which DDI objects can be read, created, updated and deleted. The collections also allows an organisation to integrate DDI automation into their IT automation framework. 

Requirements
============
 
- Ansible 2.10 and above
- Python 3.9

Collection Overview
===================

Modules
--------
The `infoblox.b1ddi_modules` collection has the following content:

DNS
----
- `b1_dns_view`: Module to create, update and delete DNS view
- `b1_dns_view_gather`: Module to get view information.
- `b1_dns_zone`: Module to create and delete DNS zone
- `b1_dns_zone_gather`: Module to get zone information.
- `b1_a_record`: Module to create and delete A record.
- `b1_a_record_gather`: Module to gather information about existing A records.
- `b1_cname_record`: Module to create and delete CNAME record
- `b1_cname_record_gather`: Module to gather information about existing CNAME records.
- `b1_ptr_record`: Module to create and delete PTR record
- `b1_ptr_record_gather`: Module to gather information about existing PTR records.
- `b1_ns_record`: Module to create and delete NS record
- `b1_ns_record_gather`: Module to gather information about existing ns records.

IPAM/DHCP
------

- `b1_ipam_ippace`: Module to create, update and delete an IPSpace in a BloxOne platform.
- `b1_ipam_ippace_gather`: Module to gather information about an existing IPSpace
- `b1_ipam_address_block`: Module to create, update and delete an Address Block in a BloxOne platform.
- `b1_ipam_address_block_gather`: Module to gather information about an existing Address Block.
- `b1_ipam_subnet`: Module to create, update and delete a subnet in BloxOne platform.
- `b1_ipam_subnet_gather`: Module to gather information about an existing subnets.
- `b1_ipam_range`: Module to create, update and delete a range in BloxOne platform.
- `b1_ipam_ipv4_reservation`: Module to create, update and delete a ipv4 reservation address in BloxOne platform.
- `b1_ipam_ipv4_reservation_gather`: Module to gather information about an ipv4 reservation address.
- `b1_ipam_fixed_address`: Module to create, update and delete a ipv4 fixed address in BloxOne platform.
- `b1_ipam_fixed_address_gather`: Module to gather information about an ipv4 fixed address. For instance mac-address of an address.

Plugins
----
- `lookup plugin`: Look up plugin to query a B1DDI objects via API

Installation
===========
The `b1ddi_modules` collection can be installed from git repository through either one way.

- Install the collection directly from the [GitHub](https://github.com/infobloxopen/bloxone-ansible/tree/main/ansible_collections/infoblox/b1ddi_modules) repository using the latest commit on the master branch:
```shell
ansible-galaxy collection install git+https://github.com/infobloxopen/bloxone-ansible#ansible_collections/infoblox/b1ddi_modules
```

- Install the collection by defining in requirements.yaml 
```shell
ansible-galaxy collection install -r requirement.yaml -p ./collections
```
The following example requirements.yaml
```yaml
---
collections:
  - name: git@github.com:infobloxopen/bloxone-ansible.git#ansible_collections/infoblox/b1ddi_modules
    type: git
    version: main

```
By default ansible will install the collection in `~/.ansible/collections`. Kindly create or update the `ansible.cfg` to install in the custom location.
```
[defaults]
collections_paths = ./collections
```
Playbooks
==================
Latest sample playbooks and examples are available at [playbooks](https://github.com/infobloxopen/bloxone-ansible/tree/main/sample_playbook).
 
Limitations
===========
Create operation is supported only for required fields.
Update operation is supported for selected fields.

Release
=====
Current Release - 1.0.1 on 02 October 2021

License
=======
This code is published under `GPL v3.0`

[COPYING](https://github.com/infobloxopen/infoblox-ansible/blob/master/COPYING) 
 
Author Information
==================
 Amit Mishra (amishra2@infoblox.com)
 Sriram Kanan (kannans@infoblox.com)
 Vedant Sethia 
 


