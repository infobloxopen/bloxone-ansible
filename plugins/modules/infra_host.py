#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: infra_host
short_description: Manage Infrastructure Hosts
description:
    - Manage Infrastructure Hosts
version_added: 2.0.0
author: Infoblox Inc. (@infobloxopen)
options:
    id:
        description:
            - ID of the object
        type: str
        required: false
    state:
        description:
            - Indicate desired state of the object
        type: str
        required: false
        choices:
            - present
            - absent
        default: present
    description:
        description:
            - "The description of the Host (optional)."
        type: str
    display_name:
        description:
            - "The name of the Host (unique)."
        type: str
    ip_space:
        description:
            - "The IP Space of the Host."
        type: str
    location_id:
        description:
            - "The resource identifier."
        type: str
    maintenance_mode:
        description: "The flag to indicate if the Host is in maintenance mode."
        choices:
            - enabled
            - disabled
        type: str
    pool_id:
        description:
            - "The resource identifier."
        type: str
    serial_number:
        description:
            - "The unique serial number of the Host."
        type: str
    tags:
        description:
            - "Tags associated with this Host."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create a host
    infoblox.bloxone.infra_host:
      display_name: "example_host"
      state: "present"

  - name: Create a host with Additional Fields
    infoblox.bloxone.infra_host:
      name: "example_host"
      description: "Example Infra Host"
      maintenance_mode: enabled
      state: "present"
      tags:
        location: "my-location"

  - name: Delete the host
    infoblox.bloxone.infra_host:
      display_name: "example_host"
      state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the Hosts object
    type: str
    returned: Always
