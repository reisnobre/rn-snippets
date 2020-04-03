#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helper utilities to format javascript jsdocs documentation.
"""


def param(argument):
    return " * @param {{}} {0}".format(argument)
