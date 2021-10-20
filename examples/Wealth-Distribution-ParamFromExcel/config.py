# -*- coding:utf-8 -*-
# @Time: 2021/10/16 17:09
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: simulator_config.py.py
import os

from Melodie import NewConfig

config = NewConfig(
    project_name='WealthDistribution',
    project_root=os.path.dirname(__file__),
    sqlite_folder='data/sqlite',
    excel_source_folder='data/excel_source',
    output_folder='data/output',
    csv_source_folder='data/csv',
)

