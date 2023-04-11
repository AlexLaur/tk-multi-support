# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk

from .models import SceneInfos, Report
from .factories import ContextFactory


class DataCollector(object):
    def collect(self):
        app = sgtk.platform.current_bundle()

        # Collect informations about the scene and the DCC
        scene_infos = app.execute_hook_method(
            "hook_scene_infos", "collect", scene_infos=SceneInfos()
        )

        # Collect informations about the context
        context = ContextFactory.build(app.context)

        # Generate the report
        report = Report(scene_infos, context)

        # Collect custom informations
        report = app.execute_hook_method(
            "hook_custom_infos", "collect", report=report
        )

        return report
