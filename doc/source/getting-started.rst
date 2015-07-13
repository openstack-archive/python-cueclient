..
    Copyright 2014 Hewlett-Packard Development Company, L.P.

    Licensed under the Apache License, Version 2.0 (the "License"); you may
    not use this file except in compliance with the License. You may obtain
    a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations
    under the License.

.. _getting-started:

===============
Getting Started
===============

.. _Development Environment:

The python-cueclient can be used either as a command line tool or as a binding to access Cue.


Installing Cue Client from source
=================================

.. index::
   double: install; python-cueclient


1. Clone the CueClient repo from GitHub

::

   $ git clone https://github.com/openstack/python-cueclient.git
   $ cd python-cueclient


2. Setup virtualenv

.. note::
   This is an optional step, but will allow CueClient's dependencies
   to be installed in a contained environment that can be easily deleted
   if you choose to start over or uninstall Cue.

::

   $ virtualenv --no-site-packages .venv
   $ . .venv/bin/activate


3. Install CueClient and its dependencies

::

   $ pip install -r requirements.txt -r test-requirements.txt
   $ python setup.py develop


Installation to use as Command Line Tool
----------------------------------------
4. To access the shell for cue client 'python-openstackclient' has to be installed.

::

   $ pip install python-openstackclient


.. note::
   This step can be skipped if you choose to use python-cueclient as only a binding to Cue API.
