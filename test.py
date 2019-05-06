#coding:utf-8


import re
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from main import Libs


mutex = threading.Lock()

# python3 -m pip install selenium

class selenium_(Libs):
    def __init__(self):
        super(selenium_,self).__init__()

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

    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        # driver.close()

    def test1(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_extension('{}lib/Ghelper_1.4.6.crx'.format(self.root))
        # browser_driver = webdriver.Chrome()
        # browser_driver.get("https://www.baidu.com")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--load-extension={}lib/ghelper'.format(self.root))
        browser = webdriver.Chrome(
            chrome_options=chrome_options
        )
        browser.get('http://ip138.com')
        browser.get('chrome://extensions/')

        # ActionChains(browser).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
            

        
        # driver.close()

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
# s.test1()







"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--load-extension=SwitchyOmega')
 
browser = webdriver.Chrome(
    executable_path="./drivers/chromedriver.exe",
    chrome_options=chrome_options
)
browser.get('http://ip138.com')
"""



from main import Run

Run.main()




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

