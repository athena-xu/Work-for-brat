#!/usr/bin/env python
# -*- Mode: Python; tab-width: 4; indent-tabs-mode: nil; coding: utf-8; -*-
# vim:set ft=python ts=4 sw=4 sts=4 autoindent:

'''
Deletion functionality.
'''

from __future__ import with_statement

from os.path import join as path_join
from message import Messager

def delete_test(filetype, filename, filedata):
    Messager.error("Type:" + filetype + "233Document deletion not supported in this version.233" + "Name:" + filename + "Data:" + filedata)
    return {}

