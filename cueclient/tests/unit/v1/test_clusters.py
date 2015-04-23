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

from cueclient.tests import base
from cueclient.v1.cli import clusters


class TestListClusters(base.TestCueBase):

    def test_list_clusters(self):
        """test cluster list."""
        arglist = []
        verifylist = []
        expected = {'00000000-0000-0000-0000-000000001234':
                    ('00000000-0000-0000-0000-000000001234',
                     'test-cluster', 'ACTIVE', []),
                    '00000000-0000-0000-0000-000000005678':
                    ('00000000-0000-0000-0000-000000005678',
                     'test-cluster2', 'BUILDING', [])}

        result = self.execute(clusters.ListClustersCommand, arglist,
                              verifylist)
        self.assertEqual(['id', 'name', 'status', 'end_points'], result[0])
        self.assert_called('GET', '/clusters')
        for cluster in result[1]:
            self.assertEqual(expected[cluster[0]], cluster)


class TestShowCluster(base.TestCueBase):

    def test_show_cluster(self):
        """test cluster show."""
        cluster_id = '00000000-0000-0000-0000-000000001234'
        arglist = [cluster_id]
        verifylist = []

        result = self.execute(clusters.ShowClusterCommand, arglist, verifylist)
        expected = [('created_at', 'end_points', 'flavor', 'id', 'name',
                     'network_id', 'size', 'status'),
                    (u'2015-01-01T00:00:00+00:00', [], '1',
                     '00000000-0000-0000-0000-000000001234',
                     'test-cluster', [u'05860da0-e2bd-4315-9cfb-7dd6e9963cd9'],
                     1, 'ACTIVE')]
        self.assert_called('GET', '/clusters/' + cluster_id)
        self.assertEqual(expected, result)

    def test_show_cluster_without_id(self):
        """test show cluster without specifying cluster id"""

        arglist = []
        verifylist = []

        self.assertRaises(SystemExit, self.execute,
                          clusters.ShowClusterCommand, arglist, verifylist)


class TestCreateCluster(base.TestCueBase):

    cluster_name = "test_Cluster"
    cluster_network_id = "9d6708ee-ea48-4e78-bef6-b50b48405091"
    cluster_flavor = "1"
    cluster_size = "2"

    def test_create_cluster(self):
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

        self.execute(clusters.CreateClusterCommand, arglist, verifylist)
        self.assert_called('POST', '/clusters')

    def test_create_cluster_without_name(self):
        """test create cluster without 'name' argument."""

        arglist = ["--nic", self.cluster_network_id,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = []
        self.assertRaises(SystemExit, self.execute,
                          clusters.CreateClusterCommand, arglist, verifylist)

    def test_create_cluster_without_nic(self):
        """test create cluster without 'network_id' argument."""

        arglist = ["--name", self.cluster_name,
                   "--flavor", self.cluster_flavor,
                   "--size", self.cluster_size]
        verifylist = []
        self.assertRaises(SystemExit, self.execute,
                          clusters.CreateClusterCommand, arglist, verifylist)

    def test_create_cluster_without_flavor(self):
        """test create cluster without 'flavor' argument."""

        arglist = ["--name", self.cluster_name,
                   "--nic", self.cluster_network_id,
                   "--size", self.cluster_size]
        verifylist = []
        self.assertRaises(SystemExit, self.execute,
                          clusters.CreateClusterCommand, arglist, verifylist)

    def test_create_cluster_without_size(self):
        """test create cluster without 'size' argument."""

        arglist = ["--name", self.cluster_name,
                   "--nic", self.cluster_network_id,
                   "--flavor", self.cluster_flavor]
        verifylist = []
        self.assertRaises(SystemExit, self.execute,
                          clusters.CreateClusterCommand, arglist, verifylist)


class TestDeleteCluster(base.TestCueBase):

    def test_delete_cluster_without_id(self):
        """test delete cluster without giving cluster id"""
        arglist = []
        verifylist = []
        self.assertRaises(SystemExit, self.execute,
                          clusters.DeleteClusterCommand, arglist, verifylist)

    def test_delete_cluster(self):
        """test delete cluster"""
        cluster_id = '00000000-0000-0000-0000-000000001234'
        arglist = [cluster_id]
        verifylist = []
        result = self.execute(clusters.DeleteClusterCommand, arglist,
                              verifylist)
        self.assert_called('DELETE', '/clusters/' + cluster_id)
        self.assertEqual(None, result)