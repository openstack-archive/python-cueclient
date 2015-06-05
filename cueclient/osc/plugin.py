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
from cueclient import utils

from openstackclient.common import utils as oscutils


DEFAULT_MB_API_VERSION = '1'

API_NAME = 'mb'
API_VERSION_OPTION = 'os_mb_api_version'
API_VERSIONS = {
    '1': 'cueclient.v1.client.Client',
}


def make_client(instance):
    cls = oscutils.get_client_class(
        API_NAME, instance._api_version[API_NAME],
        API_VERSIONS)
    return cls(session=instance.session)


def build_option_parser(parser):
    """Hook to add global options."""
    parser.add_argument(
        '--os-mb-api-version',
        metavar='<mb-api-version>',
        default=utils.env(
            'OS_MB_API_VERSION',
            default=DEFAULT_MB_API_VERSION),
        help='MB API version, default=' +
             DEFAULT_MB_API_VERSION +
             ' (Env: OS_MB_API_VERSION)')

    return parser
