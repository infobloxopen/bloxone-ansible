#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: infra_join_token
short_description: Manage JoinToken
description:
    - Manage JoinToken
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
            - revoked
        default: present
    description:
        description:
            - Description of the Join Token
        type: str
    expires_at:
        description:
            - Expiration time of the Join Token
        type: str
    name:
        description:
            - Name of the Join Token
        type: str
    tags:
        description:
            - Tags of the Join Token
        type: dict

extends_documentation_fragment:
    - infoblox.bloxone.common
"""  # noqa: E501

EXAMPLES = r"""
  - name: Create a Join token
    infoblox.bloxone.infra_join_token:
      name: "example_token"
      state: "present"

  - name: Create a Join Token with Additional Fields
    infoblox.bloxone.infra_join_token:
      name: "example_token"
      description: "Example Join Token"
      tags:
        location: "my-location"

  - name: Revoke a Join token
    infoblox.bloxone.infra_join_token:
      name: "example_token"
      state: "revoked"
"""

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from bloxone_client import ApiException, NotFoundException
    from infra_provision import JoinToken, UIJoinTokenApi
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class JoinTokenModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(JoinTokenModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = JoinToken.from_dict(self._payload_params)
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
                resp = UIJoinTokenApi(self.client).read(self.params["id"])
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "revoked":
                    return None
                raise e
        else:
            filter = f"name=='{self.params['name']}'"
            resp = UIJoinTokenApi(self.client).list(filter=filter)

            # If no results, set results to empty list
            if not resp.results:
                resp.results = []

            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple View: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = UIJoinTokenApi(self.client).create(body=self.payload)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.payload
        update_body = self.validate_readonly_on_update(self.existing, update_body, ["name", "description"])

        resp = UIJoinTokenApi(self.client).update(id=self.existing.id, body=update_body)
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        UIJoinTokenApi(self.client).delete(self.existing.id)

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
                result["msg"] = "JoinToken created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "JoinToken updated"
            elif self.params["state"] == "revoked" and self.existing is not None and self.existing.status != "REVOKED":
                self.delete()
                result["changed"] = True
                result["msg"] = "JoinToken Revoked"
            elif self.params["state"] == "revoked" and self.existing is not None and self.existing.status == "REVOKED":
                result["changed"] = False
                result["msg"] = "JoinToken Revoked"

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
        state=dict(type="str", required=False, choices=["present", "revoked"], default="present"),
        description=dict(type="str"),
        expires_at=dict(type="str"),
        name=dict(type="str"),
        tags=dict(type="dict"),
    )

    module = JoinTokenModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["name"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
