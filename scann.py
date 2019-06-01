#!/usr/bin/env python3
#coding:utf-8




from awvs_api import awvs
from search import Exploit_Search
from main import Libs



class Add(awvs):
    
    def __init__(self,target,rule):
        super(Add,self).__init__(target,rule)
    

    def add_task(self):
        self.scan_()
        




class Scann(object):

    def __init__(self):
        self.add = Add
        self.libs = Libs()
        self.read_text = self.libs.Read_text
    
    
    def add_task(self,target,rule):
        add = self.add(target=target,rule=rule)
        add.add_task()

    
    def get_target_url(self):
        d1 = []
        d2 = []
        datas1 = self.read_text(filename='sqli1.txt')
        datas2 = self.read_text(filename='sqli2.txt')
        
        i = 1
        for data1 in datas1:
            
            d1.append(data1)
            i += 1

        for data2 in datas2:
            d2.append(data2)

        return (d1,d2)



    def Sqli_Scann(self):
        datas = self.get_target_url()
        
        for target1 in datas[0]:
            self.add_task(target=target1,rule='3')

        for target2 in datas[1]:
            self.add_task(target=target1,rule='3')


    def main(self):
        self.Sqli_Scann()








    
    


    