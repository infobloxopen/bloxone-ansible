#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: Infoblox Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: ipam_range
short_description: Manage Range
description:
    - Manages a Range
    - A Range object represents a set of contiguous IP addresses in the same IP space with no gap.
    - They are expressed as a (start, end) pair within a given subnet that are grouped together for administrative purpose and protocol management.
    - The start and end values are not required to align with CIDR boundaries.
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
    comment:
        description:
            - "The description for the range. May contain 0 to 1024 characters. Can include UTF-8."
        type: str
    dhcp_host:
        description:
            - "The resource identifier."
        type: str
    dhcp_options:
        description:
            - "The list of DHCP options. May be either a specific option or a group of options."
        type: list
        elements: dict
        suboptions:
            group:
                description:
                    - "The resource identifier."
                type: str
            option_code:
                description:
                    - "The resource identifier."
                type: str
            option_value:
                description:
                    - "The option value."
                type: str
            type:
                description:
                    - "The type of item."
                    - "Valid values are:"
                    - "* I(group)"
                    - "* I(option)"
                type: str
    disable_dhcp:
        description:
            - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
            - "Defaults to I(false)."
        type: bool
    end:
        description:
            - "The end IP address of the range."
        type: str
    exclusion_ranges:
        description:
            - "The list of all exclusion ranges in the scope of the range."
        type: list
        elements: dict
        suboptions:
            comment:
                description:
                    - "The description for the exclusion range. May contain 0 to 1024 characters. Can include UTF-8."
                type: str
            end:
                description:
                    - "The end address of the exclusion range."
                type: str
            start:
                description:
                    - "The start address of the exclusion range."
                type: str
    filters:
        description:
            - "The list of all allow/deny filters of the range."
        type: list
        elements: dict
        suboptions:
            access:
                description:
                    - "The access type of DHCP filter (I(allow) or I(deny))."
                    - "Defaults to I(allow)."
                type: str
            hardware_filter_id:
                description:
                    - "The resource identifier."
                type: str
            option_filter_id:
                description:
                    - "The resource identifier."
                type: str
    inheritance_parent:
        description:
            - "The resource identifier."
        type: str
    inheritance_sources:
        description:
            - "The DHCP inheritance configuration for the range."
        type: dict
        suboptions:
            dhcp_options:
                description:
                    - "The inheritance configuration for the I(dhcp_options) field."
                type: dict
                suboptions:
                    action:
                        description:
                            - "The inheritance setting."
                            - "Valid values are:"
                            - "* I(inherit): Use the inherited value."
                            - "* I(block): Don't use the inherited value."
                            - "Defaults to I(inherit)."
                        type: str
                    value:
                        description:
                            - "The inherited DHCP option values."
                        type: list
                        elements: dict
                        suboptions:
                            action:
                                description:
                                    - "The inheritance setting."
                                    - "Valid values are:"
                                    - "* I(inherit): Use the inherited value."
                                    - "* I(block): Don't use the inherited value."
                                    - "Defaults to I(inherit)."
                                type: str
    name:
        description:
            - "The name of the range. May contain 1 to 256 characters. Can include UTF-8."
        type: str
    parent:
        description:
            - "The resource identifier."
        type: str
    space:
        description:
            - "The resource identifier."
        type: str
    start:
        description:
            - "The start IP address of the range."
        type: str
    tags:
        description:
            - "The tags for the range in JSON format."
        type: dict
    threshold:
        description:
            - "The utilization threshold settings for the range."
        type: dict
        suboptions:
            enabled:
                description:
                    - "Indicates whether the utilization threshold for IP addresses is enabled or not."
                type: bool
            high:
                description:
                    - "The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object.
                        Thresholds are inclusive in the comparison test."
                type: int
            low:
                description:
                    - "The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object.
                        Thresholds are inclusive in the comparison test."
                type: int

extends_documentation_fragment:
    - infoblox.bloxone.common
