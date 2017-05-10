from guryun_sdk.client import Client
from config import Config
# -*- coding: utf-8 -*-

from utils import format_stocks, save_csv
def main():
    #初始化Config， 可以传入用户名密码
    # cfg = Config('your username', 'your passwd')
    cfg = Config() #如果为空默认使用config.py的配置
    guryun_client = Client(cfg)
    json_data = {"id":"15", #选股器id
                "date":"2017-03-08", #选股日期， 如为空自动选系统有数据的最新一天
                "mode":2 #返回模式， 1为简单， 2为详细, 如为空默认1
                }
    try:
        result = guryun_client.filterstock(json_data)
        print(result.get('title')) #title为选股器名
        print('total count: %s' % result.get('count')) #count为选股股票总数
        print('date: {}'.format(result.get('date')))
        format_stocks(result.get('data')) #详细模式返回结果可以进行格式化， 显示更美观
        # print(result.get('data'))#简单模式直接打印
        save_csv(result.get('data')) #详细模式返回结果可以保持为csv文件
    except:
        pass

if __name__ == '__main__':
    main()
