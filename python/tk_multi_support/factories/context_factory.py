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
    @classmethod
    def build(cls, tk_ctx):
        """Build the context object

        :param tk_ctx: The context from sgtk
        :type tk_ctx: sgtk.Context
        :return: The full object context
        :rtype: tk_multi_support.models.Context
        """
        app = sgtk.platform.current_bundle()
        base_url = app.shotgun.base_url

        project = cls._get_project_dto(tk_ctx.project, base_url)
        user = cls._get_user_dto(tk_ctx.user, base_url)
        task = cls._get_task_dto(tk_ctx.task, base_url)
        step = cls._get_step_dto(tk_ctx.step, base_url)
        entity = cls._get_entity_dto(tk_ctx.entity, base_url)

        context = Context(
            project=project, entity=entity, user=user, task=task, step=step
        )

        return context

    @staticmethod
    def urljoin(*parts):
        return "/".join(str(part).strip("/") for part in parts)

    @classmethod
    def _get_user_dto(cls, ctx_user, base_url):
        if not ctx_user:
            return User()

        uid = ctx_user.get("id")
        name = ctx_user.get("name")
        login = ctx_user.get("login", None)
        email = ctx_user.get("email", None)
        url = cls.urljoin(base_url, "detail", "HumanUser", uid)

        if not login or not email:
            app = sgtk.platform.current_bundle()
            user_data = app.shotgun.find_one(
                "HumanUser",
                filters=[["id", "is", uid]],
                fields=["login", "email"],
            )

            login = user_data.get("login")
            email = user_data.get("email")

        return User(uid, name, url, login, email)

    @classmethod
    def _get_project_dto(cls, ctx_project, base_url):
        uid = ctx_project.get("id")
        name = ctx_project.get("name")
        url = cls.urljoin(base_url, "detail", "Project", uid)
        return Project(uid, name, url)

    @classmethod
    def _get_task_dto(cls, ctx_task, base_url):
        if not ctx_task:
            return Task()

        uid = ctx_task.get("id")
        name = ctx_task.get("name")
        url = cls.urljoin(base_url, "detail", "Task", uid)

        return Task(uid, name, url)

    @classmethod
    def _get_step_dto(cls, ctx_step, base_url):
        if not ctx_step:
            return Step()

        uid = ctx_step.get("id")
        name = ctx_step.get("name")
        url = cls.urljoin(base_url, "detail", "Step", uid)

        return Step(uid, name, url)

    @classmethod
    def _get_entity_dto(cls, ctx_entity, base_url):
        if not ctx_entity:
            return Entity()

        uid = ctx_entity.get("id")
        name = ctx_entity.get("name")
        entity_type = ctx_entity.get("type")
        url = cls.urljoin(base_url, "detail", entity_type, uid)

        return Entity(uid, name, url, entity_type)
