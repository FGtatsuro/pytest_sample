#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from ._logging import get_logger

logger = get_logger(__name__)

class ResponseHandler(object):

    def __call__(self, resp, *args, **kwargs):
        logger.debug('### Request ###')
        logger.debug('Method:{0}'.format(resp.request.method))
        logger.debug('URL:{0}'.format(resp.request.url))
        logger.debug('Header:{0}'.format(resp.request.headers))
        logger.debug('Body:{0}'.format(resp.request.body))
        logger.debug('### Response ###')
        logger.debug('Status:{0}'.format(resp.status_code))
        logger.debug('Header:{0}'.format(resp.headers))
        logger.debug('Body:{0}'.format(resp.text))

class HttpBinClient(object):
    '''
    The client for https://httpbin.org/
    '''

    base = 'https://httpbin.org'

    def __init__(self):
        self.session = requests.Session()
        self.session.hooks = {'response': ResponseHandler()}
    
    def ip(self):
        return self.session.get('{0}/ip'.format(self.base))
