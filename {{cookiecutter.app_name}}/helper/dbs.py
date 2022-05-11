# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# mysql+pymysql 链接方式:
# mysql+pymysql://root:ycc962464@127.0.0.1:3306链接地址及端口/tests链接的数据库名称?charset=utf8mb4 字符集
# 其中root为mysql账号, ycc962464为密码
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/{{ cookiecutter.db_name }}?charset=utf8mb4",
                       max_overflow=5, pool_size=5)
Base = declarative_base()

{%- if cookiecutter.table_name != "None" %}
# 创建单表
class {{cookiecutter.table_name|replace('_', ' ')|title|replace(' ', '') }}(Base):
    __tablename__ = '{{ cookiecutter.table_name }}'
    pass
{%- endif %}