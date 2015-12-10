#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import pytest

# Without the decorator, default timeout setting is used. Thus, this test will be failed.
@pytest.mark.slow
@pytest.mark.timeout(10)
def test_timeout():
    time.sleep(8)
