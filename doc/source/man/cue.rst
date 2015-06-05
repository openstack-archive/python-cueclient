====
cue
====


SYNOPSIS
========

  `message-broker` [options] <command> [command-options]

  `message-broker help`

  `message-broker help` <command>


DESCRIPTION
===========

`message-broker` is a command line client for controlling OpenStack Cue, the message broker provisioning service.

Before you can issue commands with `message-broker`, you must ensure that your
environment contains the necessary variables so that you can prove to the CLI
who you are and what credentials you have to issue the commands.

OPTIONS
=======

To get a list of available commands and options run::

    message-broker help

To get usage and options of a command run::

    message-broker help <command>

EXAMPLES
========

Get information about cluster create command::

    help message-broker cluster create

List available clusters::

    help message-broker cluster list

View cluster information::

    help message-broker cluster show

Delete clusters::

    help message-broker cluster delete

