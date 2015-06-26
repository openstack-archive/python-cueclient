=====================
Cue Command Line Tool
=====================

The python-cueclient can be used as a command line tool for accessing Cue API.

Credentials
-----------

As with any OpenStack utility, :program:`python-cueclient` requires certain information to
talk to the REST API, username, password, auth url (from where the other required
endpoints are retrieved once you are authenticated).

To provide your access credentials (username, password, tenant name or project_name)
you can pass them on the command line with the ``--os-username``, ``--os-password``,  ``--os-tenant-name`` or ``--os-project-name``
params, but it's easier to just set them as environment variables::

    export OS_USERNAME=<your_username>
    export OS_PASSWORD=<your_password>
    export OS_PROJECT_NAME=<project_name>

You will also need to define the authentication url with ``--os-auth-url``
or set is as an environment variable as well::

    export OS_AUTH_URL=<url_to_openstack_identity>

Since Keystone can return multiple regions in the Service Catalog, you
can specify the one you want with ``--os-region-name`` (or
``export OS_REGION_NAME``). It defaults to the first in the list returned.

Using the command line tool
---------------------------

With enough details now in environment, you can use the cue client to create,list,show or delete cluster(s).

The Openstack Client can be called interactively by simply typing:

.. code-block:: shell-session

    openstack

Cluster Create
--------------

Required fields for 'create' : name, network id , flavor and size.

.. code-block:: shell-session

    (openstack) message-broker cluster create --name cluster_04 --nic 3dd26c0b-03f2-4d2e-ae87-c02d7f33c788 --flavor 2 --size 3
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | created_at  | 2015-02-17T18:25:28+00:00            |
    | endpoints   | []                                   |
    | flavor      | 2                                    |
    | id          | 06d3c0e4-4972-4ca9-91c1-373b1c74e8e1 |
    | name        | cluster_04                           |
    | network_id  | 3dd26c0b-03f2-4d2e-ae87-c02d7f33c788 |
    | size        | 3                                    |
    | status      | BUILDING                             |
    | updated_at  | 2015-02-17T18:25:28+00:00            |
    | volume_size | None                                 |
    +-------------+--------------------------------------+

Cluster Show
------------

Required field for 'show' : cluster-id

.. code-block:: shell-session


    (openstack) message-broker cluster show 06d3c0e4-4972-4ca9-91c1-373b1c74e8e1
    +-------------+--------------------------------------+
    | Field       | Value                                |
    +-------------+--------------------------------------+
    | created_at  | 2015-02-17T18:25:28+00:00            |
    | endpoints   | []                                   |
    | flavor      | 2                                    |
    | id          | 06d3c0e4-4972-4ca9-91c1-373b1c74e8e1 |
    | name        | cluster_04                           |
    | network_id  | 3dd26c0b-03f2-4d2e-ae87-c02d7f33c788 |
    | size        | 3                                    |
    | status      | BUILDING                             |
    | updated_at  | 2015-02-17T18:25:28+00:00            |
    | volume_size | None                                 |
    +-------------+--------------------------------------+

Cluster Delete
--------------

Required field for 'delete' : cluster-id

.. code-block:: shell-session

    (openstack) message-broker cluster delete 06d3c0e4-4972-4ca9-91c1-373b1c74e8e1

Cluster List
------------

.. code-block:: shell-session

    (openstack) message-broker cluster list
    +--------------------------------------+-------------+----------+--------+------+
    | id                                   | name        | status   | flavor | size |
    +--------------------------------------+-------------+----------+--------+------+
    | 06d3c0e4-4972-4ca9-91c1-373b1c74e8e1 | cluster_04  | DELETING | 2      |    3 |
    | 09fa2dc2-7ebb-423f-9726-f45b53f0df99 | cluster_02  | DELETING | 1      |    3 |
    | 2d6a5359-2c45-44bb-baa9-3ccd2a48c217 | cluster_03  | BUILDING | 2      |    2 |
    +--------------------------------------+-------------+----------+--------+------+

Subcommands
-----------

Here are the full list of subcommands:

==================================   ======================================================
subcommand                           Notes
==================================   ======================================================
message-broker cluster create        Create Cluster
message-broker cluster delete        Delete Cluster
message-broker cluster show          Show Cluster
message-broker cluster list          List Clusters
==================================   ======================================================

