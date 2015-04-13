#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import mock

from cueclient.tests import base
from cueclient.v1.cli import clusters


class TestListClusters(base.TestCueBase):
    def test_list_clusters(self):
        """test cluster list."""
        arglist = [
        ]
        verifylist = [
        ]
        response = {"id": "111",
                    "name": "cluster_01",
                    "status": "BUILDING"}

        lister = mock.Mock(return_value=response)
        self.app.client_manager.mq.clusters.list = lister
        cmd = clusters.ListClustersCommand(self.app, self.namespace)

        parsed_args = self.check_parser(cmd, arglist, verifylist)
        result = cmd.take_action(parsed_args)

        self.assertEqual(['id', 'name', 'status', 'end_points'], result[0])


class TestCreateCluster(base.TestCueBase):

    cluster_name = "test_Cluster"
    cluster_network_id = "111222333445"
    cluster_flavor = "1"
    cluster_size = "2"

    def test_create_cluster(self):
        """test to create a new cluster with all required input arguments"""

        arglist = ["--name", self.cluster_name,
                   "--nic", self.cluster_network_id,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = [
            ('name', self.cluster_name),
            ('nic', self.cluster_network_id),
            ('flavor', self.cluster_flavor),
            ('size', self.cluster_size)
        ]
        response = {"id": "222",
                    "project_id": "test",
                    "network_id": self.cluster_network_id,
                    "name": self.cluster_name,
                    "status": "BUILDING",
                    "flavor": self.cluster_flavor,
                    "size": self.cluster_size,
                    "volume_size": "1024",
                    "deleted": "0",
                    "created_at": "2015-02-04 00:35:02",
                    "updated_at": "2015-02-04 00:35:02",
                    "deleted_at": ""}

        mocker = mock.Mock(return_value=response)
        self.app.client_manager.mq.clusters.create = mocker
        cmd = clusters.CreateClusterCommand(self.app, self.namespace)

        parsed_args = self.check_parser(cmd, arglist, verifylist)
        result = list(cmd.take_action(parsed_args))

        filtered = [('created_at', 'deleted', 'deleted_at', 'flavor', 'id',
                     'name', 'network_id', 'project_id', 'size', 'status',
                     'updated_at', 'volume_size'),
                    ('2015-02-04 00:35:02', '0', '', '1',
                     '222', 'test_Cluster',
                     '111222333445', 'test', '2', 'BUILDING',
                     '2015-02-04 00:35:02', '1024')]

        self.assertEqual(filtered, result)

    def test_create_cluster_without_name(self):
        """test create cluster without 'name' argument."""

        arglist = ["--nic", self.cluster_network_id,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.create = mocker
        cmd = clusters.CreateClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)

    def test_create_cluster_without_nic(self):
        """test create cluster without 'network_id' argument."""

        arglist = ["--name", self.cluster_name,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.create = mocker
        cmd = clusters.CreateClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)

    def test_create_cluster_without_flavor(self):
        """test create cluster without 'flavor' argument."""

        arglist = ["--name", self.cluster_name,
                   "--nic", self.cluster_network_id,
                   "--size", self.cluster_size]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.create = mocker
        cmd = clusters.CreateClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)

    def test_create_cluster_without_size(self):
        """test create cluster without 'size' argument."""

        response = {
        }

        arglist = ["--name", self.cluster_name,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=response)
        self.app.client_manager.mq.clusters.create = mocker
        cmd = clusters.CreateClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)


class TestShowCluster(base.TestCueBase):

    def test_show_cluster(self):
        """test show cluster with correct cluster id"""
        cluster_id = 'e531f2b3-3d97-42c0-b3b5-b7b6ab532018'

        response = {
            "id": cluster_id,
            "project_id": "test",
            "network_id": "26477575",
            "name": "test_cluster",
            "status": "BUILDING",
            "flavor": "1",
            "size": "2",
            "volume_size": "1024"
        }

        arglist = [cluster_id]

        verifylist = [
        ]

        mocker = mock.Mock(return_value=response)
        self.app.client_manager.mq.clusters.get = mocker
        cmd = clusters.ShowClusterCommand(self.app, self.namespace)
        parsed_args = self.check_parser(cmd, arglist, verifylist)
        result = list(cmd.take_action(parsed_args))

        filtered = [('flavor', 'id', 'name', 'network_id', 'project_id',
                     'size', 'status', 'volume_size'),
                    ('1', 'e531f2b3-3d97-42c0-b3b5-b7b6ab532018',
                     'test_cluster', '26477575', 'test', '2',
                    'BUILDING', '1024')]

        self.assertEqual(filtered, result)

    def test_show_cluster_without_id(self):
        """test show cluster without specifying cluster id"""

        arglist = [
        ]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.get = mocker
        cmd = clusters.ShowClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)


class TestDeleteCluster(base.TestCueBase):
    """test delete cluster with correct cluster id"""
    def test_delete_cluster(self):
        cluster_id = 'e531f2b3-3d97-42c0-b3b5-b7b6ab532018'
        arglist = [
            cluster_id
        ]
        verifylist = [
        ]
        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.delete = mocker
        cmd = clusters.DeleteClusterCommand(self.app, self.namespace)

        parsed_args = self.check_parser(cmd, arglist, verifylist)
        result = cmd.take_action(parsed_args)

        mocker.assert_called_with(cluster_id)
        self.assertEqual(None, result)

    def test_delete_cluster_without_id(self):
        """test show cluster without giving cluster id"""
        arglist = [
        ]
        verifylist = [
        ]

        mocker = mock.Mock(return_value=None)
        self.app.client_manager.mq.clusters.get = mocker
        cmd = clusters.DeleteClusterCommand(self.app, self.namespace)

        self.assertRaises(SystemExit, self.check_parser,
                          cmd, arglist, verifylist)
