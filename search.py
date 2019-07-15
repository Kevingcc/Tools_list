#!/usr/bin/env python3
#coding:utf-8

from src.search import selenium_




if __name__ == "__main__":
    import sys
    try:
        if sys.argv[1] in ['-help','-h','--help','--h']:
            print('keyword and number.')
            exit(0)
    except:
        pass
    
    try:
        keyword = sys.argv[1]
        number = int(sys.argv[2])
        s = selenium_()
        s.Google_Search(keyword=keyword,number=number)
    except:
        pass

    


