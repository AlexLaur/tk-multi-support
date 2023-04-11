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


class Project(namedtuple("Project", ["id", "name"], defaults=[0, None])):
    pass


class Entity(
    namedtuple("Entity", ["id", "name", "type"], defaults=[0, None, None])
):
    pass


class User(
    namedtuple(
        "User",
        ["id", "name", "login", "email"],
        defaults=[0, None, None, None],
    )
):
    pass


class Task(namedtuple("Task", ["id", "name"], defaults=[0, None])):
    pass


class Step(namedtuple("Step", ["id", "name"], defaults=[0, None])):
    pass


class Context(
    namedtuple(
        "Context",
        ["project", "entity", "user", "task", "step"],
        defaults=[Project(), Entity(), User(), Task(), Step()],
    )
):
    pass
