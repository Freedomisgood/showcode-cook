# -*- coding: utf-8 -*-
"""
list used decorators
"""
from functools import wraps

import requests

from base.exceptions import RequestException
from base.ext import LOG
from base.settings import MAX_RETRY_COUNT


def get_proxy():
    PROXY_POOL_URL = "http://localhost:5010"
    proxy = (
        requests.get(f"{PROXY_POOL_URL}/get?type=https", timeout=3).json().get("proxy")
    )
    res_proxy = {"http": "http://{}".format(proxy), "https": "https://{}".format(proxy)}
    print("获得proxy: {}".format(res_proxy))
    return res_proxy


def delete_proxy(proxy):
    PROXY_POOL_URL = "http://localhost:5010"
    requests.get(f"{PROXY_POOL_URL}/delete/?proxy={proxy}")


def requestWithProxy(func):
    """
    给请求增加上代理
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        rand_proxy = get_proxy()
        # 给请求加上proxy参数
        kwargs["proxy"] = rand_proxy
        tryTimes = 0
        resp = None
        while tryTimes < MAX_RETRY_COUNT:
            try:
                resp = func(*args, **kwargs)
                if 100 < resp.status_code < 400:
                    break
            except RequestException as e:
                tryTimes += 1
                LOG.warning("{}请求失败: e~{}".format(rand_proxy, e))
                rand_proxy = get_proxy()
                delete_proxy(rand_proxy)
        return resp

    return wrapper


def login_required(func):
    """
    类方法需要类属性self.verified==True
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.verified:
            # do something
            pass
        return func(self, *args, **kwargs)

    return wrapper
