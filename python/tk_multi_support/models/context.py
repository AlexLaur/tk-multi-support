# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from dataclasses import dataclass, field

from collections import namedtuple


@dataclass
class BaseDataObject(object):
    uid: int = field(default=0)
    name: str = field(default=None)
    url: str = field(default=None)

    def __repr__(self):
        return "{class_name}: {name} ({uid})".format(
            class_name=self.__class__.__name__, name=self.name, uid=self.uid
        )


@dataclass
class Project(BaseDataObject):
    pass


@dataclass
class Entity(BaseDataObject):
    type: str = field(default=None)

    def __repr__(self):
        return "{entity_type}: {name} ({uid})".format(
            entity_type=self.type, name=self.name, uid=self.uid
        )


@dataclass
class User(BaseDataObject):
    login: str = field(default=None)
    email: str = field(default=None)


@dataclass
class Task(BaseDataObject):
    pass


@dataclass
class Step(BaseDataObject):
    pass


@dataclass
class Context(object):
    project: Project = field(default=Project())
    entity: Entity = field(default=Entity())
    user: User = field(default=User())
    task: Task = field(default=Task())
    step: Step = field(default=Step())
