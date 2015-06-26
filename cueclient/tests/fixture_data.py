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

import fixtures
from keystoneclient import session
from six.moves.urllib import parse

from cueclient.v1 import client

MESSAGE_BROKER_URL = 'http://message.broker'


class V1(fixtures.Fixture):

    base_url = 'clusters'
    json_headers = {'Content-Type': 'application/json'}

    def __init__(self, requests):
        super(V1, self).__init__()
        self.client = None
        self.requests = requests

    def setUp(self):
        super(V1, self).setUp()

        self.cluster_1234 = {
            "name": "test-cluster",
            "id": "00000000-0000-0000-0000-000000001234",
            "size": 1,
            "network_id": ["05860da0-e2bd-4315-9cfb-7dd6e9963cd9"],
            "created_at": "2015-01-01T00:00:00+00:00",
            "endpoints": [],
            "flavor": "1",
            "status": "ACTIVE",
        }

        self.cluster_5678 = {
            "name": "test-cluster2",
            "id": "00000000-0000-0000-0000-000000005678",
            "size": 3,
            "network_id": ["05567na0-f7aa-6820-7afcd-7dd6e9963cd9"],
            "created_at": "2015-01-01T00:00:00+00:00",
            "endpoints": [],
            "flavor": "1",
            "status": "BUILDING",
        }

        self.new_cluster = {
            "name": "new-test-cluster",
            "id": "00000000-0000-0000-0000-000000009012",
            "size": 3,
            "network_id": ["05567na0-f7aa-6820-7afcd-7dd6e9963cd9"],
            "created_at": "2015-01-01T00:00:00+00:00",
            "endpoints": [],
            "flavor": "1",
            "status": "BUILDING",
        }

        clusters = [self.cluster_1234, self.cluster_5678]

        self.requests.register_uri('GET', self.url(),
                                   json=clusters,
                                   headers=self.json_headers)

        for cluster in clusters:
            self.requests.register_uri('GET', self.url(cluster['id']),
                                       json=cluster,
                                       headers=self.json_headers)

        for cluster in clusters:
            self.requests.register_uri('DELETE', self.url(cluster['id']),
                                       status_code=202)

        self.requests.register_uri('POST', self.url(),
                                   json=self.new_cluster,
                                   headers=self.json_headers)

        self.client = client.Client(session=session.Session())
        self.client.session.endpoint_override = MESSAGE_BROKER_URL

    def url(self, *args, **kwargs):
        url_args = [MESSAGE_BROKER_URL]

        if self.base_url:
            url_args.append(self.base_url)

        url = '/'.join(str(a).strip('/') for a in tuple(url_args) + args)

        if kwargs:
            url += '?%s' % parse.urlencode(kwargs, doseq=True)

        return url
