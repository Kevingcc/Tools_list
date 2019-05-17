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

logo = '\033[1;33m' +'{}'.format(logo)+ '\033[0m'


import os
import sys
import subprocess
import traceback
import re
import json
import sqlite3
import requests
from lib.datatype import AttribDict

# 获取当前文件绝对路径.
# os.getcwd()

# python 设置环境变量
# print(os.path.dirname(os.path.abspath(__file__))+'/test')
# sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/test')

# pyc文件清理
# find ./ -name "*.pyc" | xargs rm -rf

class Libs(object):
    
    def __init__(self):
        self.root_ = self.commands_(cmd=['echo $HOME'])
        self.root = '{}/.Tools/Tools_list/'.format(self.root_)
        self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])
        self.config_pip_source()
        c1 = self.Inspect_pip()
        if c1:
            self.vle = True
        else:
            self.vle = False
        self.Install_selenium()
        self.Install_requests()
        # self.Install_mechanize()
        self.Config_chromedriver()
        
        self.conn = sqlite3.connect('{}lib/GHack'.format(self.root))
        self.c = self.conn.cursor()



    def Query_Data(self,type_):
        """
        查询数据.
        data[0] = id
        页数
        data[1] = page
        漏洞类型
        data[2] = type
        标题
        data[3] = title
        内容
        data[4] = content
        """
        data = []
        cursor = self.c.execute(r"""SELECT id,page,type,title,content FROM "Exploit" WHERE "type" LIKE '{}'""".format(type_))
        for row in cursor:
            id_ = row[0]
            page = row[1]
            type_ = row[2]
            title = row[3]
            content = row[4]
            data.append([id_,page,type_,title,content])
            
        return data

        # print('查询成功...')


    def Write_Data(self,id_,page,type_,title,content):
        """
        写入数据.
        """
        try:
            expression = r"""INSERT INTO "Exploit" ("id","page","type","title","content") VALUES ('{}','{}','{}','{}','{}')""".format(id_,page,type_,title,content)
            # print(expression)
            self.c.execute(expression)
            # print('写入数据成功...')
            self.conn.commit()
            return True
        except Exception as e:
            self.Delet_Data(id_=id_)
            return False


    def Delet_Data(self,id_):
        """
        删除数据.
        """
        try:
            # DELETE FROM "Exploit" WHERE ("rowid" = 2)
            self.c.execute(r"""DELETE FROM "Exploit" WHERE ("id" = {})""".format(id_))
            self.conn.commit()
            return True
        except Exception as e:
            pass


    def Save_json(self,data={},filename='id.json'):
        with open('{}lib/{}'.format(self.root,filename),'a+') as w:
            json.dump(data,w)
            w.write('\n')
            print('保存文件完成...')

    def Read_json(self,filename='id.json'):
        lines = []
        with open('{}lib/{}'.format(self.root,filename),'r') as r:
            for line in r.readlines():
                lines.append(line.strip())
        return lines


    def Save_text(self,filename,content):
        try:
            with open('{}lib/{}'.format(self.root,filename),'a+') as w:
                if 'https' not in content or 'http' not in content:
                    content1 = 'http://'+content.strip()
                    content2 = 'https://'+content.strip()
                    r1 = requests.get(content1).status_code
                    r2 = requests.get(content2).status_code
                    if r1 == 200:
                        content = content1
                    elif r2 == 200:
                        content = content2

                w.write(content.strip()+'\n')
        except Exception as e:
            # print(traceback.format_exc())
            pass
            

    def Read_text(self,filename):
        lines = []
        with open('{}lib/{}'.format(self.root,filename),'r') as r:
            for line in r.readlines():
                lines.append(line.strip())
        return lines


    def commands_(self,cmd=[],decodes_='utf-8'):
        """
            这是一个命令行解析方法.
            return <content or False>
        """
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
        """
            这是一个命令解析方法.
            return <True or False>
        """
        try:
            c = subprocess.call(cmd,shell=True)
            if int(c) == 0:
                return True
            else:
                return False
        except Exception as e:
            # print(traceback.format_exc())
            return False   

    def config_pip_source(self):
        c1 = self.commands_(cmd=['echo $HOME'])
        if not os.path.exists(c1+'/.pip'):
            c2 = self.commands__(cmd='mkdir $HOME/.pip')
            cmd = 'sudo chmod +x {}lib/config_pip_source && bash {}lib/config_pip_source'.format(self.root,self.root)
            c = self.commands__(cmd=cmd)
            if c:
                print('pip 源配置完成...')
            else:
                print('pip.conf文件正常...')

    
    def Config_chromedriver(self):
        c1 = self.commands__(cmd=['hash chromedriver'])
        if not c1:
            print('正在配置 chromedriver...')
            c1 = self.commands__(cmd='sudo ln -s {}Chromedriver/chromedriver_70.0.3538.67 /usr/bin/chromedriver'.format(self.root))
            c2 = self.commands__(cmd='sudo chmod +x /usr/bin/chromedriver')
            if c1 and c2:
                print('chromedriver 配置完成...')
        else:
            print('chromedriver 正在运行...')

    # def Install_mechanize(self):
    #     c1 = self.commands__(cmd='python3 -m pip install mechanize==0.4.2')
    #     if c1:
    #         print('mechanize 安装成功...')
    #     else:
    #         print('mechanize 安装失败...')

    def Inspect_pip(self):
        c1 = self.commands_('python3 -m pip')
        c2 = self.commands_('python2 -m pip')
        if c1 and c2:
            print('pip3 pip2 运行正常...')
            return True
        else:
            print('pip3命令运行失败...')
            print('正在执行安装sudo apt-get install python3-pip')
            self.commands__('sudo apt-get -y install python3-pip')
            print('pip2命令运行失败...')
            print('正在执行安装sudo apt-get install python-pip')
            self.commands__('sudo apt-get -y install python-pip')
            return False

    def Install_requests(self):
        c1 = self.commands__(cmd='python3 -m pip install requests==2.21.0')
        if c1:
            print('requests 安装成功...')
        else:
            print('requests 安装失败...')
    
    def Install_selenium(self):
        c1 = self.commands__(cmd='python3 -m pip install selenium==3.141.0')
        if c1:
            print('selenium 安装成功...')
        else:
            print('selenium 安装失败...')

    def Install_subdns(self):
        if self.vle:
            c2 = self.commands_(cmd=['python3 {}subdns/subdns.py --help'.format(self.root)])
            if not c2:
                print('subdns.py 没有安装依赖项...')
                print('subdns.py 正在安装依赖项...')
                c3 = self.commands__(cmd=['python3 -m pip install aiodns==2.0.0 colorlog==4.0.2'])
                if c3:
                    print('subdns.py 依赖项安装完成...')
                
                return False
            else:
                print('subdns.py 正在运行...')
                return True

    def Install_DiscoverTarget(self):
        if self.vle:
            c1 = self.commands_(cmd=['python2 {}DiscoverTarget/DiscoverTarget.py --help'.format(self.root)])
            if not c1:
                print('DiscoverTarget.py 没有安装依赖项...')
                print('DiscoverTarget.py 正在安装依赖项...')
                c2 = self.commands__(cmd=['python2 -m pip install fofa==1.0.1 shodan==1.13.0 gevent==1.4.0 lxml==4.3.3 bs4==0.0.1'])
                if c2:
                    print('DiscoverTarget.py 依赖项安装完成...')
                
                return False
            else:
                print('DiscoverTarget.py 正在运行...')
                return True

    def Install_dirmap(self):
        if self.vle:
            c1 = self.commands_(cmd=['python3 {}dirmap/dirmap.py --help'.format(self.root)])
            if not c1:
                print('dirmap.py 没有安装依赖项...')
                print('dirmap.py 正在安装依赖项...')
                c2 = self.commands__(cmd=['python3 -m pip install -r dirmap/requirement2.txt'])
                if c2:
                    print('dirmap.py 依赖项安装完成...')
                
                return False
            else:
                print('dirmap.py 正在运行...')
                return True

    def Install_fsociety(self):
        c1 = self.commands_(cmd=['echo "99" | fsociety'])
        if not c1:
            c2 = self.commands__(cmd='sudo chmod 777 -R {}fsociety && bash {}fsociety/install.sh'.format(self.root,self.root))
            if c2:
                print('fsociety安装成功...')
            else:
                print('fsociety安装失败...')
            return False
        else:
            print('fsociety 正在运行...')
            return True

    def Install_dnsfind(self):
        c1 = self.commands_(cmd=['python2 {}dnsfind/run.py --help'.format(self.root)])
        if not c1:
            c2 = self.commands__(cmd='python2 -m pip install -r {}dnsfind/reqs.txt'.format(self.root))
            if c2:
                print('dnsfind 安装成功...')
            else:
                print('dnsfind 安装失败...')
        else:
            print('dnsfind 正在运行...')

    def Result_subdns(self):
        catalog = "{}output".format(self.root)
        filename1 = []
        filename2 = []
        for root,dirs,files in os.walk(catalog):
            for files in files:
                filename1.append(root+'/'+files)
                filename2.append(files)
        
        return (filename1,filename2)

    def Result_DiscoverTarget(self):
        catalog = "{}DiscoverTarget".format(self.root)
        filename = []
        for root,dirs,files in os.walk(catalog):
            if 'URL.txt' in files:
                for files in files:
                    filename.append(root+'/'+files)
                    filename.append(files)
            
        if '{}DiscoverTarget/URL.txt'.format(self.root) not in filename:
            return False
        
        return (filename[0],filename[1])

    def Select_Files_(self):
        """
        获取“subdns”工具日志的域名和ip地址。
        """
        filename = self.Result_subdns()
        i = 0
        for filename1 in filename[0]:
            print('查看的文件 | {}.{}'.format(i,filename1))
            i += 1
        
        ipt1 = input('文件编号>')
        i = 0
        domains = []
        ips = []
        for filename2 in filename[0]:
            if ipt1 == str(i):
                with open(filename2,'r') as r:
                    for line in r.readlines():
                        data1 = line.split(' ')
                        for data2 in data1:
                            data3 = data2.strip().split('[')
                            for data4 in data3:
                                data5 = data4.strip().split(']')[0].strip()
                                if '\'' in data5:
                                    ip1 = data5.split('\'')
                                    for ip2 in ip1:
                                        if '\'' not in ip2 and ip2 and ',' not in ip2:
                                            print('')
                                            print('存活的IP地址...')
                                            print('----------------------')
                                            print(ip2.strip())
                                            print('----------------------')
                                            print('')
                                            ips.append(ip2.strip())
                                if '\'' not in data5:
                                    print('')
                                    print('存活的域名...')
                                    print('----------------------')
                                    print(data5)
                                    print('----------------------')
                                    print('')
                                    domains.append(data5)
                            
            i += 1
        return (domains,ips)

    def Select_Files__(self):
        domains = []
        filename = self.Result_DiscoverTarget()[0]
        with open(filename,'r') as r:
            print('收集的域名...')
            for line in r.readlines():
                print('')
                print('---------------------------------------------------')
                print(line.strip())
                print('---------------------------------------------------')
                print('')
                domains.append(line.strip())
        return domains

    def Get_Filename(self,path):
        """
        获取指定目录下的所有文件绝对路径.
        """
        pathname = []
        catalog = path
        for (dirpath, dirnames, filenames) in os.walk(catalog):     
            for filename in filenames:  
                pathname += [os.path.join(dirpath, filename)]
        
        return pathname



        




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
            print(content)
            c2 = input('>')
            if not c2:
                self.Run_subdns()
            if c2 is '1':
                c3 = self.commands__(cmd=['python3 {}subdns/subdns.py --help'.format(self.root)])
                print(c3)
                print('')
                print("##############################################################################################")
                print(helps1)
                self.Run_subdns()
            if c2 is '2':
                print(helps2)
                ipt1 = input('Url>')
                c3 = self.commands__(cmd=['python3 {}subdns/subdns.py -u {} -d mini_names.txt'.format(self.root,ipt1)])
                self.Run_subdns()
            if c2 is '3':
                print('字典存放路径:$HOME/.Tools/Tools_list/dict')
                print('如果存放好了字典，请输入字典名字...')
                print(helps2)
                ipt1 = input('Url>')
                ipt2 = input('Dict>')
                c3 = self.commands__(cmd=['python3 {}subdns/subdns.py -u {} -d {}'.format(self.root,ipt1,ipt2)])
                self.Run_subdns()
            if c2 is '4':
                self.Select_Files_()
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
            print(content)
            ipt1 = input('>')
            if ipt1 is '1':
                print(helps1)
                c2 = self.commands__(cmd=['python2 {}DiscoverTarget/DiscoverTarget.py --help'.format(self.root)])
                self.Run_DiscoverTarget()
            if ipt1 is '2':
                keywords = input('>')
                c2 = self.commands__(cmd=['python2 {}DiscoverTarget/DiscoverTarget.py -B {}'.format(self.root,keywords)])
                self.Run_DiscoverTarget()
            if ipt1 is '3':
                print('例子1：> -B hello word')
                print('例子2：> -Z app:"Apache-Tomcat"')
                c3 = input('> ')
                c4 = self.commands__(cmd='python2 {}DiscoverTarget/DiscoverTarget.py {}'.format(self.root,c3))
                self.Run_DiscoverTarget()
            if ipt1 is '4':
                self.Select_Files__()
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
            print(content)
            ipt1 = input('>')
            if not ipt1:
                self.Run_dirmap()
            if ipt1 is '1':
                print(helps1)
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py --help'.format(self.root))
                self.Run_dirmap()
            if ipt1 is '2':
                print('例子：Url>https://www.baidu.com/index.php?id=1')
                ipt2 = input('Url>')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py -iU {} -t 30 -lcf --debug'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '3':
                print('例子: Filename> DiscoverTarget/URL.txt')
                ipt2 = input('Filename> ')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py -iF {} -t 30 -lcf --debug'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '4':
                print('输入选项...')
                print('例子1: > --help')
                print('例子2: > --iN xxx')
                ipt2 = input('> ')
                c2 = self.commands__(cmd='python3 {}dirmap/dirmap.py {}'.format(self.root,ipt2))
                self.Run_dirmap()
            if ipt1 is '5':
                pass
            if ipt1 is '0':
                self.main()
    
    def Run_xcdn(self):
        print("""
1.输入url.
0.返回菜单.
        """)
        ipt1 = input('>')
        if not ipt1:
            self.Run_xcdn()
        if ipt1 is '1':
            ipt2 = input('Url>')
            c1 = self.commands__(cmd='python3 {}xcdn/xcdn.py {}'.format(self.root,ipt2))
            self.Run_xcdn()
        if ipt1 is '0':
            self.main()

    def Run_DirBrute(self):
        print("""
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
        ipt1 = input('>')
        if ipt1 is '1':
            print(helps1)
            self.Run_DirBrute()
        if ipt1 is '2':
            dictnames = self.Get_Filename('{}DirBrute/dics/'.format(self.root))
            ipt2 = input('Url>')
            print('选择字典...')
            for dictname in dictnames:
                print(dictname)
            ipt3 = input('DictPath>')
            self.commands__(cmd='python2 {}DirBrute/dirbrute.py {} -e php -t 10 -d {}'.format(self.root,ipt2,ipt3))
            self.Run_DirBrute()
        if ipt1 is '0':
            self.main()
        
    def Run_xwaf(self):
        print("""
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
        ipt1 = input('>')
        if not ipt1:
            self.Run_xwaf()
        if ipt1 is '1':
            print(helps1)
            self.Run_xwaf()
        if ipt1 is '2':
            ipt2 = input('Url>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -u "{}"'.format(self.root,ipt2))
            self.Run_xwaf()
        if ipt1 is '3':
            ipt2 = input('Url>')
            ipt3 = input('Data>')
            ipt4 = input('Post parameter>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -u "{}" --data="{}" -p {}'.format(self.root,ipt2,ipt3,ipt4))
            self.Run_xwaf()
        if ipt1 is '4':
            ipt2 = input('1>')
            ipt3 = input('2>')
            ipt4 = input('3>')
            self.commands__(cmd='python3 {}bypass_waf/xwaf.py -r {} -p {} --level {}'.format(self.root,ipt2,ipt3,ipt4))
            self.Run_xwaf()
        if ipt1 is '0':
            self.main()

    def Run_fsociety(self):
        print("""
1.Run Fsociety
0.返回菜单.
        """)
        c1 = self.Install_fsociety()
        if c1:
            ipt1 = input('>')
            if ipt1 is '1':
                self.commands__(cmd='fsociety')
                self.Run_fsociety()
            if ipt1 is '0':
                self.main()


    def main(self):
        content1 = """
1.信息收集.
2.web程序.
3.黑盒测试工具包.
c.clear.
0.退出.
        """
        print(content1)
        ipt1 = input('>')
        if not ipt1:
            self.main()
        if ipt1 is '1':
            content2 = """
########
信息收集
########
1.子域名爆破.
2.URL采集.
3.web目录扫描.
4.尝试找出cdn背后的真实ip.
0.返回菜单.
            """
            print(content2)
            ipt2 = input('>')
            if not ipt2:
                self.main()
            if ipt2 is '1':
                self.Run_subdns()
            if ipt2 is '2':
                self.Run_DiscoverTarget()
            if ipt2 is '3':
                print("""
#######
选择工具
#######
1.dirmap.
2.DirBrute.
0.返回菜单.
                """)
                ipt3 = input('>')
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
            print("""
########
web程序
#######
1.xwaf waf自动化绕过工具.
0.返回菜单.
            """)
            ipt2 = input('>')
            if ipt2 is '1':
                self.Run_xwaf()
            if ipt2 is '0':
                self.main()
        if ipt1 is '3':
            print("""
1.Fsociety.
0.返回菜单.
            """)
            ipt2 = input('>')
            if not ipt2:
                self.main()
            if ipt2 is '1':
                self.Run_fsociety()
            if ipt2 is '0':
                self.main()
        if ipt1 is 'c':
            self.commands__(cmd='clear')
            self.main()
        if ipt1 is '0':
            self.commands__(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])
            exit(0)

    def test(self):
        # c = self.commands_(cmd=['ls'])
        # print(c)
        # self.Install_subdns()
        pass
        


# print(logo)
# print('')
# r = Run()
# r.test()
# r.Install_dirmap()
# r.Select_Files__()
# r.Run_dirmap()
# r.main()




