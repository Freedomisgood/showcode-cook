# -*- coding: utf-8 -*-

def changeStr2Dict(s: str) -> dict:
    s = s.strip("&")
    params = s.split("&")
    d = {}
    for p in params:
        k, v = p.split("=")
        d[k] = v
    return d
