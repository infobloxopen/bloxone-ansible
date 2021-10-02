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



Usage Instructions
==================
To run a playbook, complete the following:
 
1. Make a local copy of the repository
2. Update the ansible.cfg  
  
 
Limitations
===========
Create operation is supported only for required fields.
Update operation is supported for selected fields.

License
=======
 
 
Author Information
==================
 Amit Mishra (amishra2@infoblox.com)
 Sriram Kanan (kannans@infoblox.com)
 Vedant Sethia 
 


