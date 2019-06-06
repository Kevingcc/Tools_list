#!/usr/bin/env python3
#coding:utf-8


import colorlog
import logging


test = "hello word"

'''
set log this code is Useless
log.debug  is white ,info is green ,warn is yellow ,error is red ,critical  red!
'''
handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s [%(name)s] [%(levelname)s] %(message)s%(reset)s',
    datefmt=None,
    reset=True,
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    secondary_log_colors={},
    style='%')
handler.setFormatter(formatter)
log = colorlog.getLogger('subdns')
log.addHandler(handler)
log.setLevel(logging.INFO)

