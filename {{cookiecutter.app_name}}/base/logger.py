# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 22:48
# @File    : logger.py
import time
from pathlib import Path

from loguru import logger

from base.settings import BASEDIR

log_folder_path = Path(BASEDIR, 'logs')
log_path = Path(log_folder_path, time.strftime("%F"))  # 日志根目录 ../logs/yyyy-mm-dd/
# 创建日志文件夹
log_path.mkdir(parents=True, exist_ok=True)
# 设置logger
logger.add(sink=Path(log_path, "log.txt"), format="{time} {level} {message}", level="INFO")

LOG = logger
