#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: infra_service
short_description: Manage Infrastructure Services
description:
    - Manage Infrastructure Services
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
            - "The description of the Service (optional)."
        type: str
    desired_state:
        description:
            - "The desired state of the Service."
        type: str
        choices:
            - start
            - stop
        default: stop
    desired_version:
        description:
            - "The desired version of the Service."
        type: str
    interface_labels:
        description:
            - "List of interfaces on which this Service can operate. Note: The list can contain custom interface labels (Example: C(\"[\"WAN\",\"LAN\",\"label1\",\"label2\"]\"))"
        type: list
        elements: str
    name:
        description:
            - "The name of the Service (unique)."
        type: str
    pool_id:
        description:
            - "The resource identifier."
        type: str
    service_type:
        description:
            - "The type of the Service deployed on the Host (C(\"dns\"), C(\"cdc\"), etc.)."
        type: str
    tags:
        description:
            - "Tags associated with this Service."
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create a host
    infoblox.bloxone.infra_host:
      display_name: "example_host"
      state: "present"
    register: infra_host

  - name: Create a service
    infoblox.bloxone.infra_service:
      name: "example_service"
      service_type: "dns"
      pool_id: "{{ infra_host.object.pool_id }}"
      state: "present"

  - name: Create a Service with Additional Fields
    infoblox.bloxone.infra_service:
      name: "example_service"
      description: "Example Infra Service"
      service_type: "dns"
      pool_id: " {{ infra_host.object.pool_id }}"
      desired_version: "3.4.0"
      desired_state: "start"
      interface_labels:
        - "WAN"
        - "label1"
      state: "present"
      tags:
        location: "site-1"

  - name: Delete the Service
    infoblox.bloxone.infra_service:
      name: "example_service"
      service_type: "dns"
      pool_id: "{{ infra_host.object.pool_id }}"
      state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the Services object
    type: str
    returned: Always
item:
    description:
        - Services object
    type: complex
    returned: Always
    contains:
        configs:
            description:
                - "List of Host-specific configurations of this Service."
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
        created_at:
            description:
                - "Timestamp of creation of Service."
            type: str
            returned: Always
        description:
            description:
                - "The description of the Service (optional)."
            type: str
            returned: Always
        desired_state:
            description:
                - "The desired state of the Service. Should either be C(\"\"start\"\") or C(\"\"stop\"\")."
            type: str
            returned: Always
        desired_version:
            description:
                - "The desired version of the Service."
            type: str
            returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        interface_labels:
            description:
                - "List of interfaces on which this Service can operate. Note: The list can contain custom interface labels (Example: C(\"[\"WAN\",\"LAN\",\"label1\",\"label2\"]\"))"
            type: list
            returned: Always
        name:
            description:
                - "The name of the Service (unique)."
            type: str
            returned: Always
        pool_id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        service_type:
            description:
                - "The type of the Service deployed on the Host (C(\"dns\"), C(\"cdc\"), etc.)."
            type: str
            returned: Always
        tags:
            description:
                - "Tags associated with this Service."
            type: dict
            returned: Always
        updated_at:
            description:
                - "Timestamp of the latest update on Service."
            type: str
            returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from infra_mgmt import Service, ServicesApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class InfraServiceModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(InfraServiceModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Service.from_dict(self._payload_params)
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
                resp = ServicesApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = ServicesApi(self.client).list(filter=filter)

            # If no results, set results to empty list
            if not resp.results:
                resp.results = []

            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Services: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = ServicesApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload

        resp = ServicesApi(self.client).update(id=self.existing.id, body=update_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        ServicesApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Services created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Services updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Services deleted"

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
        desired_state=dict(type="str", choices=["start", "stop"], default="stop"),
        desired_version=dict(type="str"),
        interface_labels=dict(type="list", elements="str"),
        name=dict(type="str"),
        pool_id=dict(type="str"),
        service_type=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = InfraServiceModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name", "pool_id", "service_type"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
