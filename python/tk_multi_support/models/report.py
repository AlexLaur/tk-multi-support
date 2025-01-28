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
    """The report contains all informations about the scene, the context,
    the subject, the content and thubmnails.
    It is used to send the ticket on ShotGrid.

    It is not a true DTO because we can add other attributes on this object and
    default attributes are not protected with properties.
    """

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
