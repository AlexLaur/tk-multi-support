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


class BaseDataObject(object):
    def __init__(self, uid=0, name="", url=""):
        self._uid = uid
        self._name = name
        self._url = url

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    def __repr__(self):
        return "{class_name}: {name} ({uid})".format(
            class_name=self.__class__.__name__, name=self.name, uid=self.uid
        )


class Project(BaseDataObject):
    pass


class Entity(BaseDataObject):
    def __init__(self, uid=0, name="", url="", type=None):
        super(Entity, self).__init__(uid, name, url)

        self._type = type

    @property
    def type(self):
        return self._type

    def __repr__(self):
        return "{entity_type}: {name} ({uid})".format(
            entity_type=self.type, name=self.name, uid=self.uid
        )


class User(BaseDataObject):
    def __init__(self, uid=0, name="", url="", login="", email=""):
        super(User, self).__init__(uid, name, url)

        self._login = login
        self._email = email

    @property
    def login(self):
        return self._login

    @property
    def email(self):
        return self._email


class Task(BaseDataObject):
    pass


class Step(BaseDataObject):
    pass


class Context(
    namedtuple(
        "Context",
        ["project", "entity", "user", "task", "step"],
        defaults=[Project(), Entity(), User(), Task(), Step()],
    )
):
    pass
