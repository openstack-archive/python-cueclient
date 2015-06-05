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
from keystoneclient import adapter

from cueclient.v1.clusters import ClusterController
from cueclient import version


class Client(object):
    def __init__(self, region_name=None, endpoint_type='publicURL',
                 extensions=None, service_type='message-broker',
                 service_name=None, http_log_debug=False, session=None,
                 auth=None):
        self.session = adapter.Adapter(
            session,
            auth=auth,
            region_name=region_name,
            service_type=service_type,
            interface=endpoint_type.rstrip('URL'),
            user_agent='python-cueclient-%s' % version.version_info,
            version=('1'))

        self.clusters = ClusterController(self)
