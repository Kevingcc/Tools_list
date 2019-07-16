#!/usr/bin/env python3
#coding:utf-8



import time
import re
import traceback
import threading
import selenium
import os
# from multiprocessing import Process
# from multiprocessing import Queue as Qu

from lib import Libs
from src.search import selenium_
from lib import get_headers
from lib import info
from lib import error
from lib import warning
from lib import loads
from lib import AttribDict
from lib import print_
from lib import root
from lib import get_domain
from lib import get_filename
from lib import read_text_
from lib import input_
from lib import regular





foo = AttribDict()
headers = get_headers()
libs = Libs()
event = threading.Event
port_scan_results = []
threadLock = threading.Lock()
s_browser = selenium.webdriver.Chrome()
commands_ = libs.commands_
commands__ = libs.commands__
get_filename = libs.Get_Filename

selenium_ = selenium_()
get_page_num = selenium_.Get_Page_num


# KeyboardInterrupt


# commands
cmd1 = 'xfce4-terminal -e "bash -c \\\"{}\\\""'
cmd2 = "nmap -Pn {} -oX {}lib/nmap_xml/{}"
cmd3 = "python3 {}subdns/subdns.py -u {} -d mini_names.txt"



# dns 查询接口
dns_query1 = "https://dns.bufferover.run/dns?q={}"




