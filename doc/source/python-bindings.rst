===============
Python Bindings
===============

The python-cueclient can be used to interact with the Cue API from any other
python program.


Introduction
============

Below is a simple example of how to instantiate and perform basic tasks using
the bindings.

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session
    from cueclient.v1 import client

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

    session = keystone_session.Session(auth=auth)

    # Create an instance of the client
    cue_client = client.Client(session=session)

    # Cluster List - returns list of cluster objects
    list_response = cue_client.clusters.list()

    # Iterate the list, printing some useful information
    for cluster in list_response:

        print "Cluster ID: %s \t Name: %s \t NetworkId: %s \t Flavor: %s \t Size: %s" % \
               (cluster.id, cluster.name, cluster.network_id, cluster.flavor, cluster.size)

And the output this program might produce:

.. code-block:: console

  $ python /example.py
  Cluster ID: 213cdd06-c361-4cca-93b5-7ed651d46936 	 Name: test_binding2 	 NetworkId: 33333 	 Flavor: 1 	 Size: 2
  Cluster ID: 24f299fd-0509-4218-bf80-6c0481452480 	 Name: test_binding4 	 NetworkId: 44444 	 Flavor: 1 	 Size: 2


Authentication
==============

Cue supports Keystone authentication.

Keystone Authentication
-----------------------

Below is a sample of standard authentication with keystone v3:

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

Cue Functions
=============

Cluster List
------------

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session
    from cueclient.v1 import client

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

    session = keystone_session.Session(auth=auth)
    cue_client = client.Client(session=session)

    # Cluster List
    list_response = cue_client.clusters.list()


Cluster Show
------------

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session
    from cueclient.v1 import client

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

    session = keystone_session.Session(auth=auth)
    cue_client = client.Client(session=session)

    cluster_id = "0a352f9a-8aa8-411e-9d6d-4e6217d70afd"

    # Cluster Show
    show_response = cue_client.clusters.get(cluster_id)


Cluster Create
--------------

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session
    from cueclient.v1 import client

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

    session = keystone_session.Session(auth=auth)
    cue_client = client.Client(session=session)

    # Cluster create
    create_response = cue_client.clusters.create(name="test_binding5",
                        nic="55555", flavor="1",size="2",volume_size="0")

Cluster Delete
--------------

.. code-block:: python

    #!/usr/bin/env python

    from keystoneclient.auth.identity import v3 as keystone_v3_auth
    from keystoneclient import session as keystone_session
    from cueclient.v1 import client

    auth = keystone_v3_auth.Password(
            auth_url="http://example.com:5000/v3",
            username="admin",
            password="password",
            project_name="admin",
            project_domain_name="default",
            user_domain_name="default"
    )

    session = keystone_session.Session(auth=auth)
    cue_client = client.Client(session=session)

    delete_id = "dc86d96f-6b37-4e2d-9805-4542450f427d"

    # Cluster Delete
    delete_response = cue_client.clusters.delete(delete_id)

