# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

class SceneInfos(object):
    def __init__(self, dcc_name=None, dcc_version=None, scene_path=None):
        self.dcc_name = dcc_name
        self.dcc_version = dcc_version
        self.scene_path = scene_path
