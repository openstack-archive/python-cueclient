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
from cueclient import client


class ClusterController(client.Controller):
    def create(self, name, nic, description=None, flavor='m1.medium',
               volume_size=1024):
        data = {
            "name": name,
        }

        url = self.build_url("/clusters")

        return self._post(url, data=data)

    def list(self, marker=None, limit=None, params=None):
        url = self.build_url("/clusters", marker, limit, params)

        return self._get(url)

    def get(self, cluster_id):
        url = self.build_url("/clusters/%s" % cluster_id)

        return self._get(url)

    def update(self, cluster_id, values):
        data = {
            "cluster": values
        }

        url = self.build_url("/clusters/%s" % cluster_id)

        return self._patch(url, data=data)

    def delete(self, cluster_id):
        url = self.build_url("/clusters/%s" % cluster_id)

        return self._delete(url)
