# -*- coding: utf-8 -*-
"""
define some help functions
"""
import io
import csv
import datetime
import config
import os

def format_stocks(stocks_result):
    input_stream = io.StringIO(stocks_result)
    csv_f = csv.reader(input_stream)
    header_str = '{:<6} {:\u3000<5} {:\u3000<5} {:<7} {:<10} {:<10}'
    format_str = '{:<10} {:\u3000<5} {:\u3000<5} {:<10} {:<14} {:<10}'
    i = 0
    for row in csv_f:
        if i == 0:
            print(header_str.format(*row))
        else:
            print(format_str.format(*row))
        i += 1

def save_csv(stocks_result, date=None):
    if not date:
        date = datetime.date.today().strftime('%Y-%m-%d')
    filename = 'stock_{}.csv'.format(date)
    _check_folder(config.GURYUN_DATA_PATH)
    filepath = os.path.join(config.GURYUN_DATA_PATH, filename)
    input_stream = io.StringIO(stocks_result)
    csv_f = csv.reader(input_stream)
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(csv_f)

def _check_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)