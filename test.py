#!/usr/bin/env python3
#coding:utf-8



from main import Libs
from main import Run
from search import selenium_
from main import Libs
from search import Exploit_Search

# self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])


class test(selenium_):

    def __init__(self):
        super(test,self).__init__()
        self.Search = self.Google_Search
        self.Exploit_Search = Exploit_Search()
        self.sqli = self.Exploit_Search.Sqli_Exploit

    def test__(self):
        Searchs = self.Search('hello word')
        for Search in Searchs:
            Title = Search[0]
            Link = Search[1]
            print('Title -> ',Title)
            print('Link -> ',Link)

    def contents(self):
        pass

    def test_(self):
        self.test()
        self.browser.quit()
        self.browser_.quit()

    def test___(self):
        result1 = self.sqli()
        if result1:
            print('test___ 方法测试成功...')
            self.browser.quit()
            self.browser_.quit()




t = test()

# t.test_()
# t.test__()
t.test___()
# t.test___()

# r = Run()
# r.main()


# l = Libs()
# l.Write_Data(1,'sqli','sqli_','sqli__')
# l.Write_Data(2,2,'sqli','sqli_','sqli__')
# l.Delet_Data(2)
# Data = l.Query_Data('sqli')
# for Data_ in Data:
#     print(Data_)

# l.conn.close()

