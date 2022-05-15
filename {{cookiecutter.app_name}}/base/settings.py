# -*- coding: utf-8 -*-
# @File    : settings.py
from pathlib import Path

# 根目录
BASEDIR = Path(__file__).resolve().parent.parent
COOKIES_CACHE_FILE = BASEDIR.with_name("users/").joinpath("cookies.json")


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
