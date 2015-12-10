#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from sample.client import HttpBinClient

def test_ip():

    c = HttpBinClient()
    r = c.ip()
    body = json.loads(r.text)
    assert 'origin' in body
