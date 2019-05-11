#coding:utf-8


import re
import threading
import json
import time
import os
import traceback

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
except Exception as e:
    pass

from main import Libs


mutex = threading.Lock()

# python3 -m pip install selenium
# json.load(r) 




class selenium_(Libs):
    def __init__(self):
        super(selenium_,self).__init__()
        self.chrome_options1 = webdriver.ChromeOptions()
        self.chrome_options1.add_argument('--load-extension={}lib/ghelper'.format(self.root))
        self.chrome_options2 = webdriver.ChromeOptions()
        self.chrome_options2.add_argument('--load-extension={}lib/ReplaceGoogleCDN/chrome'.format(self.root))
        self.browser = webdriver.Chrome(
            chrome_options=self.chrome_options1
        )
        self.browser_ = webdriver.Chrome(
            chrome_options=self.chrome_options2
        )
        id_ = self.Getting_plug_ins_id()
        self.login_url = 'chrome-extension://{}/login.html'.format(id_)

    def Kill_chromedriver(self):
        # mutex.acquire()
        c1 = self.commands_(cmd=['ps -aux |grep chromedriver | cut -c 10-14'])
        c2 = c1.strip().split('\n')
        for c3 in c2:
            c4 = self.commands__(cmd='sudo kill {}'.format(c3))


    def Getting_plug_ins_id(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_extension('{}lib/Ghelper_1.4.6.crx'.format(self.root))
        # browser_driver = webdriver.Chrome()
        # browser_driver.get("https://www.baidu.com")
        # browser.get('http://ip138.com')
        if os.path.getsize('{}lib/id.json'.format(self.root)) <= 0:
            print('正在打开URL：chrome://extensions/')
            self.browser.get('chrome://extensions/')
            print('复制插件id...')
            print('点击详细信息后，即可查看id...')
            print('例子：chrome://extensions/?id=mcholjcecoiejoamfejfaadoefkcodok')
            print('如果已输入id则跳过此步骤,按回车即可跳过...')
            ipt1 = input('ID>')
            if ipt1:
                data1 = {'id':'{}'.format(ipt1)}
                self.Save_json(data=data1)
                print('ID保存成功...')

        print('ID已存在...')
        data2 = self.Read_json()
        i = 0
        for data3 in data2:
            if i == 0:
                if not os.path.getsize('{}lib/id.json'.format(self.root)) <= 0:
                    data3 = json.loads(data3)
                    # print('插件id：{}'.format(data3['id']))
                    return data3['id']
            i += 1
    
    def Login_Google_CRX(self):
        self.browser.get(self.login_url)
        if os.path.getsize('{}lib/login.json'.format(self.root)) <= 0:
            email = input('Email>')
            password = input('Password>')
            data1 = {'email':email,'password':password}
            self.Save_json(data=data1,filename='login.json')

        time.sleep(2)
        data2 = self.Read_json(filename='login.json')

        i = 0
        for line in data2:
            if i == 0:
                line = json.loads(line)
                # print('line -> ',line)
                email = line['email']
                password = line['password']
                time.sleep(10)
                log_email = self.browser.find_element_by_id('email').send_keys(email)
                log_password = self.browser.find_element_by_id('password').send_keys(password)
                log_password = self.browser.find_element_by_id('password').send_keys(Keys.ENTER)
                print('登入成功...')

            i += 1

    def requests_(self,content):
        self.Login_Google_CRX()
        time.sleep(10)
        self.browser.get('https://www.google.com')
        Search_G = self.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input').send_keys(content)
        Search_ENTER = self.browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input').send_keys(Keys.ENTER)

    
    def GHack_Page_num(self):
        pass


    def GHack(self,keyword,type_,title):

        # next page number 315
        # //*[@id="exploits-table_next"]/a

        # 1-15
        # //*[@id="exploits-table"]/tbody/tr[{}]/td[2]/a

        # //*[@id="exploits-table_paginate"]/ul/li[3]/a -> 1

        self.browser.close()
        # self.Install_selenium()
        # self.Config_chromedriver()
        time.sleep(10)
        self.browser_.get('https://www.exploit-db.com/google-hacking-database')
        time.sleep(10)
        self.browser_.find_element_by_xpath('//*[@id="exploits-table_filter"]/label/input').send_keys(keyword)
        self.browser_.find_element_by_xpath('//*[@id="exploits-table_filter"]/label/input').send_keys(Keys.ENTER)
        time.sleep(3)

        number = 1
        while True:
            number += 1
            try:
                if number == 1:
                    element1 = self.browser_.find_element_by_xpath('//*[@id="exploits-table_paginate"]/ul/li[{}]/a'.format(number+2))
                    print('Find1 -> //*[@id="exploits-table_paginate"]/ul/li[{}]/a'.format(number+2))
                if number != 1:
                    element1 = self.browser_.find_element_by_xpath('//*[@id="exploits-table_paginate"]/ul/li[{}]/a'.format(number+2)).text
                    if element1 in ['FIRST','PREVIOUS','NEXT','LAST']:
                        print('总页数：{}'.format(number-1))
                        # print('Find -> //*[@id="exploits-table_paginate"]/ul/li[{}]/a'.format(number+2))
                        number = number-1
                        break
            except Exception as e:
                print(traceback.format_exc())
                print('总页数：{}'.format(number-1))
                number = number-1
                break


        for page in range(1,number+1):
            try:
                if page == 1:
                    print('第{}页'.format(page))

                    for num in range(1,16):
                        elements = self.browser_.find_element_by_xpath('//*[@id="exploits-table"]/tbody/tr[{}]/td[2]/a'.format(num)).text
                        # print(elements)
                        if not self.Write_Data(id_=str(page)+'0'+str(num),page=page,type_=type_,title=title,content=elements):
                            self.Write_Data(id_=str(page)+'0'+str(num),page=page,type_=type_,title=title,content=elements)

                if page != 1 and page-1:
                    print('第{}页'.format(page))
                    time.sleep(4)
                    self.browser_.find_element_by_xpath('//*[@id="exploits-table_next"]/a').click()
                    time.sleep(4)

                
                    for num in range(1,16):
                        elements = self.browser_.find_element_by_xpath('//*[@id="exploits-table"]/tbody/tr[{}]/td[2]/a'.format(num)).text
                        # print(elements)
                        if not self.Write_Data(id_=str(page)+'0'+str(num),page=page,type_=type_,title=title,content=elements):
                            self.Write_Data(id_=str(page)+'0'+str(num),page=page,type_=type_,title=title,content=elements)


            except Exception as e:
                print(traceback.format_exc())
                self.browser_.close()
                break
            
        print('GHack爬取完毕...')
        self.browser_.close()



    def Sqli_Search(self):
        pass

    def Ftp_Search(self):
        pass

    def Cve_Search(self):
        pass

    def Xss_Search(self):
        pass

    def test(self):
        self.GHack('ftp','ftp','ftp')
        


    def Google_Search(self,keyword,number=26):
        """
        keyword：Search keyword.
        number：Page number.
        """
        # mutex.release()
        # thread2 = threading.Thread(target=self.requests_,args=())
        # thread1 = threading.Thread(target=self.Config_chromedriver())
        # thread2 = threading.Thread(target=self.requests_())
        # thread1.start()
        # thread2.start()
        self.browser_.close()
        result1 = []
        # self.Install_selenium()
        # self.Config_chromedriver()
        self.requests_(keyword)
        try:
            i = 0
            while True:
            # for i1 in range(2,12):
                print('第{}页'.format(i+1))    
                
                if i+1 < 27:
                    if i != 0:
                        if i+1 < number+1:
                            time.sleep(2)
                            elements = self.browser.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
                            time.sleep(1)
                            elements.click()
                            time.sleep(3)
                
                if i+1 == number+1:
                    self.browser.close()
                    break

                if i+1 == 27:
                    self.browser.close()
                    break
                
                for i2 in range(1,11):
                    try:
                        time.sleep(0.5)
                        #Title
                        elements1 = self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/div[1]/a[1]/h3'.format(i2))
                        #link
                        elements2 = self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/div[1]/a[1]/div/cite'.format(i2))
                        # print('i2 -> ',i2)
                        print(elements1.text)
                        print(elements2.text)
                        result1.append([elements1.text,elements2.text])
                
                    except Exception as e:
                        # print(traceback.format_exc())
                        pass
                
                print('下一页...')
                i += 1
            
            return result1
                
        except Exception as e:
            print(traceback.format_exc())
            pass








# s = selenium_()
# # s.Kill_chromedriver()
# s.run()





# https://www.exploit-db.com/google-hacking-database

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--load-extension=SwitchyOmega')
 
browser = webdriver.Chrome(
    executable_path="./drivers/chromedriver.exe",
    chrome_options=chrome_options
)
browser.get('http://ip138.com')
"""

# Browser.find_element_by_id('password').send_keys(Keys.ENTER)
# log_email.clear()
# login_in_xpath = '//*[@id="submit"]'
# login_in = self.browser.find_element_by_xpath(login_in_xpath)
# login_in.click()







# def test1(self):
#     # chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_extension('{}lib/Ghelper_1.4.6.crx'.format(self.root))
#     # browser_driver = webdriver.Chrome()
#     # browser_driver.get("https://www.baidu.com")
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--load-extension={}lib/ghelper'.format(self.root))
#     browser = webdriver.Chrome(
#         chrome_options=chrome_options
#     )
#     # browser.get('chrome://extensions/')
#     browser.get('http://ip138.com')

