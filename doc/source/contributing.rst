Contributing
============

Code is hosted `on GitHub`_.
Submit bugs to the Cue Client project on `Launchpad`_.
Submit code to the openstack/python-cueclient project using `Gerrit`_.

Here's a quick summary:

Install the git-review package to make life easier

.. code-block:: shell-session

  pip install git-review

Branch, work, & submit:

.. code-block:: shell-session

  # cut a new branch, tracking master
  git checkout --track -b bug/id origin/master
  # work work work
  git add stuff
  git commit
  # rebase/squash to a single commit before submitting
  git rebase -i
  # submit
  git-review

Coding Standards
----------------
Cue Client uses the OpenStack flake8 coding standards guidelines.
These are stricter than pep8, and are run by gerrit on every commit.

You can use tox to check your code locally by running

.. code-block:: shell-session

  # For just flake8 tests
  tox -e flake8
  # For tests + flake8
  tox

.. _on GitHub: https://github.com/openstack/python-cueclient
.. _Launchpad: https://launchpad.net/python-cueclient
.. _Gerrit: http://docs.openstack.org/infra/manual/developers.html#development-workflow

