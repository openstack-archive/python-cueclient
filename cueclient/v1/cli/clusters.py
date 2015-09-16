# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from cliff import command
from cliff import lister
from cliff import show
import six

from cueclient import utils

LOG = logging.getLogger(__name__)


class ListClustersCommand(lister.Lister):
    """List Clusters"""

    columns = ['id', 'name', 'status', 'size', 'endpoints']

    def get_parser(self, prog_name):
        parser = super(ListClustersCommand, self).get_parser(prog_name)

        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.mb

        data = client.clusters.list()

        cols = self.columns
        return cols, (utils.get_item_properties(s, cols) for s in data)


class ShowClusterCommand(show.ShowOne):
    """Show Cluster"""
    def get_parser(self, prog_name):
        parser = super(ShowClusterCommand, self).get_parser(prog_name)

        parser.add_argument('id', help="Cluster ID")

        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.mb

        data = client.clusters.get(parsed_args.id)

        return zip(*sorted(six.iteritems(data)))


class CreateClusterCommand(show.ShowOne):
    """Create Cluster"""

    def get_parser(self, prog_name):
        parser = super(CreateClusterCommand, self).get_parser(prog_name)

        parser.add_argument('--name', help="Cluster Name", required=True)
        parser.add_argument('--nic', help="Network to place nodes on",
                            required=True)
        parser.add_argument('--flavor', help="Flavor to use.", required=True)
        parser.add_argument('--size', help="Number of nodes", required=True)

        parser.add_argument('--volume_size', help="Volume size")
        parser.add_argument('--auth',
                            metavar="<type=type,user=user,pass=pass>",
                            help="broker authentication,"
                                 "type=type,user=user,pass=pass")

        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.mb

        auth_type = username = password = None
        if parsed_args.auth:
            for kv_str in parsed_args.auth.split(","):
                k, v = kv_str.split("=")
                if 'type' == k:
                    auth_type = v
                elif 'user' == k:
                    username = v
                elif 'pass' == k:
                    password = v
        if not auth_type:
            auth_type = 'plain'
        data = client.clusters.create(
            name=parsed_args.name,
            nic=parsed_args.nic,
            flavor=parsed_args.flavor,
            size=parsed_args.size,
            volume_size=parsed_args.volume_size,
            auth_type=auth_type,
            username=username,
            password=password)

        return zip(*sorted(six.iteritems(data)))


class SetClusterCommand(command.Command):
    """Set Cluster"""

    def get_parser(self, prog_name):
        parser = super(SetClusterCommand, self).get_parser(prog_name)

        parser.add_argument('id', help="Cluster ID")
        parser.add_argument('--name', help="Cluster Name")
        parser.add_argument('--email', help="Cluster Email")
        parser.add_argument('--ttl', type=int, help="Time To Live (Seconds)")
        description_group = parser.add_mutually_exclusive_group()
        description_group.add_argument('--description', help="Description")
        description_group.add_argument('--no-description', action='store_true')

        parser.add_argument('--masters', help="Cluster Masters", nargs='+')

        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.mb

        data = {}

        # TODO(kiall): API needs updating.. this get is silly
        if parsed_args.name:
            data['name'] = parsed_args.name

        if parsed_args.email:
            data['email'] = parsed_args.email

        if parsed_args.ttl:
            data['ttl'] = parsed_args.ttl

        if parsed_args.no_description:
            data['description'] = None
        elif parsed_args.description:
            data['description'] = parsed_args.description

        if parsed_args.masters:
            data['masters'] = parsed_args.masters

        updated = client.clusters.update(parsed_args.id, data)
        return zip(*sorted(six.iteritems(updated)))


class DeleteClusterCommand(command.Command):
    """Delete Cluster"""

    def get_parser(self, prog_name):
        parser = super(DeleteClusterCommand, self).get_parser(prog_name)

        parser.add_argument('id', help="Cluster ID")

        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.mb
        client.clusters.delete(parsed_args.id)
        LOG.info('Cluster %s was deleted', parsed_args.id)
