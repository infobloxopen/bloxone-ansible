# Infoblox BloxOne Collection for Ansible

The Infoblox BloxOne Collection (`infoblox.bloxone`) includes a variety of Ansible modules to help automate the management of BloxOne services. 

## Description 
Infoblox Universal DDI Modules for Ansible Collections facilitate the DNS and IPAM automation of VM workloads that are deployed across multiple platforms.
The bloxone_modules collection consists of modules and plug-ins required to manage the networks, IP addresses, and DNS records in universal DDI. The collection is hosted on Ansible Galaxy under infoblox.bloxone_modules.
## Version Information

### What's new in v2
- The collection has been renamed from `b1ddi_modules` to `Universal DDI`.
- The modules are renamed to follow the BloxOne API naming conventions. The old module names are deprecated and will be removed in the next major release.
- The modules are rewritten to use the [BloxOne Python client](https://github.com/infobloxopen/bloxone-python-client) library. This provides a more consistent experience across the modules and supports a wider range of BloxOne services.

## Collection Overview

### Modules
The `infoblox.bloxone` modules collection has the following content:

##### DNS
- `dns_view` : Module to create, update and delete DNS view.
- `dns_view_gather` : Module to get view information.
- `dns_zone` : Module to create and delete DNS zone.
- `dns_zone_gather` : Module to get zone information.
- `a_record` : Module to create and delete A record.
- `a_record_gather` : Module to gather information about existing A records.
- `cname_record` : Module to create and delete CNAME record
- `cname_record_gather` : Module to gather information about existing CNAME records.
- `ptr_record` : Module to create and delete PTR record
- `ptr_record_gather` : Module to gather information about existing PTR records.
- `ns_record` : Module to create and delete NS record
- `ns_record_gather` : Module to gather information about existing ns records.

##### IPAM/DHCP
- `ipam_ipspace` : Module to create, update and delete an IPSpace in a BloxOne platform.
- `ipam_ipspace_gather` : Module to gather information about an existing IPSpace
- `ipam_address_block` : Module to create, update and delete an Address Block in a BloxOne platform.
- `ipam_address_block_gather` : Module to gather information about an existing Address Block.
- `ipam_subnet` : Module to create, update and delete a subnet in BloxOne platform.
- `ipam_subnet_gather` : Module to gather information about an existing subnets.
- `ipam_range` : Module to create, update and delete a range in BloxOne platform.
- `ipam_address` : Module to create, update and delete an address in BloxOne platform.
- `ipam_address_gather` : Module to gather information about an address in BloxOne platform.
- `ipam_fixed_address` : Module to create, update and delete a ipv4 fixed address in BloxOne platform.
- `ipam_fixed_address_gather` : Module to gather information about an ipv4 fixed address. For instance mac-address of an address.
- `ipam_host_gather` : Module to gather information about an ipam host.
- `ipam_host` : Module to create, update and delete a ipam host in BloxOne platform.
- `ipam_host_gather` : Module to gather information about option space in B1DDI.
- `ipam_host` : Module to create, update and delete a option space in BloxOne platform.
- 
## Requirements
 
- ansible >= 2.15
- python >= 3.9
- requests >= 2.26.0
- bloxone-python-client >= 0.1.0

## Installation

The `infoblox.bloxone` collection can be installed from git repository.

```shell
ansible-galaxy collection install git+https://github.com/infobloxopen/bloxone-ansible.git,v2
```

The python dependencies are not installed by `ansible-galaxy`. They can be manually installed using the following command:

```shell
pip install requests
pip install git+https://github.com/infobloxopen/bloxone-python-client
```
By default ansible will install the collection in ~/.ansible/collections. Kindly create or update the ansible.cfg to install in the custom location.
```
[defaults]
collections_paths = ./collections
```
## Playbooks
Latest sample playbooks and examples are available at [playbooks](https://github.com/infobloxopen/bloxone-ansible/tree/v2/playbooks).
## Usage
### 1. Automated DNS View Management
**Description:** Automate the creation or deletion of DNS views for separating DNS configurations based on different network segments

**Example:**
```yaml
- name: Create a View
  infoblox.bloxone.dns_view:
    name: "example-view"
    state: present
```
### 2. Automated DNS Zone Management
**Description:** Create, delete, and manage DNS zones automatically based on changes in your network's domain requirements.
**Example:**
```yaml 
- name: Create an Auth Zone
  infoblox.bloxone.dns_auth_zone:
    fqdn: "example-auth-zone"
    primary_type: external
    view: "{{ _view.id }}"
    state: present
```

### 3. Automated DNS Record Management
**Description:** Automatically create, update, and delete DNS records in Universal DDI based on changes in your infrastructure.

**Example:**
```yaml
- name: Create a DNS A Record 
  infoblox.bloxone.dns_record:
    zone: "{{ _auth_zone.id }}"
    rdata:
      address: "192.168.10.10"
    type: "A"
    state: "present"
```

### 4. IP Address Management (IPAM)
**Description:** Automate the provisioning, updating, and de-provisioning of IP addresses in Universal DDI

**Example:**
```yaml
- name: "Create an IP space"
  infoblox.bloxone.ipam_ip_space:
      name: "example-ip-space"
      state: "present"
```
### 5. Address Block Management
Description: Create and delete address blocks within an IP space for IP address management.
**Example:**
```yaml
- name: "Create an Address Block"
  infoblox.bloxone.ipam_address_block:
    address: "10.0.0.0/16"
    space: "{{ ip_space.id }}"
    tags:
      location: "site-1"
    state: "present"
```

### 6. Subnet Management
Description: Create, update, and delete subnets within a specific address block.
```yaml
- name: "Create a subnet"
  infoblox.bloxone.ipam_subnet:
    address: "10.0.0.0/24"
    space: "{{ ip_space.id }}"
    state: "present"
```
TBW - Add usage examples

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Issues or RFEs

You can open an issue or request for enhancement [here](https://github.com/infobloxopen/bloxone-ansible/issues)
 


