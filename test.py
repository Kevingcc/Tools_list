#coding:utf-8



from main import Libs
from main import Run
from search import selenium_
from main import Libs

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
        self.test()

    def test___(self):
        pass


t = test()

t.test_()


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

