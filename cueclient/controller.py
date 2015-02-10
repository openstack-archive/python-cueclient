# Copyright 2012 Managed I.T.
#
# Author: Kiall Mac Innes <kiall@managedit.ie>
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
import abc
import json
from urllib import urlencode

import six


@six.add_metaclass(abc.ABCMeta)
class Controller(object):

    def __init__(self, client):
        self.client = client

    def build_url(self, url, marker=None, limit=None, params=None):
        params = params or {}

        if marker is not None:
            params['marker'] = marker
        if limit is not None:
            params['limit'] = limit

        q = urlencode(params) if params else ''
        return '%(url)s%(params)s' % {
            'url': url,
            'params': '?%s' % q
        }

    def _serialize(self, kwargs):
        if 'data' in kwargs:
            kwargs['data'] = json.dumps(kwargs['data'])

    def _post(self, url, response_key=None, **kwargs):
        self._serialize(kwargs)

        resp = self.client.session.post(url, **kwargs)
        data = resp.json()

        if response_key in data:
            return data[response_key]
        return data

    def _get(self, url, response_key=None):
        resp = self.client.session.get(url)
        data = resp.json()

        if response_key in data:
            return data[response_key]
        return data

    def _patch(self, url, response_key=None, **kwargs):
        self._serialize(kwargs)

        resp = self.client.session.patch(url, **kwargs)
        data = resp.json()

        if response_key in data:
            return data[response_key]
        return data

    def _put(self, url, response_key=None, **kwargs):
        self._serialize(kwargs)

        resp = self.client.session.put(url, **kwargs)
        data = resp.json()

        if response_key in data:
            return data[response_key]
        return data

    def _delete(self, url):
        self.client.session.delete(url)


@six.add_metaclass(abc.ABCMeta)
class CrudController(Controller):

    @abc.abstractmethod
    def list(self, *args, **kw):
        """
        List a resource
        """

    @abc.abstractmethod
    def get(self, *args, **kw):
        """
        Get a resouce
        """

    @abc.abstractmethod
    def create(self, *args, **kw):
        """
        Create a resource
        """

    @abc.abstractmethod
    def update(self, *args, **kw):
        """
        Update a resource
        """

    @abc.abstractmethod
    def delete(self, *args, **kw):
        """
        Delete a resource
        """