item:
    description:
        - Hosts object
    type: complex
    returned: Always
    contains:
        configs:
            description:
                - "The list of Host-specific configurations for each Service deployed on this Host."
            type: list
            returned: Always
            elements: dict
            contains:
                current_version:
                    description:
                        - "The current version of the Service deployed on the Host."
                    type: str
                    returned: Always
                extra_data:
                    description:
                        - "The field to carry any extra data specific to this configuration."
                    type: str
                    returned: Always
                host_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                service_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                service_type:
                    description:
                        - "The type of the Service deployed on the Host (C(\"dns\"), C(\"cdc\"), etc.)."
                    type: str
                    returned: Always
                upgraded_at:
                    description:
                        - "The timestamp of the latest upgrade of the Host-specific Service configuration."
                    type: str
                    returned: Always
        connectivity_monitor:
            description:
                - "Represents the connectivity monitor properties of a Host, to enable/disable connectivity monitoring for redundant network interfaces."
                - "The \"endpoint_type\" is:"
                - "- C(\"\"csp\"\") for enabling monitoring"
                - "- C(\"\"\"\") for disabling monitoring (default)"
                - "Note: Currently, all fields except \"endpoint_type\" are read-only, and will be overridden to default values in case they are edited."
                - "Example:"
                - "{"
                - "\"connectivity_monitor\": {"
                - "\"cost\":1000000,"
                - "\"endpoint_type\":\"csp\","
                - "\"endpoint\":\"http://csp.infoblox.com\","
                - "\"interval\":15,"
                - "\"failure_threshold\":1,"
                - "\"success_threshold\":2"
                - "}"
                - "}"
            type: dict
            returned: Always
        created_at:
            description:
                - "The timestamp of creation of Host."
            type: str
            returned: Always
        created_by:
            description:
                - "The creator of the Host (internal use only)."
            type: str
            returned: Always
        description:
            description:
                - "The description of the Host (optional)."
            type: str
            returned: Always
        display_name:
            description:
                - "The name of the Host (unique)."
            type: str
            returned: Always
        host_subtype:
            description:
                - "The sub-type of a specific Host type."
                - "Example: For Host type BloxOne Appliance, sub-type could be \"B105\" or \"VEP1425\""
            type: str
            returned: Always
        host_type:
            description:
                - "The type of Host."
                - "Should be one of: 1. NIOS , 2. NIOS HA, 3. BloxOne VM , 4. BloxOne Appliance, 5. BloxOne Container, 6. CNIOS"
            type: str
            returned: Always
        host_version:
            description:
                - "The version of the Host platform services."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        ip_address:
            description:
                - "The IP address of the Host."
            type: str
            returned: Always
        ip_space:
            description:
                - "The IP Space of the Host."
            type: str
            returned: Always
        legacy_id:
            description:
                - "The legacy Host object identifier."
            type: str
            returned: Always
        location_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        mac_address:
            description:
                - "The MAC address of the Host."
            type: str
            returned: Always
        maintenance_mode:
            description: "The flag to indicate if the Host is in maintenance mode."
            type: str
            returned: Always
        nat_ip:
            description:
                - "The NAT IP address of the Host."
            type: str
            returned: Always
        noa_cluster:
            description:
                - "The CSP cluster identifier (internal use only)."
            type: str
            returned: Always
        ophid:
            description:
                - "The unique On-Prem Host ID generated by the On-Prem device and assigned to the Host once it is registered and logged into the Infoblox Cloud."
            type: str
            returned: Always
        pool_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        serial_number:
            description:
                - "The unique serial number of the Host."
            type: str
            returned: Always
        tags:
            description:
                - "Tags associated with this Host."
            type: dict
            returned: Always
        timezone:
            description:
                - "The timezone of the Host."
            type: str
            returned: Always
        updated_at:
            description:
                - "The timestamp of the latest update on Host."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from infra_mgmt import Host, HostsApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class InfraHostModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(InfraHostModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Host.from_dict(self._payload_params)
        self._existing = None

    @property
    def existing(self):
        return self._existing

    @existing.setter
    def existing(self, value):
        self._existing = value

    @property
    def payload_params(self):
        return self._payload_params

    @property
    def payload(self):
        return self._payload

    def payload_changed(self):
        if self.existing is None:
            # if existing is None, then it is a create operation
            return True

        return self.is_changed(self.existing.model_dump(by_alias=True, exclude_none=True), self.payload_params)

    def find(self):
        if self.params["id"] is not None:
            try:
                resp = HostsApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"display_name=='{self.params['display_name']}'"
            resp = HostsApi(self.client).list(filter=filter)

            # If no results, set results to empty list
            if not resp.results:
                resp.results = []

            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Hosts: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = HostsApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        updated_body = self.payload
        updated_body.pool_id = self.existing.pool_id

        resp = HostsApi(self.client).update(id=self.existing.id, body=updated_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        HostsApi(self.client).delete(self.existing.id)

    def run_command(self):
        result = dict(changed=False, object={}, id=None)

        # based on the state that is passed in, we will execute the appropriate
        # functions
        try:
            self.existing = self.find()
            item = {}
            if self.params["state"] == "present" and self.existing is None:
                item = self.create()
                result["changed"] = True
                result["msg"] = "Hosts created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Hosts updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Hosts deleted"

            if self.check_mode:
                # if in check mode, do not update the result or the diff, just return the changed state
                self.exit_json(**result)

            result["diff"] = dict(
                before=self.existing.model_dump(by_alias=True, exclude_none=True) if self.existing is not None else {},
                after=item,
            )
            result["object"] = item
            result["id"] = (
                self.existing.id if self.existing is not None else item["id"] if (item and "id" in item) else None
            )
        except ApiException as e:
            self.fail_json(msg=f"Failed to execute command: {e.status} {e.reason} {e.body}")

        self.exit_json(**result)


def main():
    module_args = dict(
        id=dict(type="str", required=False),
        state=dict(type="str", required=False, choices=["present", "absent"], default="present"),
        description=dict(type="str"),
        display_name=dict(type="str"),
        ip_space=dict(type="str"),
        location_id=dict(type="str"),
        maintenance_mode=dict(type="str", choices=["enabled", "disabled"]),
        pool_id=dict(type="str"),
        serial_number=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = InfraHostModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["display_name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
