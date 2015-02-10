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
        response = {
            "results": [{"id": "111",
                         "name": "cluster_01", }]
        }
        lister = mock.Mock(return_value=response)
        self.app.client_manager.mq.clusters.list = lister
        cmd = clusters.ListClustersCommand(self.app, self.namespace)

        parsed_args = self.check_parser(cmd, arglist, verifylist)
        result = cmd.take_action(parsed_args)

        lister.assert_called_with()
        self.assertEqual(['id', 'name'], result[0])


class TestCreateCluster(base.TestCueBase):
    def test_create_cluster(self):
        """test to create a new cluster with all input arguments"""
        cluster_name = "test_Cluster"
        cluster_network_id = "111222333445"
        cluster_flavor = "1"
        cluster_size = "2"
        response = {"id": "222",
                    "project_id": "test",
                    "network_id": cluster_network_id,
                    "name": cluster_name,
                    "status": "BUILDING",
                    "flavor": cluster_flavor,
                    "size": cluster_size,
                    "volume_size": "1024",
                    "deleted": "0",
                    "created_at": "2015-02-04 00:35:02",
                    "updated_at": "2015-02-04 00:35:02",
                    "deleted_at": ""
                    }

        arglist = ["--name", cluster_name, "--nic", cluster_network_id,
                   "--flavor", cluster_flavor, "--size", cluster_size]
        verifylist = [
        ]

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
