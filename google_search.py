#!/usr/bin/env python3
#coding:utf-8

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
except Exception as e:
    pass

import requests
import os
import subprocess
import threading
import re
from queue import Queue
from src.search import selenium_
from lib import info
from lib import print_

# /html/body/dl/dt/dl/dt[50]/dl/dt/a




root_ = subprocess.check_output('echo $HOME',shell=True).decode().strip()
root = '{}/.Tools/Tools_list/'.format(root_)

browser_option = webdriver.ChromeOptions()
browser_option.add_argument('--load-extension={}lib/ReplaceGoogleCDN/chrome'.format(root))
browser = webdriver.Chrome(
    chrome_options=browser_option
)

# print('{}lib/chrome'.format(root))
class Search(object):
    
    def __init__(self,queue):
        self.__flag = threading.Event()
        self.__flag.set()
        self.__running = threading.Event()
        self.__running.set()
        self.queue = queue
        self.option = True
        self.selenium_ = selenium_()
        self.Google_Search = self.selenium_.Google_Search
        self.browser = self.selenium_.browser
        self.browser_ = self.selenium_.browser_


    def Get_Filename(self,path):
            """
            获取指定目录下的所有文件绝对路径.
            """
            pathname = []
            catalog = path
            for (dirpath, dirnames, filenames) in os.walk(catalog):     
                for filename in filenames:  
                    pathname += [os.path.join(dirpath, filename)]
            
            return pathname        


    def Website_search(self,keyword,number=3):
        sources = ['github.com','cnblogs.com','github.io','csdn.net']
        for url in sources:
            datas = self.Google_Search(keyword='site:{} {}'.format(url,keyword),number=number)
            for data in datas:
                link = data[1]
                self.Save(content=link)
        

    def Save(self,content):
        with open('{}lib/Search_Url.txt'.format(root),'a+') as w:
            w.write(content+'\n')


    def Find_Keyword__(self,keyword1,keyword2):
        self.Website_search(keyword=keyword1)
        with open('{}lib/Search_Url.txt'.format(root),'r') as r_:
            for link in r_.readlines():
                r = requests.get(link.strip())
                html = r.text
                scode = r.status_code
                if scode == 200:
                    com_ = re.compile(keyword2)
                    if com_.findall(html):
                        info('Url -> {}'.format(link))  
                        with open('{}lib/Search_Url_.txt'.format(root),'a+') as w:
                            w.write(link+'\n')


    def main(self):
        try:
            print_("""

1.网站搜索.
0.Exit.
            """)
            self.option = False
            browser.minimize_window()
            ipt1 = input('>')
            if ipt1 is '1':
                ipt2 = input('Google Search Keyword>')
                ipt3 = input('Result Search Keyword>')
                self.Find_Keyword__(keyword1=ipt2,keyword2=ipt3)
            if ipt1 is '0':
                exit(0)
            
            browser.quit()
            self.browser.quit()
            self.browser_.quit()
        except:
            browser.quit()
            self.browser.quit()
            self.browser_.quit()


#queue = Queue()
#s = Search(queue)
#s.main()


    
    

# start = time.clock()

# #当中是你的程序
# time.sleep(3)
# elapsed = (time.clock() - start)
# print("Time used:",elapsed)



# from queue import Queue
# # maxsize默认为0，不受限
# # 一旦>0，而消息数又达到限制，q.put()也将阻塞
# q = Queue(maxsize=0)

# # 阻塞程序，等待队列消息。
# q.get()

# # 获取消息，设置超时时间
# q.get(timeout=5.0)

# # 发送消息
# q.put()

# # 等待所有的消息都被消费完
# q.join()

# # 以下三个方法，知道就好，代码中不要使用

# # 查询当前队列的消息个数
# q.qsize()

# # 队列消息是否都被消费完，True/False
# q.empty()

# # 检测队列里消息是否已满
# q.full()
