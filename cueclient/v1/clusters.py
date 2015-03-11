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
from cueclient import controller
from cueclient import utils
from cueclient import warlock

Cluster = warlock.model_factory(utils.load_schema('v1', 'cluster'))


class ClusterController(controller.Controller):
    def create(self, name, nic, flavor, size, volume_size):
        data = {
            "network_id": nic,
            "name": name,
            "flavor": flavor,
            "size": size,
            "volume_size": volume_size
        }
        url = self.build_url("/clusters")

        return Cluster(self._post(url, json=data)['cluster'])

    def list(self, marker=None, limit=None, params=None):
        url = self.build_url("/clusters", marker, limit, params)

        response = self._get(url, "clusters")
        return [Cluster(i) for i in response]

    def get(self, cluster_id):
        url = self.build_url("/clusters/%s" % cluster_id)

        return Cluster(self._get(url)['cluster'])

    def update(self, cluster_id, values):
        data = {
            "cluster": values
        }

        url = self.build_url("/clusters/%s" % cluster_id)

        return self._patch(url, data=data)

    def delete(self, cluster_id):
        url = self.build_url("/clusters/%s" % cluster_id)

        return self._delete(url)
