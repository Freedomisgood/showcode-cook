# -*- coding: utf-8 -*-
# @Time    : 2022/7/16 11:00
# @Author  : Mrli
# @File    : login.py
from base.settings import USER_DIR_PATH, USER_DATA_FILENAME
import requests
import pickle


class LoginHelper:
    def __init__(self, username, password, login_url):
        self.username = username
        self.password = password
        self.ua = ua

        self.sess = requests.Session()
        # 确保登陆
        self.valid_login()

        self.login_url = login_url

    def login(self):
        """进行登陆"""
        data = {
            'userName': self.username,
            'password': self.password,
        }
        headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 uni-app Html5Plus/1.0 (Immersed/25.333334)',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        # TODO
        resp = self.sess.post(self.login_url, data=data, headers=headers)

        if resp.get("code") == 0:
            # TODO: 1， 登录后对请求头进行更新
            # self.sess.headers.update({"token": resp.get("result").get("token")})
            # 2. 进行存储
            with open(os.path.join(USER_DIR_PATH, USER_DATA_FILENAME.format(username=self.username)), "wb") as f:
                pickle.dump(self.sess.headers, f)
                LOG.info("登陆成功, 写入持久化的登陆信息")
        else:
            LOG.error("登陆失败, 请核实: {}".format(resp.get("msg")))

    def valid_login(self):
        """校验是否登陆有效"""
        data_file = os.path.join(USER_DIR_PATH, USER_DATA_FILENAME.format(username=self.username))
        if os.path.exists(data_file):
            with open(data_file, "rb") as f:
                h = pickle.load(f)
                self.sess.headers.update(h)
            if self.get_user_balance(moneyType=6) is None:
                LOG.info("持久化登陆信息失效...尝试重新登陆")
                self.login(self.username, self.password)
            else:
                LOG.info("读取持久化登陆信息...登陆成功")
        else:
            LOG.info("没有持久化登陆信息...进行登陆")
            self.login(self.username, self.password)
