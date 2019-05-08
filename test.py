#coding:utf-8



from main import Libs
from main import Run
from search import selenium_





class test(selenium_):

    def __init__(self):
        super(test,self).__init__()
        self.Search = self.run

    def test(self):
        Searchs = self.Search('hello word',3)
        for Search in Searchs:
            Title = Search[0]
            Link = Search[1]
            print('Title -> ',Title)
            print('Link -> ',Link)


t = test()

t.test()


