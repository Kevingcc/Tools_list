#coding:utf-8


import re
import threading
import json
import time
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from main import Libs


mutex = threading.Lock()

# python3 -m pip install selenium
# json.load(r) 

class selenium_(Libs):
    def __init__(self):
        super(selenium_,self).__init__()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--load-extension={}lib/ghelper'.format(self.root))
        self.browser = webdriver.Chrome(
            chrome_options=self.chrome_options
        )
        id_ = self.Getting_plug_ins_id()
        self.login_url = 'chrome-extension://{}/login.html'.format(id_)

    def Kill_chromedriver(self):
        # mutex.acquire()
        c1 = self.commands_(cmd=['ps -aux |grep chromedriver | cut -c 10-14'])
        c2 = c1.strip().split('\n')
        for c3 in c2:
            c4 = self.commands__(cmd='sudo kill {}'.format(c3))
        
            

    def Config_chromedriver(self):
        c1 = self.commands__(cmd=['hash chromedriver'])
        if not c1:
            print('正在配置 chromedriver...')
            c1 = self.commands__(cmd='sudo ln -s {}Chromedriver/chromedriver_70.0.3538.67 /usr/bin/chromedriver'.format(self.root))
            c2 = self.commands__(cmd='sudo chmod +x /usr/bin/chromedriver')
            if c1 and c2:
                print('chromedriver 配置完成...')
        else:
            print('chromedriver 正在运行...')


    def Install_selenium(self):
        c1 = self.commands__(cmd='python3 -m pip install selenium')
        if c1:
            print('selenium 安装成功...')
        else:
            print('selenium 安装失败...')


    def Getting_plug_ins_id(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_extension('{}lib/Ghelper_1.4.6.crx'.format(self.root))
        # browser_driver = webdriver.Chrome()
        # browser_driver.get("https://www.baidu.com")
        # browser.get('http://ip138.com')
        data2 = self.Read_json()
        print('正在打开URL：chrome://extensions/')
        self.browser.get('chrome://extensions/')
        print('复制插件id...')
        print('点击详细信息后，即可查看id...')
        print('例子：chrome://extensions/?id=mcholjcecoiejoamfejfaadoefkcodok')
        print('如果已输入id则跳过此步骤,按回车即可跳过...')
        ipt1 = input('Id>')
        if ipt1:
            data1 = {'id':'{}'.format(ipt1)}
            self.Save_json(data=data1)
            print('Id保存成功...')

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


    def run(self,keyword):
        # mutex.release()
        # thread2 = threading.Thread(target=self.requests_,args=())
        # thread1 = threading.Thread(target=self.Config_chromedriver())
        # thread2 = threading.Thread(target=self.requests_())
        # thread1.start()
        # thread2.start()
        result1 = []
        self.Config_chromedriver()
        self.requests_(keyword)
        try:
            i = 0
            while True:
            # for i1 in range(2,12):
                print('第{}页'.format(i+1))    
                
                if i+1 < 27:
                    if i != 0:
                        # print('i+1 -> ',i+1)
                        time.sleep(2)
                        elements = self.browser.find_element_by_xpath('//*[@id="pnnext"]/span[2]')
                        time.sleep(1)
                        elements.click()
                        time.sleep(3)
                
                if i+1 == 27:
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
                        result1.append([elements1,elements2])
                
                    except Exception as e:
                        # print(traceback.format_exc())
                        pass
                
                print('下一页...')
                i += 1
            
            return result1
                
        except Exception as e:
            print(traceback.format_exc())
            pass








s = selenium_()
# s.Kill_chromedriver()
s.run()







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

