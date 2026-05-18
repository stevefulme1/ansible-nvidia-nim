# -*- coding: utf-8 -*-
# Copyright (c) 2024, Steve Fulmer
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module for retrieve nim organization details."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: nim_org_info
short_description: Retrieve NIM organization details
description:
    - Retrieve NIM organization details using the NVIDIA REST API.
    - This module requires the C(requests) Python library.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    org_id:
        description:
            - The org id for the org.
        type: str
    name:
        description:
            - The name for the org.
        type: str
extends_documentation_fragment:
    - stevefulme1.nvidia_nim.nvidia_common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: Get org details
  stevefulme1.nvidia_nim.nim_org_info:
    org_id: "example-id"
"""

RETURN = r"""
org:
    description: Details of the org.
    returned: On success.
    type: dict
    sample:
        id: "example-id"
        name: "example-org"
        status: "ACTIVE"
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.stevefulme1.nvidia_nim.plugins.module_utils.nvidia_common import (
    NVIDIA_COMMON_ARGS,
    to_dict,
)
from ansible_collections.stevefulme1.nvidia_nim.plugins.module_utils.nvidia_api import (
    NvidiaApiError,
    create_api_client,
)


def get_module_args():
    module_args = dict(
        org_id=dict(type="str"),
        name=dict(type="str"),
    )
    module_args.update(NVIDIA_COMMON_ARGS)
    return module_args


def main():
    module = AnsibleModule(
        argument_spec=get_module_args(),
        supports_check_mode=True,
    )

    client = create_api_client(module)
    params = module.params

    if params.get("org_id"):
        try:
            resource = client.get(f"/v1/orgs/{params['org_id']}")
            module.exit_json(changed=False, org=to_dict(resource))
        except NvidiaApiError as exc:
            if exc.status == 404:
                module.exit_json(changed=False, org={})
            module.fail_json(msg=str(exc))
    else:
        try:
            result = client.get("/v1/orgs")
            items = result.get("data", result.get("items", []))
            module.exit_json(changed=False, orgs=[to_dict(i) for i in items])
        except NvidiaApiError as exc:
            module.fail_json(msg=str(exc))


if __name__ == "__main__":
    main()
