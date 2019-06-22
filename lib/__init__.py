#!/usr/bin/env python3
#coding:utf-8

__all__ = ['test','get_headers',
           'info','error',
           'warning','print_',
           'AttribDict','load',
           'loads','dump',
           'dumps','root',
           'red','blue',
           'green','input_',
           'regular']

import random
import subprocess
import re
import os
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

root_ = subprocess.check_output('echo $HOME',shell=True).decode().strip()
root = '{}/.Tools/Tools_list/'.format(root_)


def print_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    print(color+content+W)

def red(content):
    d = R + content + W
    print(d)

def blue(content):
    d = B + content + W
    print(d)

def green(content):
    d = G + content + W
    print(d)

def input_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    d = input(color+content+W)
    return d



def filter_domain(domain=[]):
    d1 = []
    for data1 in domain:
            if not re.findall('\.xls',data1) and \
                not re.findall('\.sql',data1) and \
                not re.findall('\.txt',data1) and \
                not re.findall('www.google.com',data1) and \
                not re.findall('www.baidu.com',data1) and \
                not re.findall('baidu.com',data1) and \
                not re.findall('google.com',data1) and \
                not re.findall('github.com',data1) and \
                not re.findall('cnblogs.com',data1) and \
                not re.findall('csdn.net',data1) and \
                not re.findall('exploit-db.com',data1):
                d1.append(data1)

    return d1



def read_text(filename):
    lines = []
    with open('{}lib/{}'.format(root,filename),'r') as r:
        for line in r.readlines():
            lines.append(line.strip())
    return lines



def read_text_(filename):
    lines = []
    with open('{}'.format(filename),'r') as r:
        for line in r.readlines():
            lines.append(line.strip())
    return lines





def get_target_sqli_url():
        from main import Libs
        d1 = []
        d2 = []
        datas1 = read_text(filename='sqli1.txt')
        datas2 = read_text(filename='sqli2.txt')
        d1 = filter_domain(domain=datas1)
        d2 = filter_domain(domain=datas2)        

        return (d1,d2)



def get_url(domain):
    d1 = domain.split('/')
    for d2 in d1:
        if \
        d2 != 'https' and \
        d2 != 'http' and \
        d2 != '/' and \
        d2 and \
        d2 != 'https:' and \
        d2 != 'https:/' and \
        d2 != 'http:' and \
        d2 != 'http:/':
            return d2.strip()


def get_filename(path):
    """
    获取指定目录下的所有文件绝对路径.
    """
    pathname = []
    catalog = path
    for (dirpath, dirnames, filenames) in os.walk(catalog):     
        for filename in filenames:  
            pathname += [os.path.join(dirpath, filename)]
    
    return pathname

def get_filename_(path):
    """
    获取文件名称.
    """
    pathname = []
    catalog = path
    for (dirpath,dirnames,filenames) in os.walk(catalog):
        for filename in filenames:
            pathname.append(filename)
    return pathname


def regular(num):
    """
    正则匹配规则.
    1.匹配数字
    2.匹配字符
    3.匹配字符及数字

    例子:regular(1)
    返回结果:
        >>> \\d+
    """
    if num == 1:
        return '\d+'
    if num == 2:
        return '[a-zA-Z]+'
    if num == 3:
        return '[a-zA-Z0-9]'
    

