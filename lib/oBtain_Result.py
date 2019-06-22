#!/usr/bin/env python3
#coding:utf-8


from .__init__ import get_filename
from .__init__ import root




# Obtain Result
def oBitain_Result_sub():
    datas = []
    domain_ = ''
    ip = ''
    filename = get_filename('{}output/'.format(root))
    for name in filename:
        with open(name,'r') as r:
            for line in r.readlines():
                l1 = line.split('[')
                domain_ = l1[0].strip()
                ip = eval('['+l1[1].strip())
                datas.append([domain_,ip])
    
    
    return datas


