#!/usr/bin/env python3
#coding:utf-8



import time
import re
from awvs_api import awvs
from search import Exploit_Search
from main import Libs



class awvs_(awvs):
    
    def __init__(self,target,rule):
        super(awvs_,self).__init__(target,rule)

    def add_task(self):
        self.scan_()

    def delete(self):
        self.delete_()
        




class Scann(object):

    def __init__(self):
        self.awvs = awvs_
        self.libs = Libs()
        self.read_text = self.libs.Read_text
        self.option = True
    
    
    def add_task(self,target,rule):
        add = self.awvs(target=target,rule=rule)
        add.add_task()

    
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
        delete = self.awvs(target='',rule='')
        delete.delete_()


    def Sqli_Scann(self):
        datas = self.get_target_url()
        self.delete_()
        
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


    def main(self):
        self.option = True
        self.Sqli_Scann()








    
    


    