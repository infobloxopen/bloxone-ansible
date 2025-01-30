# Infoblox BloxOne Collection for Ansible

The Infoblox BloxOne Collection (`infoblox.bloxone`) includes a variety of Ansible modules to help automate the management of BloxOne services. 

## Version Information

### What's new in v2
- The collection has been renamed from `b1ddi_modules` to `bloxone`.
- The modules are renamed to follow the BloxOne API naming conventions. The old module names are deprecated and will be removed in the next major release.
- The modules are rewritten to use the [Universal DDI Python client](https://github.com/infobloxopen/universal-ddi-python-client) library. This provides a more consistent experience across the modules and supports a wider range of BloxOne services.

## Requirements
 
- ansible >= 2.15
- python >= 3.9
- requests >= 2.26.0
- universal-ddi-python-client >= 0.1.0

## Installation

The `infoblox.bloxone` collection can be installed from git repository.

```shell
ansible-galaxy collection install git+https://github.com/infobloxopen/bloxone-ansible.git,v2
```

The python dependencies are not installed by `ansible-galaxy`. They can be manually installed using the following command:

```shell
pip install requests
pip install git+https://github.com/infobloxopen/universal-ddi-python-client
```

## Usage

TBW - Add usage examples

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.


 