class Scann(object):

    def __init__(self):

        self.option = True
        self.option_ = True
        self.event = event()
        self.google_search = selenium_.Google_Search
    

    def CDN_Scann(self):
        pass


    def Subdomain_Enumeration(self,domain):
        """
        Return data:
            data[0] >> domain
            data[1] >> ip
        """
        
        try:
            # threadLock.acquire()
            commands__(cmd=cmd3.format(root,domain))
        except Exception as e:
            pass
        finally:
            # threadLock.release()
            datas = get_filename('{}/output'.format(root))
            i = 0
            for data in datas:
                if os.path.getsize(datas) > 0:
                    if i == len(datas): 
                        foo.state1 = True
                i += 1
        
        


    def Collect_known_domain(self,domain):
        links = []
        d1 = domain.split('.')
        domain = d1[-2]+'.'+d1[-1]
        number = get_page_num(keyword='site:{}'.format(domain))
        datas = self.google_search(keyword='site:{}'.format(domain),number=int(number))
        try:
            for data in datas:
                link = data[1]
                if re.findall('http',link) or re.findall('https',link):
                    link = get_domain(link)
                    links.append(link)
        except Exception as e:
            # error(traceback.format_exc())
            pass

        foo.state2 = True
        return links



    def Result_Compare(self,**kwargs):
        """
        去掉重复的结果.
        """
        # global da1
        # global da2
        da1 = ''
        da2 = ''
        ds = []

        if 'S1' in kwargs:
            da1 = kwargs['S1']
        
        if 'C1' in kwargs:
            da2 = kwargs['C1']

        for da_3 in da1:
            datas = [da_3[0]] + da2
            datas_ = datas
            ds.append(datas_)

        ds1 = []
        for d1 in ds:
            if isinstance(d1,list):
                for d2 in d1:
                    ds1.append(d2)

        ds2 = []
        for d1 in ds:
            if isinstance(d1,str):
                ds2.append(d2)
        
        ds3 = list(set(ds1+ds2))

        return ds3









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



    # def get_domain(self,domain):
    #     d1 = domain.split('/')
    #     for d2 in d1:
    #         if \
    #         d2 != 'https' and \
    #         d2 != 'http' and \
    #         d2 != '/' and \
    #         d2 and \
    #         d2 != 'https:' and \
    #         d2 != 'https:/' and \
    #         d2 != 'http:' and \
    #         d2 != 'http:/':
    #             return d2.strip()



    def DNS_Query_Interface(self,domain):
        """
        DNS接口查询
        """
        # threadLock.acquire()
        #方法：add_cookie(cookie={'':'','':''})
        try:
            datas_d1 = []
            datas_d2 = []
            warning(('Query Domain -> '+domain))
            selenium_.browser_.get(dns_query1.format(domain))
            time.sleep(7)
            htmldoc = selenium_.browser_.find_element_by_xpath('/html/body/pre').text
            data = loads(htmldoc)
            # info(data['RDNS'])
            try:
                if 'FDNS_A' in data:
                    data1 = data['FDNS_A']
                    for data_1 in data1:
                        find1 = re.findall(regular(1),data_1)
                        find2 = re.findall(regular(2),data_1)
                        find3 = re.findall(regular(3),data_1)
                        d1 = data_1.split(',')
                        
                        if find1:
                            ips = d1[0]
                        if find2 or find3:
                            domains = d1[1]
                        if ips or domains:
                            datas_d1.append([ips,domains])

            except:
                pass
            
            try:
                if 'RDNS' in data:
                    data2 = data['RDNS']
                    for data_2 in data2:
                        find1 = re.findall(regular(1),data_2)
                        find2 = re.findall(regular(2),data_2)
                        find3 = re.findall(regular(3),data_2)
                        d2 = data_2.split(',')
                        if find1:
                            ips = d2[0]
                        if find2 or find3:
                            domains = d2[1]
                        if ips or domains:
                            datas_d2.append([ips,domains])
            except:
                pass
            
            foo.Dns_Qery = [datas_d1,datas_d2]

            for d1 in foo.Dns_Qery[0]:
                ip = d1[0]
                if ip:
                    domain = d1[1]
                    thread1 = threading.Thread(target=self.port_scan,args=(ip,ip))
                    time.sleep(1)
                    thread1.start()
                    info('域名:{} -> 查询IP:{}'.format(domain,ip))

            for d1 in foo.Dns_Qery[1]:
                ip = d1[0]
                if ip:
                    domain = d1[1]
                    thread2 = threading.Thread(target=self.port_scan,args=(ip,ip))
                    time.sleep(1)
                    thread2.start()
                    info('域名:{} -> 查询IP:{}'.format(domain,ip))
            
            selenium_.browser_.quit()
            return True
            
        except Exception as e:
            selenium_.browser_.quit()
            error(traceback.format_exc())
            i = 0
            while True:
                if i == 3:
                    if self.DNS_Query_Interface(domain=domain):
                        break
                    i = 0
                i += 1
        
        # threadLock.release()
        

    def port_scan(self,domain,filename):
        """
        nmap scann
        """
        try:
            libs.commands_(cmd=[cmd2.format(domain,libs.root,filename)])
            time.sleep(10)
            data1 = libs.commands_(cmd=['sudo python2 {}lib/nmap_xml.py {}lib/nmap_xml/{}'.format(libs.root,libs.root,filename)]).strip()
            # data1 = exec('data1 = '+data1)
            data1 = eval(data1)
            foo.nScan_Result = data1
            for i in range(0,2):
                for d1 in foo.nScan_Result[i]:
                    if 'ip' in d1 and \
                       'port' in d1 and \
                       'state' in d1 and \
                       'agreement' in d1:
                        
                        ip = d1.get('ip')
                        port = d1.get('port')
                        state = d1.get('state')
                        agreement = d1.get('agreement')
            
                        if ip:
                            if state != 'closed':
                                info(ip+':'+port+' /'+state+' '+'-'+agreement)
                                if port == '443' or port == '80':
                                    w = open('{}lib/Nmap_Result/nScan_Result.txt'.format(libs.root),'a+')
                                    w.write('{"ip":"%s","port":"%s","state":"%s","agreement":"%s"}' % (ip,port,state,agreement))
                                    w.write('\n')
                                    warning('写入 lib/batch/nScan_Result.txt ...')
                                    w.close()
                        
                            else:
                                error(ip+':'+port+' /'+state+' '+'-'+agreement)
            
        except Exception as e:
            # error(traceback.format_exc())
            pass
            
        
        
    def sub_domain(self):
        pass


    # def jietu(self,domain):
    #     try:
    #         # self.browser_.set_page_load_timeout(5)
    #         _browser.get(str(domain))
    #         _browser.save_screenshot('lib/img/{}.png'.format(str(domain).replace('https://','').replace('http://','')))
    #         _browser.quit()
    #         # self.browser_.close()
    #     except:
    #         error(traceback.format_exc())
    #         error('截图此：{}超时...'.format(domain))
    #         pass


    def main(self):
        print_("""
1.DNS接口查询.
0.Exit.
""")
        ipt1 = input_('选项>')
        if ipt1 is '1':
            print_("""
 ____  _   _        ___                        
|  _ \| \ | |___   / _ \ _   _  ___ _ __ _   _ 
| | | |  \| / __| | | | | | | |/ _ \ '__| | | |
| |_| | |\  \__ \ | |_| | |_| |  __/ |  | |_| |
|____/|_| \_|___/  \__\_\\\\__,_|\___|_|   \__, |
                                         |___/ 

1.批量查询
2.单个查询
0.返回菜单.
            """)            
            ipt2 = input_('>')
            if ipt2 is '0':
                self.main()
            if ipt2 is '1':
                ipt3 = input_('处理URL获取Domain name.[y/n]')
                filenames = get_filename(path='{}lib/batch'.format(root))
                for filename in filenames:
                    print_(filename)
                ipt4 = input_('Filename>')
                lines = read_text_(ipt4)
                for line in lines:
                    if ipt3 == 'y':
                        domain = get_domain(line)
                        self.DNS_Query_Interface(domain)
                    if ipt3 == 'n':
                        domain = line
                        self.DNS_Query_Interface(domain)
            if ipt2 is '2':
                ipt3 = input_('Domain>')
                self.DNS_Query_Interface(ipt3)


        if ipt1 is '0':
            selenium_.browser_.quit()
            exit(0)

            
        


    def run(self):
        self.main()
        







