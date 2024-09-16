Usage
=====

.. _installation:

Usage
-----

Relativistic is designed as a module of modules, where each submodule is a open source project to be deployed, with the top level module being a coodinator.

Each submodule has configuration specific to that project, as well as common elements, such as what ports or domains to expose the site on.

The documentation for each module will cover:

- An overview of the open source project it manages
- Simple configuration options
- Information about how authentication is handled
- An overview of how much compute and storage resources are required
- Project specific information

---- 

Airbyte
========

Overview
--------

Airbyte is an open-source data integration platform that facilitates the seamless synchronization of data from various sources to data warehouses, lakes, and other destinations. It offers a vast connector ecosystem, enabling effortless data flow and transformation, which enhances data accessibility and operational efficiency for teams.

Configuration Options
---------------------

Here are the main configuration options for the Airbyte module:

+---------------------------------------+---------------------------------------+
| Object Structure                      | Default Values                        |
+=======================================+=======================================+
| .. code-block:: text                  | .. code-block:: json                  |
|                                       |                                       |
|   object({                            |   {                                   |
|     enabled = bool                    |     "enabled": false,                 |
|     // Whether the Airbyte module     |     "postgres": {                     |
|     // is enabled or not              |       "host": null,                   |
|     postgres = object({               |       "name": null,                   |
|       host     = string               |       "password": null,               |
|       // Hostname of the Postgres DB  |       "port": 5432,                   |
|       port     = number               |       "user": null                    |
|       // Port number for Postgres     |     },                                |
|       // connection (default: 5432)   |     "subdomain": "airbyte",           |
|       name     = string               |     "userlist": ""                    |
|       // Name of the Airbyte database |   }                                   |
|       user     = string               |                                       |
|       // Username for Postgres auth   |                                       |
|       password = string               |                                       |
|       // Password for Postgres auth   |                                       |
|     })                                |                                       |
|     subdomain = string                |                                       |
|     // Subdomain for accessing the    |                                       |
|     // Airbyte instance               |                                       |
|     userlist  = string                |                                       |
|     // Comma-separated list of        |                                       |
|     // authorized user emails         |                                       |
|   })                                  |                                       |
+---------------------------------------+---------------------------------------+

Authentication
--------------

Airbyte leverages Postgres for authentication purposes. Users must provide valid Postgres credentials, including the host, port, database name, username, and password. These credentials are essential for securing access to the Airbyte instance, ensuring that only authorized personnel can manage data synchronization tasks.

Compute and Storage Resources
-----------------------------

- **Compute**: Airbyte requires moderate CPU resources to handle data synchronization activities. It performs efficiently on standard server configurations, but resource allocation may need to be adjusted based on the volume and frequency of data transfers. Note that airbyte will dynamically spin up new pods, that will be scheduled in the same kubernetes namespace.

- **Storage**: Airbyte requires a Postgres server to store its configuration and data. The size of the server will depend on the number of connectors and the volume of data being transferred, but is minimal. Other services deployed with airbyte, such as Temporal, will use the same Postgres server, with dynamic databases created.

Airbyte also creates its own Minio database for storing log data.

- **Bandwidth**: Bandwidth requirements depend on the number of data sources, the volume of data being transferred, and the frequency of synchronization. Adequate network bandwidth is necessary to prevent bottlenecks and ensure timely data updates.

Project Specific Information
----------------------------

- **Data Synchronization**: Supports both real-time and scheduled data synchronization, ensuring that data across various platforms remains consistent and up-to-date.
- **Connectors**: Provides a wide range of pre-built connectors for popular data sources and destinations, reducing the need for custom integrations.
- **Custom Connectors**: Allows the development and integration of custom connectors to support proprietary or niche data sources and destinations.
- **Monitoring and Logging**: Includes comprehensive monitoring and logging features to track the status and performance of synchronization tasks, aiding in troubleshooting and optimization.
- **Scalability**: Designed to scale horizontally, Airbyte can handle increasing data volumes and synchronization tasks by adding more compute resources as needed.
- **Security**: Implements robust security measures, including encrypted data transfers and secure storage of credentials, to protect data integrity and confidentiality.

Usage Example
-------------

To configure and deploy the Airbyte module, refer to the :doc:`Terraform module for Airbyte <./terraform/modules/airbyte>` in the `out.md` documentation. Below is a sample configuration snippet:

.. code-block:: hcl

    module "airbyte" {
      source      = "./modules/airbyte"
      enabled     = true
      postgres = {
        host     = "postgres.example.com"
        port     = 5432
        name     = "airbyte_db"
        user     = "airbyte_user"
        password = "securepassword"
      }
      subdomain   = "airbyte"
      userlist    = "user1@example.com,user2@example.com"
    }

Ensure that all required parameters are correctly set to enable seamless deployment and operation of the Airbyte module within your infrastructure.