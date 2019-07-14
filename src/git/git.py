#!/usr/bin/env python3
#coding:utf-8


import argparse
import configparser
import os
from lib import Libs
from lib import root
from lib import input_
from lib import print_
from lib import red
from lib import blue
from lib import green



libs = Libs()
commands_ = libs.commands_
commands__ = libs.commands__




def argparse_():
    parser = argparse.ArgumentParser(description='git tools.')
    parser.add_argument('--version','-v',action='store_true',help='查看版本.')
    # parser.add_argument('--path','-p',help='路径.')
    parser.add_argument('--a1','-a',action='store_true',help='用户信息配置.')
    parser.add_argument('--b1','-b',action='store_true',help='文件 add 添加功能.')
    parser.add_argument('--c1','-c',action='store_true',help='提交.')
    parser.add_argument('--d1','-d',action='store_true',help='推送功能.')
    parser.add_argument('--e1','-e',action='store_true',help='同步功能.')
    parser.add_argument('--f1','-f',action='store_true',help='删除版本库里的文件.')
    parser.add_argument('--g1','-g',action='store_true',help='查看状态.')
    parser.add_argument('--h1','-cl',action='store_true',help='克隆(clong).')
    parser.add_argument('--i1','-i',action='store_true',help='添加远程代码托管平台.')
    parser.add_argument('--y1','-y',help='文件名.')
    parser.add_argument('--z1','-z',help='路径.')
    parser.add_argument

    args = parser.parse_args()
    return args


args = argparse_()
a1 = args.a1
b1 = args.b1
c1 = args.c1
d1 = args.d1
e1 = args.e1
f1 = args.f1
g1 = args.g1
h1 = args.h1
i1 = args.i1
y1 = args.y1
z1 = args.z1


# test.ini
# conf = configparser.ConfigParser()
# path = f'{root}src/git/test.ini'
# conf.read(path,encoding='utf-8')

# sections = conf.sections()
# print(sections)
# test1 = sections[0]
# items = conf.items(test1)
# print(items[0][0])
# print(items[0][1])



try:
    if z1:
        with open(f'{root}src/git/setting.ini','w+') as w:
            d1 = '[setting]\n'
            d2 = '\n'
            d3 = f'path = "{z1}"\n'
            w.write(d1)
            w.write(d2)
            w.write(d3)
except:
    pass





try:
    """
    setting.ini
    """
    try:
        conf = configparser.ConfigParser()
        path = f'{root}src/git/setting.ini'
        conf.read(path,encoding='utf-8')

        sections = conf.sections()
        setting = sections[0]
        items = conf.items(setting)
        z1 = items[0][1]
    except:
        pass
except:
    pass










# 用户信息.
def yhxx(name,email):
    cmd1 = f'git config --global user.name "{name}"'
    cmd2 = f'git config --global user.email {email}'
    commands__(cmd1)
    commands__(cmd2)


# 添加功能.
def add(path,filename='.'):
    if filename == '.':
        cmd1 = f'cd {path} && git add -A -- .'
    else:
        cmd1 = f'cd {path} && git add {filename}'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')


# 提交.
def tj(path,content):
    cmd1 = f'cd {path} && git commit -m "{content}"'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')


# 推送功能.
def ts(path):
    cmd1 = f'cd {path} && git push -u origin master'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')

# 同步功能.
def tb(path):
    cmd1 = f'cd {path} && git pull --tags origin master'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')


# 删除版本库里的文件.
def delete_1(path,name):
    cmd1 = f'cd {path} && git rm {name}'
    cmd2 = f'cd {path} && git commit -m "remove {name}"'
    c1 = commands__(cmd1)
    c2 = commands__(cmd2)
    if not c1 or not c2:
        red('[-]没有路径.')
        red('[-]没有文件名.')


# 查看状态.
def status(path):
    cmd1 = f'cd {path} && git status'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')

# 克隆.
def clong(path,url):
    cmd1 = f'cd {path} && git clone {url}'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')

# 添加远程代码托管平台.
def add_dm(path,url):
    cmd1 = f'cd {path} && git remote add origin {url}'
    c1 = commands__(cmd1)
    if not c1:
        red('[-]没有路径.')


def _git():
    path = z1
    filename = y1
    if a1:
        ipt1 = input_('username>')
        ipt2 = input_('email>')
        yhxx(ipt1,ipt2)
    elif b1:
        add(path,filename)
    elif c1:
        ipt1 = input_('提交内容>')
        if not ipt1:
            ipt1 = 'up'
        tj(path,ipt1)
    elif d1:
        ts(path)
    elif e1:
        tb(path)
    elif f1:
        delete_1(path,filename)
    elif g1:
        status(path)
    elif h1:
        ipt1 = input_('Url>')
        clong(path,ipt1)
    elif i1:
        ipt1 = input_('Url>')
        add_dm(path,ipt1)


