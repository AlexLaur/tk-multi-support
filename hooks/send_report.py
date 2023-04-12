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

    """Send the report. A new ticket will be created on ShotGrid."""

    CONTENT = (
        "Content\n"
        "---\n"
        "\n"
        "{content}\n"
        "Context\n"
        "---\n"
        "- [{project}]({project_url})\n"
        "- [{user}]({user_url})\n"
        "- [{task}]({task_url})\n"
        "- [{step}]({step_url})\n"
        "- [Entity: {entity}]({entity_url})\n"
        "\n"
        "DCC\n"
        "---\n"
        "- {dcc_name} ({dcc_version})\n"
        "- Scene: {scene_path}"
    )

    def send(self, report):
        """Send the report. It will create a new row in Ticket entity.

        :param report: The report to send
        :type report: tk_multi_support.models.Report
        :return: True if the report has been sent, False otherwise
        :rtype: bool
        """

        self.logger.info("Sending the report on ShotGrid...")

        description = self.CONTENT.format(
            content=report.content,
            project=report.context.project,
            user=report.context.user,
            task=report.context.task,
            step=report.context.step,
            entity=report.context.entity,
            project_url=report.context.project.url,
            user_url=report.context.user.url,
            task_url=report.context.task.url,
            step_url=report.context.step.url,
            entity_url=report.context.entity.url,
            dcc_name=report.scene_infos.dcc_name,
            dcc_version=report.scene_infos.dcc_version,
            scene_path=report.scene_infos.current_scene,
        )

        data = {
            "title": report.subject,
            "description": description,
            "project": {"id": report.context.project.uid, "type": "Project"},
            "created_by": {"id": report.context.user.uid, "type": "HumanUser"},
        }

        sg_ticket = self.parent.shotgun.create("Ticket", data)
        self.logger.info("A ticket has been created.")

        for thumbnail in report.thumbnails:
            self.logger.info("Upload a thumbnail as attachment on the ticket.")
            self.parent.shotgun.upload(
                entity_type="Ticket",
                entity_id=sg_ticket.get("id"),
                path=thumbnail,
                field_name="attachments",
            )

        self.logger.info("The report has been sent on ShotGrid.")

        return True
