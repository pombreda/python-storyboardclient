# Copyright (c) 2014 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from storyboardclient import base
from storyboardclient.v1 import project_groups
from storyboardclient.v1 import projects
from storyboardclient.v1 import teams
from storyboardclient.v1 import users


class Client(base.BaseClient):
    """A client class for StoryBoard.

    Usage example:
    @code:
        from storyboard.v1 import client

        storyboard = client.Client("https://storyboard.openstack.org/api/v1",
                                   "mytoken")
    """

    def __init__(self, api_url=None, access_token=None):
        """Sets up a client with endpoint managers.

        :param api_url: (Optional) Full API url. Defaults to
        https://storyboard.openstack.org/api/v1
        :param access_token: (Optional) OAuth2 access token. If skipped only
        public read-only endpoint will be available. All other requests will
        fail with Unauthorized error.
        :return: a client instance.
        """
        super(Client, self).__init__(api_url=api_url,
                                     access_token=access_token)

        self.teams = teams.TeamsManager(self)
        self.projects = projects.ProjectsManager(self)
        self.project_groups = project_groups.ProjectGroupsManager(self)
        self.users = users.UsersManager(self)
