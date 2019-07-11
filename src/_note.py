from lib import print_
from lib import input_
from note._class.dict.dict1 import dict1

def note():
    print_("""
    笔记:
        1.dict:
    """)

    ipt1 = input_('>')
    if ipt1 is '1':
        print_("""
    1.dict1.md
        """)
        ipt2 = input_('>')
        if ipt2 is '1':
            d = dict1()
            d.content()

