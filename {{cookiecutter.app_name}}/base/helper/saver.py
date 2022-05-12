# -*- coding: utf-8 -*-
# @File    : saver.py

from base.ext import Session, LOG


class MysqlSaver:
    def __init__(self, phrase):
        self.sql_sess = Session()

    def insert(self, insert_obj):
        raise NotImplementedError
        is_exist = self.sql_sess.query(insert_obj).filter_by(entry_id=insert_obj.entry_id).count() > 0
        if not is_exist:
            self.sql_sess.add(insert_obj)
            self.sql_sess.commit()
            LOG.info("{}插入成功~".format(insert_obj))
        else:
            LOG.info("{}已持久化!".format(insert_obj))
        return
