#!/usr/bin/env python3
#coding:utf-8



import time
import threading
from src.awvs_api import awvs
from lib import input_
from lib import print_
from lib import get_filename
from lib import read_text_
from lib import get_domain
from lib import root
from lib import info
from main import Run




class awvs(object):

    def __init__(self):
        self.awvs = awvs
        self.option = True
        self.option_ = True

    def add_task(self,target,rule):
        add = self.awvs(target=target,rule=rule)
        add.add_()

    def delete_(self):
        delete_ = self.awvs(target='',rule='')
        delete_.delete_()

    def delete(self):
        delete = self.awvs(target='',rule='')
        delete.delete()

    def _add_task(self,rule):

            print_("""
    1.批量任务添加
    2.删除所有任务
    3.删除指定任务
    4.跳过
    0.Exit.
            """)
            
            if self.option_:

                ipt1 = input_('>')
                if ipt1 is '1':
                    domains = []
                    ipt2 = input_('处理URL获取Domain name.[y/n]')
                    if ipt2 is 'y':
                        i1 = True
                    if ipt2 is 'n':
                        i1 = False
                    filename = get_filename('{}lib/batch/awvs'.format(root))
                    i = 1
                    for f in filename:
                        print_(f'{i}. {f}')
                        i += 1
                    ipt3 = input_('Path编号>')
                    i = 1
                    for f in filename:
                        if ipt3 == str(i):
                            ipt3 = f
                            break
                        i += 1
                    if ipt3:
                        datas = read_text_(ipt3)
                        if i1:
                            for data in datas:
                                d = get_domain(data)
                                domains.append(d)
                    datas = domains
                    
                if ipt1 is '2':
                    self.delete_()
                    ipt2 = input_('显示细节[y/n]>')
                    if ipt2 is 'y':
                        pass
                    if ipt2 is 'n':
                        self.option = False
                if ipt1 is '3':
                    self.delete()
                    ipt2 = input_('显示细节[y/n]>')
                    if ipt2 is 'y':
                        pass
                    if ipt2 is 'n':
                        self.option = False
                if ipt1 is '4':
                    self.option_ = False
                
                eXit = False if not ipt1 is '0' else True

            try:
                def r():
                    if eXit:
                        return False
                    i = 1
                    for target1 in datas:
                        if i <= 5:
                            if self.option:
                                info(('Add scann target -> ',target1))
                            self.add_task(target=target1,rule=rule)
                        else:
                            i = 0
                            time.sleep(600)
                        i += 1
                thread1 = threading.Thread(target=r)
                thread1.start()
            except Exception as e:
                # red(traceback.format_exc())
                pass


    def main(self):
        print_("""
1.awvs.
0.返回菜单.
        """)
        ipt1 = input_('选项>')
        if ipt1 is '1':
            print_("""
    ___        __       ____  
   / \ \      / /_   __/ ___| 
  / _ \ \ /\ / /\ \ / /\___ \ 
 / ___ \ V  V /  \ V /  ___) |
/_/   \_\_/\_/    \_/  |____/ 


AWVS 配置:
[0] 全扫描
[1] 高风险漏洞
[2] 跨站点脚本漏洞
[3] SQL注入漏洞
[4] 脆弱的密码
[5] 仅爬行'
[x]返回菜单.
    """)    
            ipt2 = input_('配置>')
            if ipt2 is 'x':
                self.main()
            self._add_task(rule=ipt2)

        if ipt1 == '0':
            r = Run()
            r.main()

