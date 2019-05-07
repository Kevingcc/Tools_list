#coding:utf-8


import re
import threading
import json
import time
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
        mutex.acquire()
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
        i = 0
        for data3 in data2:
            if i == 0:
                if not data3:
                    print('正在打开URL：chrome://extensions/')
                    self.browser.get('chrome://extensions/')
                    print('复制插件id...')
                    print('点击详细信息后，即可查看id.')
                    print('例子：chrome://extensions/?id=mcholjcecoiejoamfejfaadoefkcodok')
                    ipt1 = input('Id>')
                    data1 = {'id':'{}'.format(ipt1)}
                    self.Save_json(data=data1)
                    break
                else:
                    data3 = json.loads(data3)
                    print('插件id：{}'.format(data3['id']))
                    return data3['id']
                
            i += 1

    def extract_cookie(self):
        self.browser.get(self.login_url)
        denglu = self.browser.find_element_by_xpath('//*[@id="submit"]')
        action = ActionChains(self.browser)
        denglu.click()
        curpage_url = self.browser.current_url 
        data2 = self.Read_json(filename='login.json')
        i = 0
        for line in data2:
            if not line.strip():
                email = input('Email>')
                password = input('Password>')
                data1 = {'email':email,'password':password}
                self.Save_json(data=data1,filename='login.json')
            else:
                print('插件登入成功...')
            i += 1
        data3 = self.Read_json(filename='login.json')
        i = 0
        for line in data3:
            if i == 0:
                email = json.loads(line['email'])
                password = json.loads(line['password'])
                log_email = self.browser.find_element_by_id('email')
                log_password = self.browser.find_element_by_id('password')
                log_email.clear()
                log_email.send_keys(email)
                time.sleep(3)
                log_password.clear()
                log_password.send_keys(password)
                login_in_xpath = '//*[@id="submit"]'
                login_in = self.browser.find_element_by_xpath(login_in_xpath)
                login_in.click()
                
            i += 1





        # i = input('>')

        
        


    def run(self):
        thread2 = threading.Thread(target=self.Config_chromedriver())
        # thread3 = threading.Thread(target=self.test)
        thread1 = threading.Thread(target=self.Kill_chromedriver())
        thread2.start()
        # thread3.start()
        mutex.release()
        thread1.start()





s = selenium_()
# s.Kill_chromedriver()
s.extract_cookie()







"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--load-extension=SwitchyOmega')
 
browser = webdriver.Chrome(
    executable_path="./drivers/chromedriver.exe",
    chrome_options=chrome_options
)
browser.get('http://ip138.com')
"""







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

