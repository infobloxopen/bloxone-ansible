# -*- coding: utf-8 -*-

# Copyright: Infoblox
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


class ModuleDocFragment:
    DOCUMENTATION = r"""
options:
    portal_key:
        description:
          - The API token for authentication against Infoblox BloxOne API. If not set, the environment variable E(INFOBLOX_PORTAL_KEY) will be used.
        type: str
        aliases: [ infoblox_portal_key, api_key ]

    portal_url:
        description:
          - The Infoblox Cloud Services Portal (CSP) URL. If not set, the environment variable E(INFOBLOX_PORTAL_URL) will be used.
        type: str
        aliases: [ infoblox_portal_url, csp_url ]
        default: 'https://csp.infoblox.com'
"""
