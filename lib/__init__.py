#!/usr/bin/env python3
#coding:utf-8

__all__ = ['test','get_headers',
           'info','error',
           'warning','print_',
           'AttribDict','load',
           'loads','dump',
           'dumps']

import random
from json import load
from json import loads
from json import dump
from json import dumps
from .debug import test
from .debug import log
from .headers import get_headers
from .datatype import AttribDict

info = log.info
error = log.error
warning = log.warning

W = '\033[0m'

G = '\033[1;32m'
O = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'

def print_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    print(color+content+W)

