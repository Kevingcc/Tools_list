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

from lib.setting import option_install
import os

if option_install:
    os.system('python3 -m pip install colorlog==4.0.2')







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





class Run(Libs):
    
    def __init__(self,cmd=''):
        self.cmd = cmd
        super(Run,self).__init__()
        


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
        helps1 = """
使用: subdns.py [-h] [-v] [-d 字典] [-u 域名] [-s 深度] [-n 字典]

to use get subnames of dns

optional arguments:
  -h, --help            显示此帮助消息并退出
  -v, --version         显示程序的版本号并退出
  -d DICT, --dict DICT  指定词典
  -u DOMAIN, --domain 领域
                        指定域名
  -s DEEP, --deep DEEP  深度 域名
  -n NEXT, --next NEXT  指定词典
        """
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
        helps1 = """
Usage: 
      _____  _                          _______                   _   
     |  __ \(_)                        |__   __|                 | |  
     | |  | |_ ___  ___ _____   _____ _ __| | __ _ _ __ __ _  ___| |_ 
     | |  | | / __|/ __/ _ \ \ / / _ \ '__| |/ _` | '__/ _` |/ _ \ __|
     | |__| | \__ \ (_| (_) \ V /  __/ |  | | (_| | | | (_| |  __/ |_ 
     |_____/|_|___/\___\___/ \_/ \___|_|  |_|\__,_|_|  \__, |\___|\__|
                                                        __/ |         
                                                       |___/         
                                        Coded By Coco413 (v1.0 RELEASE) 
    

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -S SHODAN, --shodan=SHODAN
                        使用shodan空间搜索引擎
  -F FOFA, --fofa=FOFA  FOFA空间搜索引擎
  -Z ZOOMEYE, --zoomeye=ZOOMEYE
                        使用ZOOMEYE空间搜索引擎
  -C CENSYS, --censys=CENSYS
                        使用censys空间搜索引擎
  -B B3G, --b3g=B3G     传统搜索引擎使用百度360谷歌

例子: python DiscoverTarget.py -S Apache-Tomcat -F app="Apache-Tomcat" -Z
app:"Apache-Tomcat" -C Apache-Tomcat -B Powered by Discuz

"""
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
        helps1 = """
                     #####  # #####  #    #   ##   #####
                     #    # # #    # ##  ##  #  #  #    #
                     #    # # #    # # ## # #    # #    #
                     #    # # #####  #    # ###### #####
                     #    # # #   #  #    # #    # #
                     #####  # #    # #    # #    # #   v1.0

使用: python3 dirmap.py -iU https://target.com -lcf

可选参数:
  -h, --help            show this help message and exit

引擎:
  引擎配置

  -t THREAD_NUM, --thread THREAD_NUM
                        线程数, default 30

目标:
  Target config

  -iU TARGET            扫描单个目标 (e.g. http://target.com)
  -iF FILE              从目标文件加载目标 (e.g. urls.txt)
  -iR START-END         从int（开始）到int（结束）的数组 (e.g.
                        192.168.1.1-192.168.2.100)
  -iN IP/MASK           通过IP/掩码生成IP. (e.g. 192.168.1.0/24)

Bruter:
  Bruter config

  -lcf, --加载配置文件
                        通过配置文件加载配置
  --debug               打印有效载荷并退出

        """
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
        helps1 = """
用法: dirbrute.py target [options] 
例子: python dirbrute.py www.cdxy.me -e php -t 10
         python dirbrute.py www.cdxy.me -t 10 -d ./dics/ASP/uniq

选项:
  -h, --help            show this help message and exit
  -e EXT, --ext=EXT     选择扩展名: php asp aspx jsp...
  -t THREADS_NUM, --threads=线程数
                        线程数. default = 10
  -d DIC_PATH, --dic=字典路径.
                        默认字典: ./dics/dirs.txt

        """
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
        help1 = """
	XSStrike v3.1.4

usage: xsstrike.py [-h] [-u TARGET] [--data PARAMDATA] [-e ENCODE] [--fuzzer]
                   [--update] [--timeout TIMEOUT] [--proxy] [--params]
                   [--crawl] [--json] [--path] [--seeds ARGS_SEEDS]
                   [-f ARGS_FILE] [-l LEVEL] [--headers [ADD_HEADERS]]
                   [-t THREADCOUNT] [-d DELAY] [--skip] [--skip-dom] [--blind]
                   [--console-log-level {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR}]
                   [--file-log-level {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR}]
                   [--log-file LOG_FILE]

optional arguments -- 可选参数:
  -h, --help            show this help message and exit
  -u TARGET, --url TARGET url -- 目标
  --data PARAMDATA      post data -- 发布数据
  -e ENCODE, --encode ENCODE encode payloads -- 编码有效载荷
  --fuzzer              fuzzer -- 模糊测试
  --update              update -- 更新
  --timeout TIMEOUT     timeout -- 超时
  --proxy               use prox(y|ies) -- 代理
  --params              find params -- 查找参数
  --crawl               crawl -- 爬行
  --json                treat post data as json -- 将Post数据视为JSON
  --path                inject payloads in the path -- 在路径中注入有效载荷
  --seeds ARGS_SEEDS    load crawling seeds from a file -- 从文件加载爬行种子
  -f ARGS_FILE, --file ARGS_FILE load payloads from a file -- args_file 从文件加载有效负载
  -l LEVEL, --level LEVEL level of crawling -- 爬行等级
  --headers [ADD_HEADERS] add headers -- 添加报头
  -t THREADCOUNT, --threads THREADCOUNT number of threads -- 线程数
  -d DELAY, --delay DELAY delay between requests -- 请求之间的延迟
  --skip                don't ask to continue -- 不要求继续
  --skip-dom            skip dom checking -- 跳过DOM检查
  --blind               inject blind XSS payload while crawling -- 爬行时注入盲XSS负载
  --console-log-level {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR} Console logging level -- {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR} 控制台日志记录级别
  --file-log-level {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR} File logging level -- {INFO,VULN,GOOD,CRITICAL,RUN,DEBUG,WARNING,ERROR} 文件记录级别
  --log-file LOG_FILE   Name of the file to log -- 日志文件的名称


        """
        print_("""
#########
XSStrike
#########
[1].扫描单个目标.
[2].扫描多个目标.
[h].帮助.
[0].返回菜单.
        """)
        ipt1 = input_('>')
        if ipt1 is '1':
            pass

        if ipt1 is '2':
            pass

        if ipt1 is 'h':
            print_(help1)

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
    [0].返回菜单.
            """)
            ipt2 = input_('>')
            if ipt2 is '1':
                ipt3 = input_('内容>')
                self.commands__(cmd='figlet {}'.format(ipt3))
                self.commands__(cmd='toilet {}'.format(ipt3))
                self.main()
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
    











































































































































































































