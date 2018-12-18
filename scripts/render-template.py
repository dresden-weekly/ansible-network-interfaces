#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

import jinja2
import yaml

with open(".information.yml") as fp:
    information = yaml.load(fp)

loader = jinja2.FileSystemLoader(searchpath="")
environment = jinja2.Environment(loader=loader, keep_trailing_newline=True)

template = environment.get_template(sys.argv[1])
result = template.render({
    "ansible_role_name": information.get("ansible_role_name", "NONE"),
    "molecule_needs_docker": information.get("molecule_needs_docker", False),
    "travis_decrypt_key": information.get("travis_decrypt_key", "NONE")
})
with open(sys.argv[1], "w+") as fp:
    fp.write(result)
