#coding:utf-8



from main import Libs
from main import Run
from search import selenium_
from main import Run

# self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])


class test(selenium_):

    def __init__(self):
        super(test,self).__init__()
        self.Search = self.Google_Search

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
        data = self.test()
        print(data)


t = test()

t.test_()


# r = Run()
# r.main()
