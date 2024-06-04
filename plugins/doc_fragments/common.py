# -*- coding: utf-8 -*-

# Copyright: Infoblox
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment:
    DOCUMENTATION = r"""
options:
    api_key:
        description:
          - The API token for authentication against Infoblox BloxOne API. If not set, the environment variable E(BLOXONE_API_KEY) will be used.
        type: str
        aliases: [ bloxone_api_key ]

    csp_url:
        description:
          - The Infoblox Cloud Services Portal (CSP) URL. If not set, the environment variable E(BLOXONE_CSP_URL) will be used.
        type: str
        aliases: [ bloxone_csp_url ]
        default: 'https://csp.infoblox.com'
"""
