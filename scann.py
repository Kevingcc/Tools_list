#!/usr/bin/env python3
#coding:utf-8



import time
import re
import requests
import socket
import traceback
import threading
from awvs_api import awvs
from search import Exploit_Search
from main import Libs
from search import selenium_
from lib import get_headers
from lib import info
from lib import error
from lib import warning
from lib import loads



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
        self.selenium_ = selenium_()
        self.browser = self.selenium_.browser
        self.browser_ = self.selenium_.browser_
    
    
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
                    info(('target -> ',target1))
                self.add_task(target=target1,rule='3')
            else:
                i = 0
                time.sleep(600)
            i += 1

        i = 1
        for target2 in datas[1]:
            if i <= 5:
                if self.option:
                    info(('target -> ',target1))
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

    def DNS_Query_Interface(self,domain):
        """
        DNS接口查询
        """
        #方法：add_cookie(cookie={'':'','':''})
        try:
            self.browser_.get(dns_query1.format(domain))
            # htmldoc = self.browser_.find_element_by_xpath('//*').get_attribute("outerHTML")
            time.sleep(7)
            htmldoc = self.browser_.find_element_by_xpath('/html/body/pre').text
            data = loads(htmldoc)
            # print(data['RDNS'])
            return data['RDNS']
        except Exception as e:
            error(traceback.format_exc())
            self.DNS_Query_Interface(domain=domain)
        

    def port_scan(self,host=[],port=[]):
        ports = []
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        try:
            for z in port:
                for h in host:
                    s.connect(('{}'.format(h),int(z)))
                    ports.append(z)
        except:
            pass
        
        return ports


    def jietu(self,url):
        try:
            self.browser_.set_page_load_timeout(5)
            self.browser_.get(url)
            self.browser_.save_screenshot('lib/img/{}.png'.format(str(url).replace('https://','').replace('http://','')))
            self.browser_.close()
        except:
            error('截图此：{}超时...'.format(url))
            pass

    def port_scan_nmap(self):
        pass

    def main(self,host,post,domain):
        # thread1 = threading.Thread(target=self.Sqli_Scann,args='')
        thread1 = threading.Thread(target=self.Sqli_Scann)
        thread2 = threading.Thread(target=self.port_scan,args=(host,post))
        thread3 = threading.Thread(target=self.DNS_Query_Interface,args=(domain))






# s = Scann()
# data = s.DNS_Query_Interface(domain='www.baidu.com')
# print(data)
# s.browser_.quit()
# s.browser.quit()

# s = Scann()
# result = s.port_scan(host=['www.baidu.com'],port=[80,443,333,222])
# print(result)
# s.browser.quit()
# s.browser_.quit()

s = Scann()
s.main()

