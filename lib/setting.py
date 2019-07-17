#!/usr/bin/env python3
#coding:utf-8

import os


root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'

"""

-------
属性设置
-------

"""

option_install = False

"""
awvs server
awvs apikey
"""
awvs_server = 'https://127.0.0.1:13443/api/v1'
awvs_apikey = ''

"""
nessus server
nessus apikey
"""
nessus_server = ''
nessus_secretKey = ''
nessus_accessKey = ''


"""
google 插件账号登入
"""
username = ''
password = ''


"""
zoomeye username and password
"""
username_z = ''
password_z = ''


"""
系统平台

可选参数:
    Linux:
        kali
        deepin

"""
system_platform = 'kali'


"""
九世信息收集工具配置
"""
def jiushixxsj(url,domain,
               thread=100,xianc=20,
               directory=10000,subdomain=10000,
               domain_baopo=0,dire_path='dict/scan.txt'):
    content = """
# @author:九世
# @time:2019/7/2
# @file:mian.py

URL='{}' #输入要进行探测的url
DOMAIN='{}' #输入要进行探测的域名
THREAD={} #协程设置
XIANC={} #进程数设置
DIRECTORY={} #目录扫描的协程设置
SUBDOMAIN={} #子域名爆破协程设置
DOMAIN_BAOPO={} #0为不开启子域名爆破，1为开启
DIRE_PATH=r'{}' #引用dict目录下的指定字典
    """.format(url,domain,thread,xianc,directory,subdomain,domain_baopo,dire_path)

    with open('{}信息收集工具/config/config.py'.format(root),'w') as w:
        w.write(content)
    
    return True


"""
是否添加秘钥
"""
key_config = False


"""
Install Chrome.
"""
Ichrome = True


"""
root 模式下 add user
"""
kali_user = True
