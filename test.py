#coding:utf-8



from main import Libs
from main import Run
from search import selenium_


# self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])


class test(selenium_):

    def __init__(self):
        super(test,self).__init__()
        self.Search = self.Google_Search

    def test(self):
        Searchs = self.Search('hello word')
        for Search in Searchs:
            Title = Search[0]
            Link = Search[1]
            print('Title -> ',Title)
            print('Link -> ',Link)

    def contents(self):
        pass


t = test()

t.test()


