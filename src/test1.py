#!/usr/bin/env python3
#coding:utf-8



"""
这是一个python脚本特征识别工具，通过枚举的特征判断此脚本是基于python2 或 python3.
"""





import asyncio
import time

"""
特征
"""
t1 = '!/usr/bin/env python3'
t2 = '!/usr/bin/python3'
t3 = 'python3'

t4 = '!/usr/bin/env python2'
t5 = '!/usr/bin/python2'
t6 = 'python2'


semaphore = asyncio.Semaphore(8000)
loop = asyncio.get_event_loop()





async def Distinguish(sem,num,times):
    async with sem:
        if int(times) < 5:
            times = int(times) + 2
        else:
            times = int(times) - 2

        t = int(times)
        time.sleep(int(t))
        print('我是:'+str(num))




def run():
    for num in range(10):
        task = asyncio.ensure_future(Distinguish(sem=semaphore,num=num,times=num))
        loop.run_until_complete(task)

run()
