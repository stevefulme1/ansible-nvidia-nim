> **EXPERIMENTAL** - This collection is a proof of concept and is not production ready.
> Modules may use placeholder API endpoints and have not been validated against real infrastructure.
> Do not use in production environments.

    # stevefulme1.nvidia_nim

    Ansible Collection for NVIDIA NIM (Inference Microservices). Provides modules for managing NIM endpoints, deployments, models, caching, scaling policies, and monitoring.

    ## Requirements

    - Ansible >= 2.16
    - Python >= 3.9
    - `requests` Python library

    ## Modules

    - `stevefulme1.nvidia_nim.nim_model` - Manage NIM models
- `stevefulme1.nvidia_nim.nim_model_info` - Retrieve NIM model details
- `stevefulme1.nvidia_nim.nim_endpoint` - Manage NIM inference endpoints
- `stevefulme1.nvidia_nim.nim_endpoint_info` - Retrieve NIM endpoint details
- `stevefulme1.nvidia_nim.nim_deployment` - Manage NIM deployments
- `stevefulme1.nvidia_nim.nim_deployment_info` - Retrieve NIM deployment details
- `stevefulme1.nvidia_nim.nim_profile` - Manage NIM inference profiles
- `stevefulme1.nvidia_nim.nim_profile_info` - Retrieve NIM profile details
- `stevefulme1.nvidia_nim.nim_scaling_policy` - Manage NIM scaling policies
- `stevefulme1.nvidia_nim.nim_health_check` - Run NIM endpoint health checks
- `stevefulme1.nvidia_nim.nim_cache` - Manage NIM model caches
- `stevefulme1.nvidia_nim.nim_cache_info` - Retrieve NIM cache details
- `stevefulme1.nvidia_nim.nim_metrics` - Retrieve NIM endpoint metrics
- `stevefulme1.nvidia_nim.nim_org` - Manage NIM organizations
- `stevefulme1.nvidia_nim.nim_org_info` - Retrieve NIM organization details

    ## Roles

    - `nim_deploy` - Deploy NVIDIA NIM inference endpoints
- `nim_monitor` - Monitor NVIDIA NIM endpoint health and performance
- `nim_scale` - Scale NVIDIA NIM deployments

    ## EDA

    - `nim_events` - Watch NIM endpoints for health and scaling events

    ## License

    GPL-3.0-or-later
