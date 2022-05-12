# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta


def format_datetime(target_time: str) -> str:
    _date = datetime.strptime(target_time, "%Y-%m-%dT%H:%M:%S+08:00")
    local_time = _date + timedelta(hours=8)
    end_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
    return end_time


def _compile_time(hm: str):
    return "{} {}:00".format(date.today(), hm)


def _mktime_from_strtime(tm: str):
    return datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").timestamp()


def hm2timestmapMs(hm: str):
    """将HH:MM转换成当日时间戳, Ms级别"""
    return _mktime_from_strtime(_compile_time(hm)) * 1000


def hm2timestmapS(hm: str):
    """将HH:MM转换成当日时间戳, s级别"""
    return _mktime_from_strtime(_compile_time(hm))