"""
EXAMPLES = r"""
    - name: "Create an IP Space (required as parent)"
      infoblox.bloxone.ipam_ip_space:
        name: "my-ip-space"
        state: "present"
      register: ip_space

    - name: "Create a Subnet (required as parent)"
      infoblox.bloxone.ipam_subnet:
        address: "10.0.0.0/24"
        space: "{{ ip_space.id }}"
        state: "present"

    - name: "Create a Range"
      infoblox.bloxone.ipam_range:
        start: "10.0.0.1"
        end: "10.0.0.100"
        space: "{{ ip_space.id }}"
        state: "present"

    - name: "Create a Range with additional Fields"
      infoblox.bloxone.ipam_range:
        start: "10.0.0.1"
        end: "10.0.0.100"
        space: "{{ ip_space.id }}"
        disable_dhcp: "true"
        tags:
          location: "site-1"
        name: "Example Range"
        exclusion_ranges:
          - start: "10.0.0.10"
            end: "10.0.0.20"
            comment: "Exclude this range"
        threshold:
          enabled: true
          high: 90
          low: 10
        state: "present"

    - name: "Delete the Range"
      infoblox.bloxone.ipam_range:
        start: "10.0.0.1"
        end: "10.0.0.100"
        space: "{{ ip_space.id }}"
        state: "absent"
"""

RETURN = r"""
id:
    description:
        - ID of the Range object
    type: str
    returned: Always
