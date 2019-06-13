#!/usr/bin/env python3
#coding:utf-8



import requests
from main import Libs
from lib import info
from lib import warning
from lib import error
from lib import print_
from lib import root
from search import selenium_
from os import system



selenium_ = selenium_()
# browser = selenium_.browser
# browser_ = selenium_.browser_
google_search = selenium_.Google_Search



class spider(object):

    def __init__(self):
        self.root = root 

    def main(self,keyword):
        results = google_search(keyword=keyword,number=2)
        i = 0
        system('mkdir {}lib/doc_image/pyautogui'.format(self.root))
        for result in results:
            # title = result[0]
            link = result[1]
            html_doc = requests.get(link).text
            with open('{}lib/doc_image/pyautogui/{}'.format(self.root,'pyautogui{}.html'.format(str(i))),'a+') as w:
                w.write(html_doc)
            i += 1


    def run(self):
        self.main(keyword='site:pyautogui.readthedocs.io')








if __name__ == '__main__':
    s = spider()
    s.run()



















