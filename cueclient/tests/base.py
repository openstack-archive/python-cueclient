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

import argparse

import mock
from oslo_serialization import jsonutils
from requests_mock.contrib import fixture as requests_mock_fixture
import six
import testtools

from cueclient.tests.fixture_data import V1


class TestCueBase(testtools.TestCase):
    def setUp(self):
        super(TestCueBase, self).setUp()
        self.requests = self.useFixture(requests_mock_fixture.Fixture())
        fix = V1(self.requests)
        client_fixture = self.useFixture(fix)
        cs = client_fixture.client

        # Build up a fake app
        self.app = mock.Mock()
        self.app.client_manager = mock.Mock()
        self.app.client_manager.mb = cs

    def check_parser(self, cmd, args, verify_args):
        """Test for parsing arguments"""
        cmd_parser = cmd.get_parser('check_parser')
        parsed_args = cmd_parser.parse_args(args)

        for av in verify_args:
            attr, value = av
            if attr:
                self.assertIn(attr, parsed_args)
                self.assertEqual(getattr(parsed_args, attr), value)
        return parsed_args

    def execute(self, cmd_class, arglist, verifylist):
        cmd = cmd_class(self.app, argparse.Namespace())
        parsed_args = self.check_parser(cmd, arglist, verifylist)
        data = cmd.take_action(parsed_args)
        return data

    def assert_called(self, method, path, body=None):
        self.assertEqual(self.requests.last_request.method, method)
        self.assertEqual(self.requests.last_request.path_url, path)

        if body:
            req_data = self.requests.last_request.body
            if isinstance(req_data, six.binary_type):
                req_data = req_data.decode('utf-8')
            if not isinstance(body, six.string_types):
                # json load if the input body to match against is not a string
                req_data = jsonutils.loads(req_data)
            self.assertEqual(req_data, body)