item:
    description:
        - Range object
    type: complex
    returned: Always
    contains:
        comment:
            description:
                - "The description for the range. May contain 0 to 1024 characters. Can include UTF-8."
            type: str
            returned: Always
        compartment_id:
            description:
                - "The compartment associated with the object. If no compartment is associated with the object, the value defaults to empty."
            type: str
            returned: Always
        created_at:
            description:
                - "Time when the object has been created."
            type: str
            returned: Always
        dhcp_host:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        dhcp_options:
            description:
                - "The list of DHCP options. May be either a specific option or a group of options."
            type: list
            returned: Always
            elements: dict
            contains:
                group:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_code:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_value:
                    description:
                        - "The option value."
                    type: str
                    returned: Always
                type:
                    description:
                        - "The type of item."
                        - "Valid values are:"
                        - "* I(group)"
                        - "* I(option)"
                    type: str
                    returned: Always
        disable_dhcp:
            description:
                - "Optional. I(true) to disable object. A disabled object is effectively non-existent when generating configuration."
                - "Defaults to I(false)."
            type: bool
            returned: Always
        end:
            description:
                - "The end IP address of the range."
            type: str
            returned: Always
        exclusion_ranges:
            description:
                - "The list of all exclusion ranges in the scope of the range."
            type: list
            returned: Always
            elements: dict
            contains:
                comment:
                    description:
                        - "The description for the exclusion range. May contain 0 to 1024 characters. Can include UTF-8."
                    type: str
                    returned: Always
                end:
                    description:
                        - "The end address of the exclusion range."
                    type: str
                    returned: Always
                start:
                    description:
                        - "The start address of the exclusion range."
                    type: str
                    returned: Always
        filters:
            description:
                - "The list of all allow/deny filters of the range."
            type: list
            returned: Always
            elements: dict
            contains:
                access:
                    description:
                        - "The access type of DHCP filter (I(allow) or I(deny))."
                        - "Defaults to I(allow)."
                    type: str
                    returned: Always
                hardware_filter_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                option_filter_id:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
        id:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_assigned_hosts:
            description:
                - "The list of the inheritance assigned hosts of the object."
            type: list
            returned: Always
            elements: dict
            contains:
                display_name:
                    description:
                        - "The human-readable display name for the host referred to by I(ophid)."
                    type: str
                    returned: Always
                host:
                    description:
                        - "The resource identifier."
                    type: str
                    returned: Always
                ophid:
                    description:
                        - "The on-prem host ID."
                    type: str
                    returned: Always
        inheritance_parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        inheritance_sources:
            description:
                - "The DHCP inheritance configuration for the range."
            type: dict
            returned: Always
            contains:
                dhcp_options:
                    description:
                        - "The inheritance configuration for the I(dhcp_options) field."
                    type: dict
                    returned: Always
                    contains:
                        action:
                            description:
                                - "The inheritance setting."
                                - "Valid values are:"
                                - "* I(inherit): Use the inherited value."
                                - "* I(block): Don't use the inherited value."
                                - "Defaults to I(inherit)."
                            type: str
                            returned: Always
                        value:
                            description:
                                - "The inherited DHCP option values."
                            type: list
                            returned: Always
                            elements: dict
                            contains:
                                action:
                                    description:
                                        - "The inheritance setting."
                                        - "Valid values are:"
                                        - "* I(inherit): Use the inherited value."
                                        - "* I(block): Don't use the inherited value."
                                        - "Defaults to I(inherit)."
                                    type: str
                                    returned: Always
                                display_name:
                                    description:
                                        - "The human-readable display name for the object referred to by I(source)."
                                    type: str
                                    returned: Always
                                source:
                                    description:
                                        - "The resource identifier."
                                    type: str
                                    returned: Always
                                value:
                                    description:
                                        - "The inherited value for the DHCP option."
                                    type: dict
                                    returned: Always
                                    contains:
                                        option:
                                            description:
                                                - "Option inherited from the ancestor."
                                            type: dict
                                            returned: Always
                                            contains:
                                                group:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_code:
                                                    description:
                                                        - "The resource identifier."
                                                    type: str
                                                    returned: Always
                                                option_value:
                                                    description:
                                                        - "The option value."
                                                    type: str
                                                    returned: Always
                                                type:
                                                    description:
                                                        - "The type of item."
                                                        - "Valid values are:"
                                                        - "* I(group)"
                                                        - "* I(option)"
                                                    type: str
                                                    returned: Always
                                        overriding_group:
                                            description:
                                                - "The resource identifier."
                                            type: str
                                            returned: Always
        name:
            description:
                - "The name of the range. May contain 1 to 256 characters. Can include UTF-8."
            type: str
            returned: Always
        parent:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        protocol:
            description:
                - "The type of protocol (I(ip4) or I(ip6))."
            type: str
            returned: Always
        space:
            description:
                - "The resource identifier."
            type: str
            returned: Always
        space_name:
            description:
                - "The name of the IP Space the range belongs to."
            type: str
            returned: Always
        start:
            description:
                - "The start IP address of the range."
            type: str
            returned: Always
        tags:
            description:
                - "The tags for the range in JSON format."
            type: dict
            returned: Always
        threshold:
            description:
                - "The utilization threshold settings for the range."
            type: dict
            returned: Always
            contains:
                enabled:
                    description:
                        - "Indicates whether the utilization threshold for IP addresses is enabled or not."
                    type: bool
                    returned: Always
                high:
                    description:
                        - "The high threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
                low:
                    description:
                        - "The low threshold value for the percentage of used IP addresses relative to the total IP addresses available in the scope of the object. Thresholds are inclusive in the comparison test."
                    type: int
                    returned: Always
        updated_at:
            description:
                - "Time when the object has been updated. Equals to I(created_at) if not updated after creation."
            type: str
            returned: Always
        utilization:
            description:
                - "The utilization statistics of IPV4 addresses for the range."
            type: dict
            returned: Always
            contains:
                abandon_utilization:
                    description:
                        - "The percentage of abandoned IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
                abandoned:
                    description:
                        - "The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client)."
                    type: str
                    returned: Always
                dynamic:
                    description:
                        - "The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases."
                    type: str
                    returned: Always
                free:
                    description:
                        - "The number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                static:
                    description:
                        - "The number of defined IP addresses such as reservations or DNS records. It can be computed as I(static) = I(used) - I(dynamic)."
                    type: str
                    returned: Always
                total:
                    description:
                        - "The total number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                used:
                    description:
                        - "The number of IP addresses used in the scope of the object."
                    type: str
                    returned: Always
                utilization:
                    description:
                        - "The percentage of used IP addresses relative to the total IP addresses available in the scope of the object."
                    type: int
                    returned: Always
        utilization_v6:
            description:
                - "The utilization of IPV6 addresses in the range."
            type: dict
            returned: Always
            contains:
                abandoned:
                    description: "The number of IP addresses in the scope of the object which are in the abandoned state (issued by a DHCP server and then declined by the client)."
                    type: str
                    returned: Always
                dynamic:
                    description: "The number of IP addresses handed out by DHCP in the scope of the object. This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases."
                    type: str
                    returned: Always
                static:
                    description: "The number of defined IP addresses such as reservations or DNS records. It can be computed as static = used - dynamic."
                    type: str
                    returned: Always
                total:
                    description: "The total number of IP addresses available in the scope of the object."
                    type: str
                    returned: Always
                used:
                    description: "The number of IP addresses used in the scope of the object."
                    type: str
                    returned: Always
