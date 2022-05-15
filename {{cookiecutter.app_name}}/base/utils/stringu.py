# -*- coding: utf-8 -*-
import json
import re
from typing import Union


def changeStr2Dict(s: str) -> dict:
    s = s.strip("&")
    params = s.split("&")
    d = {}
    for p in params:
        k, v = p.split("=")
        d[k] = v
    return d


def to_dataclass(d: Union[dict, str]):
    def extract_type(s: str):
        return re.search("<class \'(\w+)\'>", s).group(1)

    if isinstance(d, str):
        d = json.loads(d)
    for k, v in d.items():
        print(f"{k}: {extract_type(str(type(v)))}")


if __name__ == '__main__':
    a = """
    {
        "gid": 30
    }
    """
    to_dataclass(a)
