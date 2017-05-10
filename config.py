# -*- coding: utf-8 -*-
GURYUN_HOST = 'www.guryun.com'
GURYUN_USERNAME = 'testuser' #改为你的用户名
GURYUN_PASSWD = 'testpass1' #改为你的密码
GURYUN_PROTOCOL = 'http'
GURYUN_PORT = 80
GURYUN_API_VERSION = 'v1.0' #API版本号， 未来可能变化
GURYUN_DATA_PATH = 'data' #生成csv存放目录

class Config(object):

    """docstring for Config"""
    def __init__(self, username=None, passwd=None):
        super(Config, self).__init__()
        self.host = GURYUN_HOST
        self.username = username if username else GURYUN_USERNAME
        self.passwd = passwd if passwd else GURYUN_PASSWD
        self.protocol = GURYUN_PROTOCOL
        self.port = GURYUN_PORT
        self.version = GURYUN_API_VERSION
