#!/usr/bin/env python3
#coding:utf-8



"""
这是一个python脚本版本识别工具，通过枚举的特征判断此脚本是基于python2 或 python3.
"""



import requests
import time
import re
import argparse
import asyncio
import threading
from threading import Thread
from os import system




def argparse_():
    parser = argparse.ArgumentParser(description='python 脚本版本识别工具.')
    parser.add_argument('--version','-v',action='store_true',help='查看版本.')
    parser.add_argument('--path','-p',help='路径.')
    args = parser.parse_args()
    return args


_args = argparse_()
path = _args.path


"""
特征
"""
def py3():
    t1 = '!/usr/bin/env python3'
    t2 = '!/usr/bin/python3'
    t3 = 'python3'
    # t4 = 'range'
    t5 = 'print('
    return (t1,t2,t3,t5)

def py2():
    t1 = '!/usr/bin/env python2'
    t2 = '!/usr/bin/python2'
    t3 = 'python2'
    # t4 = 'xrange'
    t5 = 'print '
    return (t1,t2,t3,t5)

lock = threading.Lock()


"""
扫描
"""
def scan1():
    with open(path,'r') as r:
        for line in r.readlines():
            # py3
            for d1 in py3():
                # lock.acquire()
                if d1 in line:
                    print('Is py3!')
                    print('Py3 keyword -> {}'.format(d1))
                    return True

    print('py3 no!')
    return False
                

def scan2():
    with open(path,'r') as r:
        for line in r.readlines():
            # py2
            for d1 in py2():
                # lock.acquire()
                if d1 in line:
                    print('Is py2!')
                    print('Py2 keyword => {}'.format(d1))
                    return True

    print('py2 no!')
    return False


"""
主函数
"""
def main():
    thread1 = Thread(target=scan1)
    thread2 = Thread(target=scan2)
    thread1.start()
    thread2.start()

# lock.release()
if __name__ == "__main__":
    main()
