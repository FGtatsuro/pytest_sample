#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pytest_runtest_setup(item):
    # TODO: More sophisticated way
    # This is for look of stdout. 
    # Without this:
    # <test name> DEBUG:<log>
    #
    # With this:
    # <test name>
    # DEBUG:<log>
    print('')
