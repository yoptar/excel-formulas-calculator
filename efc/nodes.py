# coding: utf8

from __future__ import unicode_literals
from tatsu.objectmodel import Node


class EFCBaseNode(Node):
    pass


class AddSubNode(EFCBaseNode):
    mult = None


class Add(AddSubNode):
    mult = 1


class Subtract(AddSubNode):
    mult = -1
