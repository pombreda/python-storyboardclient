# Copyright (c) 2015 Mirantis Inc.
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

import mock

from storyboardclient.tests import base as test_base
from storyboardclient.v1 import projects


class ProjectsTestCase(test_base.TestCase):

    @mock.patch("storyboardclient.v1.projects.ProjectsManager._list")
    def test_projects_list(self, mock_private_list):
        mock_private_list.return_value = [
            projects.Project(mock.MagicMock(),
                             info={"name": "test_project"}),
            projects.Project(mock.MagicMock(),
                             info={"name": "test_project_2"})]

        teams_list = projects.ProjectsManager(mock.MagicMock()).list()

        self.assertEqual(2, len(teams_list))

    @mock.patch("storyboardclient.v1.projects.ProjectsManager._post")
    def test_projects_create(self, mock_private_post):
        projects.ProjectsManager(mock.MagicMock()).create(
            name="test_project",
            description="test_description")

        mock_private_post.assert_called_once_with(
            "/projects",
            {"name": "test_project",
             "description": "test_description"})

    @mock.patch("storyboardclient.v1.projects.ProjectsManager._put")
    def test_projects_update(self, mock_private_put):
        projects.ProjectsManager(mock.MagicMock()).update(
            id="project_id",
            name="test_project_updated")

        mock_private_put.assert_called_once_with(
            "/projects/project_id",
            {"name": "test_project_updated"})
