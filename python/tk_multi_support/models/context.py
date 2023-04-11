# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from collections import namedtuple


class Project(namedtuple("Project", ["id", "name", "url"], defaults=[0, None, None])):
    def __repr__(self):
        return "Project: {} ({})".format(self.name, self.id)


class Entity(
    namedtuple("Entity", ["id", "name", "type", "url"], defaults=[0, None, None, None])
):
    def __repr__(self):
        return "{}: {} ({})".format(self.type, self.name, self.id)


class User(
    namedtuple(
        "User",
        ["id", "name", "login", "email", "url"],
        defaults=[0, None, None, None, None],
    )
):
    def __repr__(self):
        return "User: {} ({})".format(self.login, self.id)


class Task(namedtuple("Task", ["id", "name", "url"], defaults=[0, None, None])):
    def __repr__(self):
        return "Task: {} ({})".format(self.name, self.id)


class Step(namedtuple("Step", ["id", "name", "url"], defaults=[0, None, None])):
    def __repr__(self):
        return "Step: {} ({})".format(self.name, self.id)


class Context(
    namedtuple(
        "Context",
        ["project", "entity", "user", "task", "step"],
        defaults=[Project(), Entity(), User(), Task(), Step()],
    )
):
    pass
