#!/usr/bin/env python3
#coding:utf-8
from lib import _commands
from lib import Libs
from lib import root
from lib import AttribDict
from lib import red
from lib import blue
from lib import green
from lib import _red
import threading

libs = Libs()
foo = AttribDict()
commands_ = libs.commands_
commands__ = libs.commands__

class search(object):

    def __init__(self):
        pass

    def pdf_search(self,keyword):
        try:
            c1 = _commands(1)
            result = commands_(cmd='pdfgrep "{}" -r -n {}note/*'.format(keyword,root))
            foo.result1 = result
        except Exception as e:
            pass

    def text_search(self,keyword):
        try:
            c1 = _commands(1)
            result = commands_(cmd='grep "{}" -r -n {}note/*'.format(keyword,root))
            foo.result2 = result
        except Exception as e:
            pass

    def search(self,keyword):
        """
        search
        """

        thread1 = threading.Thread(target=self.pdf_search,args=(keyword,))
        thread2 = threading.Thread(target=self.text_search,args=(keyword,))
        thread1.start()
        thread2.start()
        try:
            # pdf search result.
            pdf_result1 = foo.result1
            for n1 in pdf_result1:
                if n1 == keyword:
                    n2 = n1 + _red(n1)
            # text search result.
            text_result2 = foo.result2
            for n1 in pdf_result1:
                if n1 == keyword:
                    n2 = n1 + _red(n1)
                    
        except Exception as e:
            pass
        



