# Infoblox BloxOne Collection for Ansible

About 
=====
Infoblox Ansible Collection for BloxOne (`infoblox.b1ddi_modules`) allows you to interact with the BloxOne DDI through APIs. 

Requirements
============
 
- Ansible 2.10 and above
- Python 3.9
- JsonPath ( pip install Jsonpath )

Collection Overview
===================

Modules
--------
The `infoblox.b1ddi_modules` collection has the following content:

- `b1_dns_view`: Module to create and delete DNS view
- `b1_dns_zone`: Module to create and delete DNS zone
- `b1_a_record`: Module to create and delete A record
- `b1_cname_record`: Module to create and delete CNAME record
- `b1_ptr_record`: Module to create and delete PTR record
- `b1_ns_record`: Module to create and delete NS record


Role Variables
--------------
 
You need to provide the following variables as an extra var character to the Ansible playbook during runtime:
 
- `create_dns_view`: For creating a DNS view
- `delete_dns_view`: For deleting a DNS view
- `create_dns_zone`: For creating a DNS zone
- `delete_dns_zone`: For deleting a DNS zone
- `create_a_record`: For creating an A record
- `delete_a_record`: For deleting an A record
- `create_ns_record`: For creating an NS record
- `delete_ns_record`: For deleting an NS record
- `create_ptr_record`: For creating a PTR record
- `delete_ptr_record`: For deleting a PTR record

Usage Instructions
==================
To run a playbook, complete the following:
 
1. Make a local copy of the repository.  
  
2. Update the names of the objects to be created and deleted in vars_file.yaml. 

Example:
--------
```shell
  views:
     - name: devops1
  	    desc: test1
  	    zones:
   	   - fqdn: dev1.com
         host: 172.28.4.128
         record:
      	     - name: record_1
              record_ip: 10.10.10.13
   	   - fqdn: dev2.com
         host: 172.28.4.128
         record:
     	      - name: record_2
              record_ip: 10.10.10.14
       - fqdn: dev3.com
         host: 172.28.4.128
         record:
     	      - name: record_3
              record_ip: 10.10.10.14
```
 
3. Execute the following commands for running the playbook:

- To create a DNS view:
```shell
$ ansible-playbook configure.yml -e create_dns_view=True
```
- To delete a DNS view:
```shell
$ ansible-playbook configure.yml -e delete_dns_view=True
```
- To create a DNS zone:
```shell
$ ansible-playbook configure.yml -e create_dns_zone=True
```
- To delete a DNS view:
```shell
$ ansible-playbook configure.yml -e delete_dns_zone=True
```

Limitations
===========
The update operation is currently not supported

License
=======
 
 
Author Information
==================
 


