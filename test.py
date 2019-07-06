#!/usr/bin/env python3
#coding:utf-8



from src.scann import *
from src.search import selenium_

selenium_ = selenium_()
browser = selenium_.browser
browser_ = selenium_.browser_


if __name__ == "__main__":
    browser.minimize_window()
    browser_.minimize_window()
    main()
    # queue = Queue()
    # s = Scann(queue=queue,domain='')
    # s.Subdomain_Enumeration(domain='')
    browser.quit()
    browser_.quit()
    browser.quit()

# self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])









# t = test()
# t.test_()
# t.test__()
# t.test___()
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





# from src.note_search import search


# s1 = search()
# search = s1.search
# search('x')