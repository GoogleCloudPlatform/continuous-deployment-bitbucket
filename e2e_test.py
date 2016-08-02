# Copyright 2015, Google, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable
# law or agreed to in writing, software distributed under the License is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and
# limitations under the License.


import urllib2
import logging
import os

HOST_NAME = os.getenv('CLOUDSDK_CORE_PROJECT', 'http://continuous-deployment-python.appspot.com')
HOST = "http://{hostName}.appspot.com".format(hostName=HOST_NAME)

# [START e2e]
response = urllib2.urlopen("{host}/get_author/ulysses".format(host=HOST))
html = response.read()
assert(html == "James Joyce")
# [END e2e]


