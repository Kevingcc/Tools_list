#!/usr/bin/env python3
#coding:utf-8



logo = """
                                   
#######
#          ##     ####   #       ######
#         #  #   #    #  #       #
#####    #    #  #       #       #####
#        ######  #  ###  #       #
#        #    #  #    #  #       #
#######  #    #   ####   ######  ######

-----------------------------------------

@Author:Remix
@Date:2019-4-25


"""

# logo = '\033[1;33m' +'{}'.format(logo)+ '\033[0m'




import os
import sys
import traceback
from lib import AttribDict
from lib import info
from lib import error
from lib import warning
from lib import print_
from lib import input_
from lib import Libs
from lib import get_POC_T_script
from lib import _grep
from lib import red
from lib import green
from lib import _grep
from lib import grep

#helps
from lib import poc_t_helps
from lib import dirmap_helps
from lib import discovertarget_helps
from lib import subdns_helps
from lib import xsstrike_helps
from lib import dirbrute_helps
from lib import TideFinger_helps





class Run(Libs):
    
    def __init__(self,cmd=''):
        self.cmd = cmd
        super(Run,self).__init__()
        
    def TideFinger(self,**kwargs):
        helps = TideFinger_helps
        print_("""
######＃
指纹识别
######＃
[1].单个识别.
[2].批量识别.
[h].帮助.
[0].返回菜单.
        """)

        for args in kwargs:
            if args == 'url':
                url = kwargs['url']

        ipt1 = input_('>')
        if ipt1 is '1':
            pass
        if ipt1 is '2':
            pass
        if ipt1 is 'h':
            pass
        if ipt1 is '0':
            pass

    def POC_T(self):
        self.Install_POC_T()
        helps = poc_t_helps
        print_("""
######
POC_T
######
[1].批量POC验证.
[2].单个POC验证.
[h].帮助.
[0].返回菜单.
        """)
        f1,f2,f3 = get_POC_T_script()
        ipt1 = input_('>')
        if ipt1 is '1':
            pass
        if ipt1 is '2':
            ipt2 = input_('URL>')
            self.TideFinger(url=ipt2)
            ipt3 = input_('指纹名称>')
            f1,f2,f3 = get_POC_T_script()
            for sf1 in f1:
                with open('{}lib/script_name.txt'.format(self.root),'a+') as w:
                    w.write(sf1+'\n')
            search_r = _grep(keyword=ipt3,path='{}lib/script_name.txt'.format(self.root))
            print('')
            print('')
            red('----------------------------')
            print('')
            for s1 in search_r:
                line_number,line_content = s1
                print(line_content)
            green('----------------------------')
            ipt4 = input_('选择脚本>')
            
        if ipt1 is 'h':
            print_(helps)
        if ipt1 is '0':
            self.main()



    def Run_subdns(self):
        content = """
#########
子域名爆破
#########
1.查看帮助.
2.输入url.
3.自定义字典.
4.查看结果.
0.返回菜单.
        """
        helps1 = subdns_helps
        c1 = self.Install_subdns()
        helps2 = "例子：Url>baidu.com"
        if c1:
            print_(content)
            c2 = input_('>')
            if not c2:
                self.Run_subdns()
            if c2 is '1':
                # c3 = self.commands_(cmd=['python3 {}subdns/subdns.py --help'.format(self.root)])
                # jinhao = '#'*173
                # print_(jinhao)
                # print_(str(c3))
                # print_('')
                # print_(jinhao)
                print_(helps1)
                self.Run_subdns()
            if c2 is '2':
                print_(helps2)
                ipt1 = input_('Url>')
                c3 = self.commands__(cmd=['python3 {}subdns/subdns.py -u {} -d mini_names.txt'.format(self.root,ipt1)])
                self.Run_subdns()
            if c2 is '3':
                print_('字典存放路径:$HOME/.Tools/Tools_list/dict')
                print_('如果存放好了字典，请输入字典名字...')
                print_(helps2)
                ipt1 = input_('Url>')
                ipt2 = input_('Dict>')
                c3 = self.commands__(cmd=['python3 {}subdns/subdns.py -u {} -d {}'.format(self.root,ipt1,ipt2)])
                self.Run_subdns()
            if c2 is '4':
                self.sElect_Files_()
                self.Run_subdns()
            if c2 is '0':
                self.main()
    
    def Run_DiscoverTarget(self):
        content = """
#######
URL采集
#######
1.查看帮助.
2.输入关键字.
3.自定义命令.
4.查看结果.
0.返回菜单.
        """
        helps1 = discovertarget_helps
        c1 = self.Install_DiscoverTarget()
        if c1:
            print_(content)
            ipt1 = input_('>')
            if ipt1 is '1':
                print_(helps1)
                # c2 = self.commands__(cmd=['python2 {}DiscoverTarget/DiscoverTarget.py --help'.format(self.root)])
                self.Run_DiscoverTarget()
            if ipt1 is '2':
                keywords = input_('>')
                c2 = self.commands__(cmd=['sudo python2 {}DiscoverTarget/DiscoverTarget.py -B {}'.format(self.root,keywords)])
                self.Run_DiscoverTarget()
            if ipt1 is '3':
                print_('例子1：> -B hello word')
                print_('例子2：> -Z app:"Apache-Tomcat"')
                c3 = input_('> ')
                c4 = self.commands__(cmd='sudo python2 {}DiscoverTarget/DiscoverTarget.py {}'.format(self.root,c3))
                self.Run_DiscoverTarget()
            if ipt1 is '4':
                self.sElect_Files__()
                self.Run_DiscoverTarget()
            if ipt1 is '0':
                self.main()

    def Run_dirmap(self):
        content = """
###########
web目录扫描
###########
1.查看帮助.
2.输入URL.
3.尝试批量扫描，请输入文件名.
4.自定义命令.
5.查看结果.
0.返回菜单.
        """
        helps1 = dirmap_helps
        c1 = self.Install_dirmap()
        if c1:
            print_(content)
            ipt1 = input_('>')
            if not ipt1:
                self.Run_dirmap()
            if ipt1 is '1':
                print_(helps1)
                # c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py --help'.format(self.root))
                self.Run_dirmap()
            if ipt1 is '2':
                print_('例子：Url>https://www.baidu.com/')
                ipt2 = input_('Url>')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py -iU {} -t 30 -lcf --debug'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '3':
                print_('例子: Filename> DiscoverTarget/URL.txt')
                ipt2 = input_('Filename> ')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py -iF {} -t 30 -lcf --debug'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '4':
                print_('输入选项...')
                print_('例子1: > --help')
                print_('例子2: > --iN xxx')
                ipt2 = input_('> ')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py {}'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '5':
                pass
            if ipt1 is '0':
                self.main()
    
    def Run_xcdn(self):
        print_("""
1.输入url.
0.返回菜单.
        """)
        ipt1 = input_('>')
        if not ipt1:
            self.Run_xcdn()
        if ipt1 is '1':
            ipt2 = input_('Url>')
            c1 = self.commands__(cmd='python3 {}xcdn/xcdn.py {}'.format(self.root,ipt2))
            self.Run_xcdn()
        if ipt1 is '0':
            self.main()

    def Run_DirBrute(self):
        print_("""
###########
web目录扫描.
###########
1.查看帮助.
2.输入url.
0.返回菜单.
        """)
        helps1 = dirbrute_helps
        ipt1 = input_('>')
        if ipt1 is '1':
            print_(helps1)
            self.Run_DirBrute()
        if ipt1 is '2':
            dictnames = self.Get_Filename('{}DirBrute/dics/'.format(self.root))
            ipt2 = input_('Url>')
            print_('选择字典...')
            for dictname in dictnames:
                print_(dictname)
            ipt3 = input_('DictPath>')
            self.commands__(cmd='python2 {}DirBrute/dirbrute.py {} -e php -t 10 -d {}'.format(self.root,ipt2,'"'+ipt3+'"'))
            self.Run_DirBrute()
        if ipt1 is '0':
            self.main()
        
    def Run_xwaf(self):
        print_("""
1.查看帮助.
2.输入url.
3.输入url,post参数.
4.选择headerfile,输入参数,设置攻击向量level大小.
0.返回菜单.
        """)
        helps1 = """
1.python3 xwaf.py -u "http://www.baidu.com/1.php?id=1"
2.python3 xwaf.py -u "http://www.baidu.com/1.php" --data="postdata" -p xxx
3.python3 xwaf.py -r /tmp/headerfile -p xxx --level 5
        """
        ipt1 = input_('>')
        if not ipt1:
            self.Run_xwaf()
        if ipt1 is '1':
            print_(helps1)
            self.Run_xwaf()
        if ipt1 is '2':
            ipt2 = input_('Url>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -u "{}"'.format(self.root,ipt2))
            self.Run_xwaf()
        if ipt1 is '3':
            ipt2 = input_('Url>')
            ipt3 = input_('Data>')
            ipt4 = input_('Post parameter>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -u "{}" --data="{}" -p {}'.format(self.root,ipt2,ipt3,ipt4))
            self.Run_xwaf()
        if ipt1 is '4':
            ipt2 = input_('1>')
            ipt3 = input_('2>')
            ipt4 = input_('3>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -r {} -p {} --level {}'.format(self.root,ipt2,ipt3,ipt4))
            self.Run_xwaf()
        if ipt1 is '0':
            self.main()

    def Run_fsociety(self):
        print_("""
1.Run Fsociety
0.返回菜单.
        """)
        c1 = self.Install_fsociety()
        if c1:
            ipt1 = input_('>')
            if ipt1 is '1':
                self.commands__(cmd='fsociety')
                self.Run_fsociety()
            if ipt1 is '0':
                self.main()


    def xsstrike(self):
        self.Install_xSStrike()
        help1 = xsstrike_helps
        print_("""
#########
XSStrike
#########
[1].扫描单个目标(GET).
[2].扫描单个目标(POST).
[3].扫描多个目标.
[4].测试URL路径组件.
[5].将POST数据视为JSON.
[6].爬行.
[7].自定义命令.
[h].帮助.
[0].返回菜单.
        """)
        ipt1 = input_('>')
        if not ipt1:
            self.xsstrike()
        if ipt1 is '1':
            ipt2 = input_('URL>')
            c1 = self.commands__(cmd='{}XSStrike/xsstrike.py -u \"{}\"'.format(self.root,ipt2))
            self.xsstrike()

        if ipt1 is '2':
            ipt2 = input_('URL>')
            ipt3 = input_('data>')
            c1 = self.commands__(cmd='{}XSStrike/xsstrike.py -u \"{}\" --data \"{}\"'.format(self.root,ipt2,ipt3))
            self.xsstrike()    

        if ipt1 is '3':
            ipt2 = input_('FilenamePath>')
            c1 = self.commands__(cmd='{}/XSStrike/xsstrike.py --seeds {}'.format(self.root,ipt2))
            self.xsstrike()

        if ipt1 is '4':
            ipt2 = input_('Payload>')
            ipt3 = input_('Url>')
            c1 = self.commands__(cmd='{}/XSStrike/xsstrike.py -u "{}{}" --path'.format(self.root,ipt3,ipt2))
            self.xsstrike()
        
        if ipt1 is '5':
            pass

        if ipt1 is '6':
            pass

        if ipt1 is '7':
            print_(help1)
            ipt2 = input_('>')
            c1 = self.commands__(cmd='{}/XSStrike/xsstrike.py {}'.format(self.root,ipt2))
            self.xsstrike()

        if ipt1 is 'h':
            print_(help1)
            self.xsstrike()

        if ipt1 is '0':
            self.main()




    def main(self):
        content1 = """
{}


[1].信息收集.
[2].Web程序.
[3].黑盒测试工具包.
[4].Linux 工具.
[5].漏洞验证(POC).
[6].漏洞测试(FUZZ).
[c].Clear.
[0].退出.
        """.format(logo)
        print_(content1)
        ipt1 = input_('>')
        if not ipt1:
            self.main()
        if ipt1 is '1':
            content2 = """
########
信息收集
########
1.子域名爆破.
2.URL采集.
3.Web目录扫描.
4.尝试找出cdn背后的真实ip.
0.返回菜单.
            """
            print_(content2)
            ipt2 = input_('>')
            if not ipt2:
                self.main()
            if ipt2 is '1':
                self.Run_subdns()
            if ipt2 is '2':
                self.Run_DiscoverTarget()
            if ipt2 is '3':
                print_("""
#######
选择工具
#######
1.dirmap.
2.DirBrute.
0.返回菜单.
                """)
                ipt3 = input_('>')
                if not ipt3:
                    self.main()
                if ipt3 is '1':
                    self.Run_dirmap()
                if ipt3 is '2':
                    self.Run_DirBrute()
                if ipt3 is '0':
                    self.main()
            if ipt2 is '4':
                self.Run_xcdn()
            if ipt2 is '0':
                self.main()
        
        if ipt1 is '2':
            print_("""
########
web程序
#######
1.xwaf waf自动化绕过工具.
0.返回菜单.
            """)
            ipt2 = input_('>')
            if ipt2 is '1':
                self.Run_xwaf()
            if ipt2 is '0':
                self.main()
        if ipt1 is '3':
            print_("""
1.Fsociety.
0.返回菜单.
            """)
            ipt2 = input_('>')
            if not ipt2:
                self.main()
            if ipt2 is '1':
                self.Run_fsociety()
            if ipt2 is '0':
                self.main()
        
        if ipt1 is '4':
            print_("""
##########
linux 工具
##########
    [1].输出艺术字.
    [2].获取工具的绝对路径.
    [0].返回菜单.
            """)
            ipt2 = input_('>')
            if ipt2 is '1':
                ipt3 = input_('内容>')
                self.commands__(cmd='figlet {}'.format(ipt3))
                self.commands__(cmd='toilet {}'.format(ipt3))
                self.main()
            if ipt2 is '2':
                ipt3 = input_('Tool name>')
                c1 = self.commands_(cmd='whereis {}'.format(ipt3))
                c2 = self.commands_(cmd='which {}'.format(ipt3))
                data1 = grep(ipt3,c1)
                data2 = grep(ipt3,c2)
                print(data1)
                print(data2)
            
            if ipt2 is '0':
                self.main()
        
        if ipt1 is '5':
            print_("""
############
漏洞验证(POC)
############
1.Xss
2.Sqli
3.Csrf
0.返回菜单
            """)
            ipt2 = input_('>')
            if ipt2 is '0':
                self.main()
            

        if ipt1 is '6':
            print_("""
#############
漏洞测试(FUZZ)
#############
1.Xss
2.Sqli
3.Csrf
0.返回菜单
            """)
            ipt2 = input_('>')
            if ipt2 is '1':
                print_("""
####
Xss
####
1.XSStrike.
0.返回菜单.
                """)
                ipt3 = input_('>')
                if ipt3 is '1':
                    self.xsstrike()
                    self.main()
                if ipt3 is '0':
                    self.main()
            
            if ipt2 is '0':
                self.main()


        if ipt1 is 'c':
            self.commands__(cmd='clear')
            self.main()

        if ipt1 is '0':
            c1 = self.commands_(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])
            print_(c1)
            exit(0)

    def test(self):
        # c = self.commands_(cmd=['ls'])
        # print_(c)
        # self.Install_subdns()
        pass
        


# print_(logo)
# print_('')
# r = Run()
# r.test()
# r.Install_dirmap()
# r.Select_Files__()
# r.Run_dirmap()
# r.main()








if __name__ == '__main__':
    r = Run()
    r.main()
    











































































































































































































