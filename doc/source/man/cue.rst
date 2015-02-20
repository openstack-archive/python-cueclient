====
cue
====


SYNOPSIS
========

  `cue` [options] <command> [command-options]

  `cue help`

  `cue help` <command>


DESCRIPTION
===========

`cue` is a command line client for controlling OpenStack Cue, the messaging service.

Before you can issue commands with `cue`, you must ensure that your
environment contains the necessary variables so that you can prove to the CLI
who you are and what credentials you have to issue the commands.

OPTIONS
=======

To get a list of available commands and options run::

    cue help

To get usage and options of a command run::

    cue help <command>

EXAMPLES
========

Get information about cluster create command::

    help cue cluster create

List available clusters::

    help cue cluster list

View cluster information::

    help cue cluster show

Delete clusters::

    help cue cluster delete

