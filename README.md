# Infoblox BloxOne Collection for Ansible

The Infoblox BloxOne Collection (`infoblox.bloxone`) includes a variety of Ansible modules to help automate the management of BloxOne services. 

## Version Information

This version(v2) of the Infoblox BloxOne Collection is a complete rewrite. 
If you still need to use the `b1ddi_modules`, please switch to the v1 branch.

### What's new in v2
- The collection has been renamed from `b1ddi_modules` to `bloxone`.
- The modules have been renamed to follow the BloxOne API naming conventions and Ansible best practices.
- Uses the [BloxOne Python client](https://github.com/infobloxopen/bloxone-python-client) library to interact with the BloxOne API.
- Supports a wider range of BloxOne services including DDI, Threat Defense and Infrastructure Management.
- Rewritten with the current best practices for Ansible collections.

### Compatibility
Since this is a complete rewrite, the modules in this collection are not compatible with the modules in the v1 branch.

## Requirements
 
- ansible >= 2.15
- python >= 3.9
- bloxone-python-client >= 0.1.0

## Installation

The `infoblox.bloxone` collection can be installed from git repository.

```shell
ansible-galaxy collection install git+https://github.com/infobloxopen/bloxone-ansible.git,v2
```

The python dependencies are not installed by `ansible-galaxy`. They can be manually installed using the following command:

```shell
pip install git+https://github.com/infobloxopen/bloxone-python-client
```

## Usage

TBW - Add usage examples

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.


 