def main():

    scan1 = Scann()
    scan1.run()


    




if __name__ == "__main__":
    s_browser.minimize_window()
    main()
    # queue = Queue()
    # s = Scann(queue=queue,domain='')
    # s.Subdomain_Enumeration(domain='')
    # selenium_.browser.quit()
    selenium_.browser_.quit()
    # s_browser.quit()




# queue = Queue()
# s = Scann(queue=queue,domain=['https://www.baidu.com','https://www.so.com'])

# # s.port_scan(domain='www.baidu.com',filename='baidu.xml')
# # info(foo.nScan_Result[0]['ip'])

# # s.DNS_Query_Interface(domain='baidu.com')
# # info(foo.Dns_Qery)

# s.Sqli_Scann()

# selenium_.browser.quit()
# selenium_.browser_.quit()
















# from queue import Queue
# from threading import Thread
# import time

# class Student(Thread):
#     def __init__(self, name, queue):
#         super().__init__()
#         self.name = name
#         self.queue = queue

#     def run(self):
#         while True:
#             # 阻塞程序，时刻监听老师，接收消息
#             msg = self.queue.get()
#             # 一旦发现点到自己名字，就赶紧答到
#             if msg == self.name:
#                 print("{}：到！".format(self.name))
            
#             if self.queue.empty():
#                 exit(0)



# class Teacher:
#     def __init__(self, queue):
#         self.queue=queue

#     def call(self, student_name):
#         print("老师：{}来了没？".format(student_name))
#         # 发送消息，要点谁的名
#         self.queue.put(student_name)


# queue = Queue()
# teacher = Teacher(queue=queue)
# s1 = Student(name="小明", queue=queue)
# s2 = Student(name="小亮", queue=queue)
# s1.start()
# s2.start()


# print('开始点名~')
# teacher.call('小明')
# time.sleep(1)
# teacher.call('小亮')










































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

# s = Scann()






































# class test(threading.Thread):

#     def __init__(self,queue):
#         super(test,self).__init__()
#         self.queue = queue

#     def t1(self):
#         self.queue.put('hello t1')
#         self.queue.put('hello t1_1')
#         self.queue.put([1,2,3,4,5])
#         self.queue.put({1:'1a',2:'2a'})
#         self.queue.put((11,22,33))
#         self.queue.put({'test1':1})
#         self.queue.put({'test1':2})


#     def t2(self):
#         while True:
#             time.sleep(1)
#             print('hello t2')

#     def t3(self):
#         while True:
#             time.sleep(1)
#             print('hello t3')


#     def run(self):
#         th1 = threading.Thread(target=self.t1)
#         th2 = threading.Thread(target=self.t2)
#         th3 = threading.Thread(target=self.t3)
        
#         # 并发执行
#         th1.start()
#         # 获取队列元素[1]
#         print(self.queue.get())
#         # 获取队列元素[2]
#         print(self.queue.get())
#         # 获取队列元素[3]
#         print(self.queue.get())
        
#         print(self.queue.get())
#         print(self.queue.get())
#         print(self.queue.get()['test1'])
#         print(self.queue.get()['test1'])


#         # th2.start()
#         # th3.start()
        
#         # 正常执行
#         # self.t1()
#         # self.t2()
#         # self.t3()




# queue = Queue()
# t = test(queue)
# t.start()
# selenium_.browser.quit()
# selenium_.browser_.quit()

# """
# result:
#     hello t1
#     hello t1_1
#     [1, 2, 3, 4, 5]
#     {1: '1a', 2: '2a'}
#     (11, 22, 33)

# """