"""  # noqa: E501

from ansible_collections.infoblox.bloxone.plugins.module_utils.modules import BloxoneAnsibleModule

try:
    from ipam import Range, RangeApi
    from universal_ddi_client import ApiException, NotFoundException
except ImportError:
    pass  # Handled by BloxoneAnsibleModule


class RangeModule(BloxoneAnsibleModule):
    def __init__(self, *args, **kwargs):
        super(RangeModule, self).__init__(*args, **kwargs)

        exclude = ["state", "csp_url", "api_key", "portal_url", "portal_key", "id"]
        self._payload_params = {k: v for k, v in self.params.items() if v is not None and k not in exclude}
        self._payload = Range.from_dict(self._payload_params)
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
                resp = RangeApi(self.client).read(self.params["id"], inherit="full")
                return resp.result
            except NotFoundException as e:
                if self.params["state"] == "absent":
                    return None
                raise e
        else:
            filter = (
                f"start=='{self.params['start']}' and end=='{self.params['end']}' and space=='{self.params['space']}'"
            )
            resp = RangeApi(self.client).list(filter=filter, inherit="full")
            if len(resp.results) == 1:
                return resp.results[0]
            if len(resp.results) > 1:
                self.fail_json(msg=f"Found multiple Range: {resp.results}")
            if len(resp.results) == 0:
                return None

    def create(self):
        if self.check_mode:
            return None

        resp = RangeApi(self.client).create(body=self.payload, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def update(self):
        if self.check_mode:
            return None

        update_body = self.validate_readonly_on_update(self.existing, self.payload, ["space"])

        resp = RangeApi(self.client).update(id=self.existing.id, body=update_body, inherit="full")
        return resp.result.model_dump(by_alias=True, exclude_none=True)

    def delete(self):
        if self.check_mode:
            return

        RangeApi(self.client).delete(self.existing.id)

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
                result["msg"] = "Range created"
            elif self.params["state"] == "present" and self.existing is not None:
                if self.payload_changed():
                    item = self.update()
                    result["changed"] = True
                    result["msg"] = "Range updated"
            elif self.params["state"] == "absent" and self.existing is not None:
                self.delete()
                result["changed"] = True
                result["msg"] = "Range deleted"

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
        comment=dict(type="str"),
        dhcp_host=dict(type="str"),
        dhcp_options=dict(
            type="list",
            elements="dict",
            options=dict(
                group=dict(type="str"),
                option_code=dict(type="str"),
                option_value=dict(type="str"),
                type=dict(type="str"),
            ),
        ),
        disable_dhcp=dict(type="bool"),
        end=dict(type="str"),
        exclusion_ranges=dict(
            type="list",
            elements="dict",
            options=dict(
                comment=dict(type="str"),
                end=dict(type="str"),
                start=dict(type="str"),
            ),
        ),
        filters=dict(
            type="list",
            elements="dict",
            options=dict(
                access=dict(type="str"),
                hardware_filter_id=dict(type="str"),
                option_filter_id=dict(type="str"),
            ),
        ),
        inheritance_parent=dict(type="str"),
        inheritance_sources=dict(
            type="dict",
            options=dict(
                dhcp_options=dict(
                    type="dict",
                    options=dict(
                        action=dict(type="str"),
                        value=dict(
                            type="list",
                            elements="dict",
                            options=dict(
                                action=dict(type="str"),
                            ),
                        ),
                    ),
                ),
            ),
        ),
        name=dict(type="str"),
        parent=dict(type="str"),
        space=dict(type="str"),
        start=dict(type="str"),
        tags=dict(type="dict"),
        threshold=dict(
            type="dict",
            options=dict(
                enabled=dict(type="bool"),
                high=dict(type="int"),
                low=dict(type="int"),
            ),
        ),
    )

    module = RangeModule(
        argument_spec=module_args,
        supports_check_mode=True,
        required_if=[("state", "present", ["start", "end", "space"])],
    )

    module.run_command()


if __name__ == "__main__":
    main()
