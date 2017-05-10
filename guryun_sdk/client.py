# -*- coding: utf-8 -*-
'''
股人云API调用SDK
网站： www.guryun.com
项目地址：https://github.com/guryun/guryunSDK
'''

import requests
from .logger import logger
from .urlmap import URLMAP

class Client(object):
    """docstring for Client"""
    timeout = 3

    def __init__(self, config):
        super(Client, self).__init__()
        self.config = config

    def filterstock(self, json_data):
        path = URLMAP['filterstock']
        url = self._makeurl(path)
        try:
            resp = requests.post(url, auth=(self.config.username, self.config.passwd),json
                =json_data, headers={'content-type':'application/json', 'accept':'application/json'},timeout=self.timeout)
        except Exception as e:
            logger.error(e)

        if resp.status_code == 200:
            return resp.json()
        else:
            logger.error(resp.text)
            raise ValueError('error request')

    def _makeurl(self, path):
        url = '{}://{}:{}/api/{}{}'.format(self.config.protocol,self.config.host,self.config.port, self.config.version,path)
        logger.debug('send request: {}'.format(url))
        return url
