# -*- coding: utf-8 -*-

# Copyright: Infoblox
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment:
    DOCUMENTATION = r"""
options:
    api_key:
        description:
          - Configures the API token for authentication against Infoblox BloxOne API.
        type: str
        required: true
    csp_url:
        description:
          - Configures the Infoblox BloxOne host URL.
        type: str
        default: 'https://csp.infoblox.com'
"""
