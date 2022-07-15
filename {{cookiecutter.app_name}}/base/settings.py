# -*- coding: utf-8 -*-
# @File    : settings.py
from pathlib import Path

# 根目录
BASEDIR = Path(__file__).resolve().parent
COOKIES_CACHE_FOLDER = BASEDIR.with_name("users")
COOKIES_CACHE_FOLDER.mkdir(exist_ok=True)
COOKIES_CACHE_FILE = COOKIES_CACHE_FOLDER.joinpath("cookies.json")



COOKIES = {}

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
}


# VPN配置
http_proxy = "socks5h://127.0.0.1:10808"
https_proxy = "socks5h://127.0.0.1:10808"
proxies = {
    # "https": https_proxy,
    # "http": http_proxy
}

# 网络请求最大重试次数
NET_MAX_RETRY_COUNT = 5

ASSETS_FOLDER = Path(__file__).resolve().with_name("assets")
