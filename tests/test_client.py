#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import pytest

from sample.client import HttpBinClient

@pytest.mark.slow
@pytest.mark.httpaccess
def test_ip():

    c = HttpBinClient()
    r = c.ip()
    body = json.loads(r.text)
    assert 'origin' in body
