# Infoblox BloxOne Collection for Ansible

The Infoblox BloxOne Collection (`infoblox.universal_ddi`) includes a variety of Ansible modules to help automate the management of BloxOne services. 

## Description 
Infoblox Universal DDI Modules for Ansible Collections facilitate the DNS and IPAM automation of VM workloads that are deployed across multiple platforms.
The universal_ddi_modules collection consists of modules and plug-ins required to manage the networks, IP addresses, and DNS records in universal_ddi. The collection is hosted on Ansible Galaxy under infoblox.universal_ddi_modules.
## Version Information

### What's new in v2
- The collection has been renamed from `b1ddi_modules` to `universal_ddi`.
- The modules are renamed to follow the Universal DDI API naming conventions. The old module names are deprecated and will be removed in the next major release.
- The modules are rewritten to use the [Universal DDI Python client](https://github.com/infobloxopen/universal-ddi-python-client) library. This provides a more consistent experience across the modules and supports a wider range of universal_ddi services.

## Collection Overview

### Modules
The `infoblox.universal_ddi` modules collection has the following content:

##### DNS
- `dns_acl` : Module to create, update and delete DNS ACL.
- `dns_acl_info` : Module to get DNS ACL information.
- `dns_auth_nsg` : Module to create, update and delete Auth NSG.
- `dns_auth_nsg_info` : Module to get Auth NSG information.
- `dns_auth_zone` : Module to create, update and delete Auth zone.
- `dns_auth_zone_info` : Module to get Auth zone information.
- `dns_delegation` : Module to create, update and delete DNS delegation.
- `dns_delegation_info` : Module to get DNS delegation information.
- `dns_forward_nsg` : Module to create, update and delete DNS forward NSG.
- `dns_forward_nsg_info` : Module to get DNS forward NSG information.
- `dns_forward_zone` : Module to create, update and delete DNS forward zone.
- `dns_forward_zone_info` : Module to get DNS forward zone information.
- `dns_host` : Module to update and disassociate DNS host.
- `dns_host_info` : Module to get DNS host information.
- `dns_record` : Module to create, update and delete DNS record.
- `dns_record_info` : Module to get DNS record information.
- `dns_server` : Module to create, update and delete DNS server.
- `dns_server_info` : Module to get DNS server information.
- `dns_view` : Module to create, update and delete DNS view.
- `dns_view_info` : Module to get view information.

##### INFRA
- `infra_host` : Module to create, update and delete an INFRA host.
- `infra_host_info` : Module to get INFRA host information.
- `infra_join_token` : Module to create, update and delete an INFRA join token.
- `infra_join_token_info` : Module to get INFRA join token information.
- `infra_service` : Module to create, update and delete an INFRA service.
- `infra_service_info` : Module to get INFRA service information.

##### IPAM
- `ipam_address` : Module to create, update and delete an IPAM address.
- `ipam_address_info` : Module to get IPAM address information.
- `ipam_address_block` : Module to create, update and delete an IPAM address block.
- `ipam_address_block_info` : Module to get IPAM address block information.
- `ipam_host` : Module to create, update and delete a IPAM host.
- `ipam_host_info` : Module to get IPAM host information.
- `ipam_ip_space` : Module to create, update and delete an IPAM IPSpace.
- `ipam_ip_space_info` : Module to get IPAM IPSpace information.
- `ipam_range` : Module to create, update and delete a IPAM range.
- `ipam_range_info` : Module to get IPAM range information.
- `ipam_subnet` : Module to create, update and delete a IPAM subnet.
- `ipam_subnet_info` : Module to get IPAM subnets information.
- `tsig_key` : Module to create, update and delete a tsig key.
- `tsig_key_info` : Module to get tsig key information.
- `kerberos_key_info` : Module to get kerberos key information.
- `ipam_next_available_ip_info` : Module to get next available ip information.
- `ipam_next_available_subnet_info` : Module to get next available subnets information.
- `ipam_next_available_address_block_info` : Module to get next available address block information.

## Requirements
 
- ansible >= 2.15
- python >= 3.9
- requests >= 2.26.0
- universal-ddi-python-client >= 0.1.0

## Installation

The `infoblox.universal_ddi` collection can be installed from git repository.

```shell
ansible-galaxy collection install git+https://github.com/infobloxopen/bloxone-ansible.git,v2
```

The python dependencies are not installed by `ansible-galaxy`. They can be manually installed using the following command:

```shell
pip install requests
pip install git+https://github.com/infobloxopen/universal-ddi-python-client
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

- name: Delete the View
  infoblox.bloxone.dns_view:
    name: "example-view"
    state: absent
```
### 2. Automated DNS ACL Management
**Description:** Automate the creation, modification, or deletion of DNS Access Control Lists (ACLs) for controlling and securing access to DNS services based on various criteria such as IP addresses, subnets, or specific user groups.

**Example:**
```yaml
- name: Create an ACL
  infoblox.bloxone.dns_acl:
    name: "example-acl"
    state: present
    
- name: Delete the ACL
  infoblox.bloxone.dns_acl:
    name: "example-acl"
    state: absent
```

### 3. Automated DNS AUTH NSG Management
**Description:** Automate the creation, modification, or deletion of DNS Authoritative Name Server Groups (NSG) to streamline and enhance DNS configurations.

**Example:**
```yaml
- name: Create an Auth NSG
  infoblox.bloxone.dns_auth_nsg:
    name: "example_nsg"
    state: present

- name: Delete the Auth NSG
  infoblox.bloxone.dns_auth_nsg:
    name: "example_nsg"
    state: absent
```

### 4. Automated DNS Auth Zone Management
**Description:** Automate the creation, deletion, or management of DNS Authoritative Zones to ensure consistent and efficient management of DNS records.

**Example:**
```yaml
- name: Create an Auth Zone
  infoblox.bloxone.dns_auth_zone:
    fqdn: "test-auth-zone"
    primary_type: external
    view: "{{ view.id }}"
    state: present

- name: Delete the Auth Zone
  infoblox.bloxone.dns_auth_zone:
    fqdn: "test-auth-zone"
    primary_type: external
    view: "{{ view.id }}"
    state: absent
```
### 5. DNS Delegation Management
**Description:** Create and delete DNS delegations within a domain for DNS management.

**Example:**
```yaml
- name: Create a Delegation
  infoblox.bloxone.dns_delegation:
    fqdn: "test-delegation"
    delegation_servers:
      - fqdn: "ns1.example.com."
        address: "12.0.0.0"
    view: "{{ view.id }}"
    state: present

- name: Delete the Delegation
  infoblox.bloxone.dns_delegation:
    fqdn: "test-delegation"
    view: "{{ view.id }}"
    state: absent
```

### 6. DNS Forward Zone Management
**Description:** Create and delete forward zones to direct DNS queries for a domain or subdomain to specific DNS servers.

**Example:**
```yaml
- name: Create a Forward Zone
  infoblox.bloxone.dns_forward_zone:
    fqdn: "example_zone."
    state: present

- name: Delete the Zone
  infoblox.bloxone.dns_forward_zone:
    name: "example_zone."
    state: "absent"
```

### 7. DNS Forwarding NSG Configuration
**Description:** Create and delete forward zones to direct DNS queries traffic.

**Example:**
```yaml
- name: Create a Forward NSG
  infoblox.bloxone.dns_forward_nsg:
    name: "example_nsg"
    state: "present"
    
- name: Delete the Forward NSG
  infoblox.bloxone.dns_forward_nsg:
    name: "example_nsg"
    state: "absent"
```

### 8. Automated DNS Record Management
**Description:** Automatically create, update, and delete DNS records in Universal DDI based on changes in your infrastructure.

**Example:**
```yaml
- name: Create a DNS A Record 
  infoblox.bloxone.dns_record:
    zone: "{{ auth_zone.id }}"
    rdata:
      address: "192.168.10.10"
    type: "A"
    state: "present"

- name: Delete the A Record
  infoblox.bloxone.dns_record:
    zone: "{{ auth_zone.id }}"
    rdata:
      address: "192.168.10.10"
    type: "A"
    state: absent
```

### 9. IP Address Management (IPAM)
**Description:** Automate the provisioning, updating, and de-provisioning of IP addresses in Universal DDI

**Example:**
```yaml
- name: "Create an IP space"
  infoblox.bloxone.ipam_ip_space:
      name: "example-ip-space"
      state: "present"

- name: "Delete IP Space"
  infoblox.bloxone.ipam_ip_space:
      name: "example-ip-space"
      state: "absent"
```
### 10. Address Block Management
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

- name: "Delete an Address Block"
  infoblox.bloxone.ipam_address_block:
    address: "10.0.0.0/16"
    space: "{{ ip_space.id }}"
    state: "absent"
```

### 11. Subnet Management
Description: Create, update, and delete subnets within a specific address block.

**Example:**
```yaml
- name: "Create a subnet"
  infoblox.bloxone.ipam_subnet:
    address: "10.0.0.0/24"
    space: "{{ ip_space.id }}"
    state: "present"

- name: "Delete a Subnet"
  infoblox.bloxone.ipam_subnet:
    address: "10.0.0.0/24"
    space: "{{ ip_space.id }}"
    state: "absent"
```

### 12. Address Management
**Description:** Manage and allocate IP address blocks, subnets, and ranges to efficiently utilize and track IP addresses within an organization or network.

**Example:**
```yaml
- name: "Create an Address"
  infoblox.bloxone.ipam_address:
    address: "10.0.0.3"
    space: "{{ ip_space.id }}"
    state: "present"
    
- name: "Delete an Address"
  infoblox.bloxone.ipam_address:
    address: "10.0.0.3"
    space: "{{ ip_space.id }}"
    state: "absent"
```

### 13. Host Management
**Description:** Managing the allocation, reservation, and tracking of IP addresses for hosts within a network.

**Example:**
```yaml
- name: "Create a Host"
  infoblox.bloxone.ipam_host:
    name: "example_host"
    state: "present"
  
- name: "Delete a host"
  infoblox.bloxone.ipam_host:
    name: "example_host"
    state: "absent"
```

### 14. IPAM Range Management
**Description:** Define, allocate, and manage IP address ranges within a subnet to ensure efficient use of IP space.

**Example:**
```yaml
- name: "Create a Range"
  infoblox.bloxone.ipam_range:
    start: "10.0.0.1"
    end: "10.0.0.100"
    space: "{{ ip_space.id }}"
    state: "present"
    
- name: "Delete the Range"
  infoblox.bloxone.ipam_range:
    start: "10.0.0.1"
    end: "10.0.0.100"
    space: "{{ ip_space.id }}"
    state: "absent"
```

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Issues or RFEs

You can open an issue or request for enhancement [here](https://github.com/infobloxopen/bloxone-ansible/issues)
 


