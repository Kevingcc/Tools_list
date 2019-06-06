#!/usr/bin/env python3
#coding:utf-8



import time
import re
from awvs_api import awvs
from search import Exploit_Search
from main import Libs
from lib.headers import get_headers


        


headers = get_headers()


# commands
cmd1 = "xfce4-terminal -e {}"



# dns 查询接口
dns_query1 = "https://dns.bufferover.run/dns?q={}"





class Scann(object):

    def __init__(self):
        self.awvs = awvs
        self.libs = Libs()
        self.read_text = self.libs.Read_text
        self.option = True
    
    
    def add_task(self,target,rule):
        add = self.awvs(target=target,rule=rule)
        add.add_()

    
    def get_target_url(self):
        d1 = []
        d2 = []
        datas1 = self.read_text(filename='sqli1.txt')
        datas2 = self.read_text(filename='sqli2.txt')
        
        for data1 in datas1:
            if not data1.find('.xls') != -1 and not data1.find('.sql') != -1 \
                and not data1.find('.txt') != -1:    
                d1.append(data1)

        for data2 in datas2:
            if not data2.find('.xls') != -1 and not data2.find('.sql') != -1 \
                and not data2.find('.txt') != -1:
                d2.append(data2)

        return (d1,d2)


    def delete_(self):
        delete_ = self.awvs(target='',rule='')
        delete_.delete_()

    def delete(self):
        delete = self.awvs(target='',rule='')
        delete.delete()

    def Sqli_Scann(self):
        datas = self.get_target_url()
        
        if self.option:
            print("""
    1.删除所有任务.
    2.删除单个任务.
    3.跳过.
    0.Exit.
            """)
            ipt1 = input('>')
            if ipt1 is '1':
                self.delete_()
                ipt2 = input('显示细节[y/n]>')
                if ipt2 is 'y':
                    pass
                if ipt2 is 'n':
                    self.option = False
            if ipt1 is '2':
                self.delete()
                ipt2 = input('显示细节[y/n]>')
                if ipt2 is 'y':
                    pass
                if ipt2 is 'n':
                    self.option = False
            if ipt1 is '3':
                pass
            if ipt1 is '0':
                exit(0)

        i = 1
        for target1 in datas[0]:
            if i <= 5:
                if self.option:
                    print('target -> ',target1)
                self.add_task(target=target1,rule='3')
            else:
                i = 0
                time.sleep(600)
            i += 1

        i = 1
        for target2 in datas[1]:
            if i <= 5:
                if self.option:
                    print('target -> ',target1)
                self.add_task(target=target1,rule='3')
            else:
                i = 0
                time.sleep(600)
            i += 1


    def CDN_Scann(self):
        self.libs.commands__(cmd='')


    def Subdomain_Enumeration(self):
        pass


    def Collect_known_domain(self):
        pass


    def DNS_Query_ZZ(self):
        """
        站长之家nslookup查询 http://tool.chinaz.com/nslookup/
        """
        pass

    def DNS_Query_ZZ_(self):
        """
        站长之家whois查询 http://whois.chinaz.com/
        """
        pass

    def DNS_Query_Interface(self):
        """
        DNS接口查询
        """
        pass

    def main(self):
        self.Sqli_Scann()








    
    


    