#   Copyright 2012-2013 OpenStack Foundation
#
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
import json
import os

import pkg_resources


def env(*vars, **kwargs):
    """Search for the first defined of possibly many env vars

    Returns the first environment variable defined in vars, or
    returns the default defined in kwargs.

    """
    for v in vars:
        value = os.environ.get(v)
        if value:
            return value
    return kwargs.get('default', '')


def get_item_properties(item, fields, mixed_case_fields=[], formatters={}):
    """Return a tuple containing the item properties.

    :param item: a single dict resource
    :param fields: tuple of strings with the desired field names
    :param mixed_case_fields: tuple of field names to preserve case
    :param formatters: dictionary mapping field names to callables
       to format the values
    """
    row = []
    for field in fields:
        if field in mixed_case_fields:
            field_name = field.replace(' ', '_')
        else:
            field_name = field.lower().replace(' ', '_')
        data = item[field_name] if field_name in item else ''
        if field in formatters:
            row.append(formatters[field](data))
        else:
            row.append(data)
    return tuple(row)


def resource_string(*args, **kwargs):
    """Return specified resource as a string"""
    if len(args) == 0:
        raise ValueError()

    package = kwargs.pop('package', None)

    if not package:
        package = 'cueclient'

    resource_path = os.path.join('resources', *args)

    if not pkg_resources.resource_exists(package, resource_path):
        # TODO(ap): add exceptions
        # raise exceptions.ResourceNotFound('Could not find the requested '
        # 'resource: %s' % resource_path)
        pass

    return pkg_resources.resource_string(package, resource_path)


def load_schema(version, name, package=None):
    """Load json schema from resources"""
    schema_string = resource_string('schemas', version, '%s.json' % name,
                                    package=package)

    return json.loads(schema_string)