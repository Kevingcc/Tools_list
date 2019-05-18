#coding:utf-8


import re
import threading
import json
import time
import os
import traceback
import random

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
        #配置代理.
        # self.chrome_options2.add_argument('--proxy-server=http://202.20.16.82:10152')
        # self.chrome_options2.add_argument('window-size=1000x1000')
        self.browser = webdriver.Chrome(
            chrome_options=self.chrome_options1
        )
        self.browser_ = webdriver.Chrome(
            chrome_options=self.chrome_options2
        )
        self.browser.minimize_window()
        self.browser_.minimize_window()
        # self.browser.close()
        # self.browser_.close()
        id_ = self.Getting_plug_ins_id()
        self.login_url = 'chrome-extension://{}/login.html'.format(id_)

        self.Filter_List = ['not a robot','人机','验证','身份']

        self.cookie = ''


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
        try:
            self.browser.get(self.login_url)
            self.browser.minimize_window()
            if os.path.getsize('{}lib/login.json'.format(self.root)) <= 0:
                print('谷歌访问助手插件的账号及密码登入...')
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
        except Exception as e:
            print('Login_Google_CRX = ',traceback.format_exc())
            pass

    def requests_(self,content):
        self.Login_Google_CRX()
        if not os.path.getsize('{}lib/cookies.txt'.format(self.root)) <= 0:
            cookies = self.Read_text('cookies.txt')
            for cookie in cookies:
                cookie = eval(cookie.strip())
                if cookie:
                    self.cookie = random.choice(cookie)
                    print('cookie = ',self.cookie)

        time.sleep(10)
        self.browser.get('https://www.google.com')
        
        if self.cookie:
            self.browser.add_cookie(self.cookie)
        
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

        # self.browser.quit()
        try:
            time.sleep(10)
            self.browser_.get('https://www.exploit-db.com/google-hacking-database')
            self.browser_.minimize_window()
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
                    # print(traceback.format_exc())
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
                    # print(traceback.format_exc())
                    # self.browser_.close()
                    break
                
            print('GHack爬取完毕...')
            # self.browser_.quit()
        except Exception as e:
            # print(traceback.format_exc())
            pass


    def test(self):
        self.GHack('ftp','ftp','ftp')
        


    def Verification_Handle(self,htmldoc):
        for Filter in self.Filter_List:
            pattern = re.compile(Filter+'*')
            if pattern.findall(htmldoc):
                print('发现google验证...')
                if os.path.getsize('{}lib/cookies.txt'.format(self.root)) <= 3000:
                    ipt1 = input('手动验证完成[y|n]')
                    if ipt1:
                        if ipt1 is 'y':
                            cookies = self.browser.get_cookies()
                            print('cookies = ',cookies)
                            self.Save_text_('cookies.txt',cookies)
                            print('继续爬取数据...')
                        if ipt1 is 'n':
                            pass
                    return False
            return True
            

    def Google_Search(self,keyword,number=26):
        """
        keyword：Search keyword.
        number：Page number.
        data[0] = Title
        data[1] = Link
        """
        # mutex.release()
        # thread2 = threading.Thread(target=self.requests_,args=())
        # thread1 = threading.Thread(target=self.Config_chromedriver())
        # thread2 = threading.Thread(target=self.requests_())
        # thread1.start()
        # thread2.start()
        try:
            # self.browser_.quit()
            result1 = []
            self.requests_(keyword)
            htmldoc1 = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")
            # self.browser.minimize_window() 
            # print('htmldoc1 = ',htmldoc1)           
            if self.Verification_Handle(htmldoc1):
                try:
                    htmldoc2 = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")
                    self.Verification_Handle(htmldoc2)
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
                                    htmldoc3 = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")
                                    self.Verification_Handle(htmldoc3)

                        if i+1 == number+1:
                            # self.browser.close()
                            break

                        if i+1 == 27:
                            # self.browser.close()
                            break
                        
                        for i2 in range(1,11):
                            try:
                                time.sleep(0.5)
                                #Title
                                elements1 = self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/div[1]/a[1]/h3'.format(i2))
                                #link
                                elements2 = self.browser.find_element_by_xpath('//*[@id="rso"]/div/div/div[{}]/div/div/div[1]/a[1]'.format(i2)).get_attribute('href')
                                
                                print('title = ',elements1.text)
                                print('link = ',elements2)
                                result1.append([elements1.text,elements2])
                        
                            except Exception as e:
                                # print(traceback.format_exc())
                                pass
                        
                        print('下一页...')
                        i += 1
                    
                    # self.browser.quit()
                    return result1
                        
                except Exception as e:
                    # print(traceback.format_exc())
                    pass
        except Exception as e:
            print(traceback.format_exc())
            pass        





class Exploit_Search(object):
    """
    通过Google hack 搜索可利用的漏洞.
    """
    def __init__(self):
        self.selenium_ = selenium_()
        self.google_search = self.selenium_.Google_Search
        self.query = self.selenium_.Query_Data
        self.GHack = self.selenium_.GHack
        self.Save_text = self.selenium_.Save_text
        self.Read_text = self.selenium_.Read_text
        self.browser = self.selenium_.browser
        self.browser_ = self.selenium_.browser_

    def CVE_Exploit(self):
        """
        收集存在CVE漏洞的站点.
        """
        pass

    def FTP_Exploit(self):
        """
        收集存在FTP漏洞的站点.
        """
        pass

    def WEB_Frame_Exploit(self):
        """
        收集指定版本的WEB框架存在漏洞的站点.
        """
        pass

    def Sqli_Exploit(self):
        """
        收集存在sqli的站点.
        """
        result1 = self.Sqli_Search(keyword='sqli',filename='sqli1.txt')
        if result1:
            self.browser.quit()
            self.browser_.quit()
            print('Sqli 站点收集完成...')
        
        result2 = self.Sqli_Search(keyword='sql',filename='sqli2.txt')
        if result2:
            self.browser.quit()
            self.browser_.quit()
            print('Sqli 站点收集完成...')

        return True
    
    def Xss_Exploit(self):
        """
        收集存在xss的站点.
        """
        pass

    def CSRF_Exploit(self):
        """
        收集存在CSRF的站点.
        """
        pass

    def Sqli_Search(self,keyword,filename):
        try:
            self.GHack(keyword=keyword,type_='sqli',title='sqli')
            query = self.query(type_='sqli')
            for query_ in query:
                content = query_[4]
                google_search = self.google_search(keyword=content,number=3)
                for google_search_ in google_search:
                    title = google_search_[0]
                    link = google_search_[1]
                    self.Save_text(filename=filename,content=link)
            return True
        except Exception as e:
            pass
        
                





# s = selenium_()
# # s.Kill_chromedriver()
# s.run()

# driver.back() 
# driver.forward() 
# driver.refresh()



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

