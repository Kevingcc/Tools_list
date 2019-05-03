#coding:utf-8

import os
import sys
import subprocess
import traceback



class Libs(object):
    
    def __init__(self):
        self.config_pip_source()
        c1 = self.Inspect_pip()
        if c1:
            self.vle = True
        else:
            self.vle = False

    def commands(self,cmd):
        try:
            """
            这是一个命令解析方法.
            return <content or False>
            """
            c = subprocess.check_output(cmd,shell=True)
            return c
        except Exception as e:
            #处理不存的命令
            return False

    def commands_(self,cmd=[],decodes_='utf-8'):
        try:
            cc = []
            c = subprocess.check_output(cmd,shell=True)
            c = c.decode(decodes_).strip()
            cc.append(c)
            for value in cc:
                if value:
                    return value
                else:
                    return False
        except Exception as e:
            # print(traceback.format_exc())
            return False    
        
    def commands__(self,cmd='',decodes_='utf-8'):
        try:
            cc = []
            c = subprocess.call(cmd,shell=True)
            cc.append(c)
            for value in cc:
                if value:
                    return value
                else:
                    return False
        except Exception as e:
            # print(traceback.format_exc())
            return False   

    def config_pip_source(self):
        c1 = self.commands_(cmd=['echo $HOME'])
        if not os.path.exists(c1+'/.pip'):
            c2 = self.commands_(cmd=['mkdir $HOME/.pip'])
        else:
            print('.pip目录正常...')
            if not os.path.exists(c1+'/.pip/pip.conf'):
                cmd = ['sudo chmod +x lib/config_pip_source','lib/config_pip_source']
                c = self.commands_(cmd=cmd)
                if c:
                    print('pip 源配置完成...')
            else:
                print('pip.conf文件正常...')



    def Inspect_pip(self):
        c1 = self.commands('python3 -m pip')
        c2 = self.commands('python2 -m pip')
        if c1 and c2:
            print('pip3 pip2 运行正常...')
            return True
        else:
            print('pip3命令运行失败...')
            print('正在执行安装sudo apt-get install python3-pip')
            self.commands_('sudo apt-get install python3-pip')
            print('pip2命令运行失败...')
            print('正在执行安装sudo apt-get install python-pip')
            self.commands_('sudo apt-get install python-pip')
            return False
    
    def Install_subdns(self):
        if self.vle:
            c2 = self.commands_(cmd=['python3 subdns/subdns.py --help'])
            if not c2:
                print('subdns.py 没有安装依赖项...')
                print('subdns.py 正在安装依赖项...')
                c3 = self.commands_(cmd=['python3 -m pip install aiodns==2.0.0 colorlog==4.0.2'])
                if c3:
                    print('subdns.py 依赖项安装完成...')
                
                return False
            else:
                print('subdns.py 正在运行...')
                return True

    def Install_DiscoverTarget(self):
        if self.vle:
            c1 = self.commands_(cmd=['python2 DiscoverTarget/DiscoverTarget.py --help'])
            if not c1:
                print('DiscoverTarget.py 没有安装依赖项...')
                print('DiscoverTarget.py 正在安装依赖项...')
                c2 = self.commands_(cmd=['python2 -m pip install fofa==1.0.1 shodan==1.13.0 gevent==1.4.0 lxml==4.3.3 bs4==0.0.1'])
                if c2:
                    print('DiscoverTarget.py 依赖项安装完成...')
                
                return False
            else:
                print('DiscoverTarget.py 正在运行...')
                return True

    
        



            



class Run(Libs):
    
    def __init__(self,cmd=''):
        self.cmd = cmd
        super(Run,self).__init__()

    def Run_subdns(self):
        content = """
########
子域名爆破
########
1.查看帮助.
2.输入url.
3.自定义字典.
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
            print(content)
            c2 = input('>')
            if c2 is '1':
                c3 = self.commands__(cmd=['python3 subdns/subdns.py --help'])
                print(c3)
                print('')
                print("##############################################################################################")
                print(helps1)
                self.main()
            if c2 is '2':
                print(helps2)
                ipt1 = input('Url>')
                c3 = self.commands__(cmd=['python3 subdns/subdns.py -u {} -d mini_names.txt'.format(ipt1)])
                self.main()
            if c2 is '3':
                print('字典存放路径:$HOME/.Tools/Tools_list/dict')
                print('如果存放好了字典，请输入字典名字...')
                print(helps2)
                ipt1 = input('Url>')
                ipt2 = input('Dict>')
                c3 = self.commands__(cmd=['python3 subdns/subdns.py -u {} -d {}'.format(ipt1,ipt2)])
                self.main()
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
            print(content)
            ipt1 = input('>')
            if ipt1 is '1':
                print(helps1)
                c2 = self.commands_(cmd=['python2 DiscoverTarget/DiscoverTarget.py --help'])
                self.main()
            if ipt1 is '2':
                keywords = input('>')
                c2 = self.commands__(cmd=['python2 DiscoverTarget/DiscoverTarget.py -B {}'.format(keywords)])
                self.main()
            if ipt1 is '3':
                print('例子1：> -B hello word')
                print('例子2：> -Z app:"Apache-Tomcat"')
                c3 = input('> ')
                c4 = self.commands__(cmd='python2 DiscoverTarget/DiscoverTarget.py {}'.format(c3))
                self.main()
            if ipt1 is '0':
                self.main()

    def main(self):
        content1 = """
1.信息收集.
2.clear.
0.退出.
        """
        print(content1)
        ipt1 = input('>')
        if ipt1 is '1':
            content2 = """
1.子域名爆破.
2.URL采集.
0.返回菜单.
            """
            print(content2)
            ipt2 = input('>')
            if ipt2 is '1':
                self.Run_subdns()
            if ipt2 is '2':
                self.Run_DiscoverTarget()
            if ipt2 is '0':
                self.main()
        if ipt1 is '2':
            self.commands__(cmd='clear')
            self.main()
        if ipt1 is '0':
            exit(0)

    def test(self):
        # c = self.commands_(cmd=['ls'])
        # print(c)
        # self.Install_subdns()
        pass
        



r = Run()
# r.test()
r.main()

