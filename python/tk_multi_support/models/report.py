# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.


class Report(object):
    def __init__(
        self, scene_infos, context, subject="", content="", thumbnails=None
    ):

        self.scene_infos = scene_infos
        self.context = context
        self.subject = subject
        self.content = content
        self.thumbnails = thumbnails or []

    def keys(self):
        return self.__dict__.keys()
