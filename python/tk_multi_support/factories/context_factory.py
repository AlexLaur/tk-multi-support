# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk

from ..models import Context, Project, User, Task, Step, Entity


class ContextFactory(object):
    @staticmethod
    def build(tk_ctx):
        """Build the context object

        :param tk_ctx: The context from sgtk
        :type tk_ctx: sgtk.Context
        :return: The full object context
        :rtype: tk_multi_support.models.Context
        """
        app = sgtk.platform.current_bundle()

        project = Project(tk_ctx.project.get("id"), tk_ctx.project.get("name"))

        if tk_ctx.user:
            if not tk_ctx.user.get("login", None) or not tk_ctx.user.get(
                "email", None
            ):
                user_data = app.shotgun.find_one(
                    "HumanUser",
                    filters=[["id", "is", tk_ctx.user.get("id")]],
                    fields=["id", "name", "login", "email"],
                )

                user = User(
                    user_data.get("id"),
                    user_data.get("name"),
                    user_data.get("login"),
                    user_data.get("email"),
                )
            else:
                user = User(
                    tk_ctx.user.get("id"),
                    tk_ctx.user.get("name"),
                    tk_ctx.user.get("login"),
                    tk_ctx.user.get("email"),
                )
        else:
            user = User()

        if tk_ctx.task:
            task = Task(tk_ctx.task.get("id"), tk_ctx.task.get("name"))
        else:
            task = Task()

        if tk_ctx.step:
            step = Step(tk_ctx.step.get("id"), tk_ctx.step.get("name"))
        else:
            step = Step()

        if tk_ctx.step:
            entity = Entity(
                tk_ctx.entity.get("id"),
                tk_ctx.entity.get("name"),
                tk_ctx.entity.get("type"),
            )
        else:
            entity = Entity()

        context = Context(
            project=project, entity=entity, user=user, task=task, step=step
        )

        return context
