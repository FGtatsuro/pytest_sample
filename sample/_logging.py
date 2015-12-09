#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from logging import getLogger, Formatter, StreamHandler, DEBUG

def get_logger(name):
    formatter = Formatter('%(levelname)s:%(name)s:%(asctime)s:%(message)s')
    handler = StreamHandler(sys.stdout)
    handler.setLevel(DEBUG)
    handler.setFormatter(formatter)
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)
    return logger
