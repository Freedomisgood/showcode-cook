# -*- coding: utf-8 -*-
# @File    : main.py

from base.helper.runner import Runner


def _init_parser():
    """获得CLI参数"""
    from argparse import ArgumentParser

    parser = ArgumentParser("jd_super_seckill")
    return parser.parse_args()


if __name__ == "__main__":
    args = _init_parser()
    r = Runner()
    r.run()
