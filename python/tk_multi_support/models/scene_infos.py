# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from dataclasses import dataclass, field


@dataclass
class SceneInfos(object):
    """This object contains all informations of the scene."""

    dcc_name: str = field(default=None)
    dcc_version: str = field(default=None)
    scene_path: str = field(default=None)
