#!/usr/bin/env python3
#coding:utf-8

from lib import get_filename
from lib import root
from lib import print_
from lib import red
from lib import input_
from lib import info
from lib import warning
from lib import error
from lib import Libs
from lib import AttribDict
from lib import regular
from lib import green
from lib import blue
from lib import _red

from threading import Thread
import time
import re
try:
    import queue
except:
    import Queue



q = queue.Queue()

libs = Libs()
commands_ = libs.commands_
commands__ = libs.commands__
cmd2 = "sudo nmap -Pn \"{}\" -oX \"{}lib/nmap_xml/{}\""
foo = AttribDict()





def port_scan(ip,filename):
    """
    nmap scann
    """
    try:
        green(f'Run cmd -> {cmd2.format(ip,libs.root,filename)}')
        libs.commands_(cmd=[cmd2.format(ip,libs.root,filename)])
        time.sleep(10)
        data1 = libs.commands_(cmd=['sudo python2 {}lib/nmap_xml.py {}lib/nmap_xml/{}'.format(libs.root,libs.root,filename)]).strip()
        # data1 = exec('data1 = '+data1)
        data1 = eval(data1)
        foo.nScan_Result = data1
        for i in range(0,2):
            for d1 in foo.nScan_Result[i]:
                if 'ip' in d1 and \
                    'port' in d1 and \
                    'state' in d1 and \
                    'agreement' in d1:
                    
                    ip = d1.get('ip')
                    port = d1.get('port')
                    state = d1.get('state')
                    agreement = d1.get('agreement')
        
                    if ip:
                        print('')
                        if state != 'closed' and state != 'filtered':
                            info(ip+':'+port+' /'+state+' '+'-'+agreement)
                            if port == '443' or port == '80':
                                w = open('{}lib/Nmap_Result/nScan_Result.txt'.format(libs.root),'a+')
                                w.write('{"ip":"%s","port":"%s","state":"%s","agreement":"%s"}' % (ip,port,state,agreement))
                                w.write('\n')
                                warning('写入 lib/batch/nScan_Result.txt ...')
                                w.close()
                    
                        else:
                            if state == 'closed':
                                error(ip+':'+port+' /'+state+' '+'-'+agreement)
                            elif state == 'filtered':
                                warning(ip+':'+port+' /'+state+' '+'-'+agreement)
                    
        
    except Exception as e:
        # error(traceback.format_exc())
        pass












def ip_or_domain_result_handle():
    from main import Run
    r1 = Run()
    main = r1.main

    print_("""
########
处理结果
########
1.查看结果.
2.结果提交到nmap扫描. 
0.返回菜单.
    """)

    ipt1 = input_('>')

    if ipt1 is '0':
        main()

    if ipt1 is '1':
        filenames = get_filename(path=f'{root}lib/fping')
        
        if not filenames:
            red('[Error] fping 没有结果.')
            return False

        i = 1
        for filename in filenames:
            print_(str(i)+'. '+filename)
            i += 1
        
        ipt1 = input_('>')

        i = 1
        for filename in filenames:
            if str(i) == ipt1:
                ipt1 = str(filename.replace(' ','').replace('\n',''))
                break
            i += 1

        with open(f'{ipt1}','r') as r:
            for line in r.readlines():
                if re.findall(f'({regular(1)})(\.+)*',line):
                    ip = str(line.strip().replace(' ','').replace('\n',''))
                    if ip:
                        data = _red(ip)
                        print(data)

    if ipt1 is '2':
        filenames = get_filename(path=f'{root}lib/fping')
        
        if not filenames:
            red('[Error] fping 没有结果.')
            return False

        i = 1
        for filename in filenames:
            print_(str(i)+'. '+filename)
            i += 1
        
        ipt1 = input_('>')

        i = 1
        for filename in filenames:
            if str(i) == ipt1:
                ipt1 = str(filename.replace(' ','').replace('\n',''))
                break
            i += 1

        with open(f'{ipt1}','r') as r:
            for line in r.readlines():
                if re.findall(f'({regular(1)})(\.+)*',line):
                    ip = str(line.strip().replace(' ','').replace('\n',''))
                    if ip:
                        thread1 = Thread(target=port_scan,args=(ip,ip))
                        thread1.start()
        
     
        

        
    
            


