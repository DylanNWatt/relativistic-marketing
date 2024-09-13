## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | ~> 2.14.0 |
| <a name="requirement_kubernetes"></a> [kubernetes](#requirement\_kubernetes) | ~> 2.21.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_airbyte"></a> [airbyte](#module\_airbyte) | ./modules/airbyte | n/a |
| <a name="module_airflow"></a> [airflow](#module\_airflow) | ./modules/airflow | n/a |
| <a name="module_analytics_postgres"></a> [analytics\_postgres](#module\_analytics\_postgres) | ./modules/analytics_postgres | n/a |
| <a name="module_argo_cd"></a> [argo\_cd](#module\_argo\_cd) | ./modules/argo_cd | n/a |
| <a name="module_argo_workflows"></a> [argo\_workflows](#module\_argo\_workflows) | ./modules/argo_workflows | n/a |
| <a name="module_configuration_postgres"></a> [configuration\_postgres](#module\_configuration\_postgres) | ./modules/configuration_postgres | n/a |
| <a name="module_dagster"></a> [dagster](#module\_dagster) | ./modules/dagster | n/a |
| <a name="module_jitsu"></a> [jitsu](#module\_jitsu) | ./modules/jitsu | n/a |
| <a name="module_kestra"></a> [kestra](#module\_kestra) | ./modules/kestra | n/a |
| <a name="module_kubernetes_dashboard"></a> [kubernetes\_dashboard](#module\_kubernetes\_dashboard) | ./modules/kubernetes-dashboard | n/a |
| <a name="module_lightdash"></a> [lightdash](#module\_lightdash) | ./modules/lightdash | n/a |
| <a name="module_prometheus"></a> [prometheus](#module\_prometheus) | ./modules/prometheus | n/a |
| <a name="module_superset"></a> [superset](#module\_superset) | ./modules/superset | n/a |
| <a name="module_tooljet"></a> [tooljet](#module\_tooljet) | ./modules/tooljet | n/a |
| <a name="module_windmill"></a> [windmill](#module\_windmill) | ./modules/windmill | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_airbyte"></a> [airbyte](#input\_airbyte) | Configuration for Airbyte deployment | <pre>object({<br>    enabled = bool<br>    postgres = object({<br>      host     = string<br>      port     = number<br>      name     = string<br>      user     = string<br>      password = string<br>    })<br>    subdomain = string<br>    userlist  = string<br>  })</pre> | <pre>{<br>  "enabled": false,<br>  "postgres": {<br>    "host": null,<br>    "name": null,<br>    "password": null,<br>    "port": 5432,<br>    "user": null<br>  },<br>  "subdomain": "airbyte",<br>  "userlist": ""<br>}</pre> | no |
| <a name="input_airflow"></a> [airflow](#input\_airflow) | Configuration for Apache Airflow deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_analytics_postgres"></a> [analytics\_postgres](#input\_analytics\_postgres) | Configuration for Analytics PostgreSQL deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_argo_cd"></a> [argo\_cd](#input\_argo\_cd) | Configuration for Argo CD deployment | <pre>object({<br>    enabled   = bool<br>    subdomain = string<br>  })</pre> | <pre>{<br>  "enabled": false,<br>  "subdomain": "argocd"<br>}</pre> | no |
| <a name="input_argo_workflows"></a> [argo\_workflows](#input\_argo\_workflows) | Configuration for Argo Workflows deployment | <pre>object({<br>    enabled   = bool<br>    subdomain = string<br>    rbac_rule = string<br>  })</pre> | <pre>{<br>  "enabled": false,<br>  "rbac_rule": "false",<br>  "subdomain": "argo-workflows"<br>}</pre> | no |
| <a name="input_dagster"></a> [dagster](#input\_dagster) | Configuration for Dagster deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_domain_config"></a> [domain\_config](#input\_domain\_config) | Domain configuration for deployments | <pre>object({<br>    deployment_domain = string<br>    zone_domain       = string<br>  })</pre> | <pre>{<br>  "deployment_domain": "",<br>  "zone_domain": ""<br>}</pre> | no |
| <a name="input_google_oauth"></a> [google\_oauth](#input\_google\_oauth) | Google OAuth configuration for authentication | <pre>object({<br>    client_id     = string<br>    client_secret = string<br>  })</pre> | <pre>{<br>  "client_id": "",<br>  "client_secret": ""<br>}</pre> | no |
| <a name="input_jitsu"></a> [jitsu](#input\_jitsu) | Configuration for Jitsu deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_kestra"></a> [kestra](#input\_kestra) | Configuration for Kestra deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_kubernetes_config"></a> [kubernetes\_config](#input\_kubernetes\_config) | Kubernetes configuration settings | <pre>object({<br>    config_path = string<br>  })</pre> | <pre>{<br>  "config_path": "~/.kube/config"<br>}</pre> | no |
| <a name="input_kubernetes_dashboard"></a> [kubernetes\_dashboard](#input\_kubernetes\_dashboard) | Configuration for Kubernetes Dashboard deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_lightdash"></a> [lightdash](#input\_lightdash) | Configuration for Lightdash deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_superset"></a> [superset](#input\_superset) | Configuration for Apache Superset deployment | <pre>object({<br>    enabled         = bool<br>    default_user    = string<br>    default_password = string<br>    secret_key      = string<br>  })</pre> | <pre>{<br>  "default_password": "admin",<br>  "default_user": "admin@superset.com",<br>  "enabled": false,<br>  "secret_key": "YOUR_OWN_RANDOM_GENERATED_SECRET_KEY"<br>}</pre> | no |
| <a name="input_tooljet"></a> [tooljet](#input\_tooljet) | Configuration for Tooljet deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |
| <a name="input_windmill"></a> [windmill](#input\_windmill) | Configuration for Windmill deployment | <pre>object({<br>    enabled = bool<br>  })</pre> | <pre>{<br>  "enabled": false<br>}</pre> | no |

## Outputs

No outputs.
