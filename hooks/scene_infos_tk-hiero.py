# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sgtk

import hiero.core

from sgtk import TankError


HookClass = sgtk.get_hook_baseclass()


class SceneInfos(HookClass):

    """Scene informations. It collects all informations like the current scene,
    the DCC name and the DCC version.
    """

    def collect(self, scene_infos):
        scene_infos.current_scene = self._get_scene_path()
        scene_infos.dcc_name = self._get_dcc_name()
        scene_infos.dcc_version = self._get_dcc_version()
        return scene_infos

    def _get_scene_path(self):
        project = self._get_current_project()
        return project.path().replace("/", os.path.sep)

    def _get_dcc_name(self):
        name = self.parent.engine.host_info.get("name")
        if name == "unknown":
            return "Hiero"
        return name

    def _get_dcc_version(self):
        version = self.parent.engine.host_info.get("version")
        return version

    def _get_current_project(self):
        """
        Returns the current project based on where in the UI the user clicked
        """

        # get the menu selection from hiero engine
        selection = self.parent.engine.get_menu_selection()

        if len(selection) != 1:
            raise TankError("Please select a single Project!")

        if not isinstance(selection[0], hiero.core.Bin):
            raise TankError("Please select a Hiero Project!")

        project = selection[0].project()
        if project is None:
            # apparently bins can be without projects (child bins I think)
            raise TankError("Please select a Hiero Project!")

        return project
