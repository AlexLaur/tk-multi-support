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


HookClass = sgtk.get_hook_baseclass()


class ReportSender(HookClass):

    CONTENT = ""

    def send(self, report):
        """Send the report. It will create a new row in Ticket entity.

        :param report: The report to send
        :type report: tk_multi_support.models.Report
        :return: True if the report has been sent, False otherwise
        :rtype: bool
        """

        data = {
            "title": report.subject,
            "description": report.content,
            "project": {"id": report.context.project.id, "type": "Project"}
        }

        # TODO add attachements for thumbnails

        print(data)

        # self.parent.shotgun.create("Ticket", data)

        return True