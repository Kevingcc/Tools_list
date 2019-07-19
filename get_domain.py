#!/usr/bin/env python3
#coding:utf-8



from sys import argv
from lib import get_domain


try:
    if argv[1] == '-h' or argv[1] == '-help':
        print('usage:')
        print('     批量处理url提取域名.')
        print('     path.')
        print('     save_path.')


    path = argv[1]
    save_path = argv[2]

    with open(path,'r') as r:
        for line in r.readlines():
            url = line
            domain = get_domain(url)
            with open(save_path,'a+') as w:
                w.write(domain+'\n')
except:
    print('usage:')
    print('     批量处理url提取域名.')
    print('     path.')
    print('     save_path.')

