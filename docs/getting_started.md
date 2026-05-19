# Getting Started with stevefulme1.nvidia_nim

>-

## Installation

```bash
ansible-galaxy collection install stevefulme1.nvidia_nim
```

## Requirements

- Ansible >= 2.16
- Python >= 3.12

## Authentication

Refer to individual module documentation for authentication requirements.

## Quick Example

```yaml
---
- name: Example playbook
  hosts: localhost
  connection: local
  gather_facts: false
  collections:
    - stevefulme1.nvidia_nim
  tasks:
    - name: Get info
      stevefulme1.nvidia_nim.nim_cache:
        api_url: "{{ api_url }}"
        api_token: "{{ api_token }}"
      register: result

    - name: Show result
      ansible.builtin.debug:
        var: result
```

## Collection Contents

- **Modules**: 15
- **Roles**: 3
- **EDA plugins**: 1

## Next Steps

- Browse the module documentation: `ansible-doc stevefulme1.nvidia_nim.<module_name>`
- Check the [README](../README.md) for the full module and role list
- Review [CONTRIBUTING.md](../CONTRIBUTING.md) to contribute
