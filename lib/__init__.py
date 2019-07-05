#!/usr/bin/env python3
#coding:utf-8

__all__ = ['test','get_headers',
           'info','error',
           'warning','print_',
           'AttribDict','load',
           'loads','dump',
           'dumps','root',
           'red','blue',
           'green','input_',
           'regular','Libs']

try:
    import random
    import traceback
    import subprocess
    import re
    import os
    import json
    import time
    from lxml import etree
    import sqlite3
    import requests
    from json import load
    from json import loads
    from json import dump
    from json import dumps
except Exception as e:
    pass

from lib.setting import option_install
from .debug import test
from .debug import log
from .headers import get_headers
from .datatype import AttribDict


info = log.info
error = log.error
warning = log.warning



W = '\033[0m'
G = '\033[1;32m'
O = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'

root_ = subprocess.check_output('echo $HOME',shell=True).decode().strip()
root = '{}/.Tools/Tools_list/'.format(root_)


def print_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    print(color+content+W)

def red(content):
    d = R + content + W
    print(d)

def _red(content):
    d = R + content + W
    return d

def blue(content):
    d = B + content + W
    print(d)

def green(content):
    d = G + content + W
    print(d)

def input_(content):
    colors = ['G','O','R','B']
    color = eval(random.choice(colors))
    d = input(color+content+W)
    return d



def filter_domain(domain=[]):
    """
    过滤器.
    """
    d1 = []
    for data1 in domain:
            if not re.findall('\.xls',data1) and \
                not re.findall('\.sql',data1) and \
                not re.findall('\.txt',data1) and \
                not re.findall('www.google.com',data1) and \
                not re.findall('www.baidu.com',data1) and \
                not re.findall('baidu.com',data1) and \
                not re.findall('google.com',data1) and \
                not re.findall('github.com',data1) and \
                not re.findall('cnblogs.com',data1) and \
                not re.findall('csdn.net',data1) and \
                not re.findall('exploit-db.com',data1):
                d1.append(data1)

    return d1

def _commands(num):
    """
    命令选择.
    c = _commands(1)
    >>> 'xfce4-terminal -e "bash -c \\\"{}\\\""'
    """
    # commands
    if num == 1:
        cmd1 = 'xfce4-terminal -e "bash -c \\\"{}\\\""'
        return cmd1
    

def read_text(filename):
    lines = []
    with open('{}lib/{}'.format(root,filename),'r') as r:
        for line in r.readlines():
            lines.append(line.strip())
    return lines



def read_text_(filename):
    lines = []
    with open('{}'.format(filename),'r') as r:
        for line in r.readlines():
            lines.append(line.strip())
    return lines





def get_target_sqli_url():
        d1 = []
        d2 = []
        datas1 = read_text(filename='sqli1.txt')
        datas2 = read_text(filename='sqli2.txt')
        d1 = filter_domain(domain=datas1)
        d2 = filter_domain(domain=datas2)        

        return (d1,d2)



def get_url(domain):
    d1 = domain.split('/')
    for d2 in d1:
        if \
        d2 != 'https' and \
        d2 != 'http' and \
        d2 != '/' and \
        d2 and \
        d2 != 'https:' and \
        d2 != 'https:/' and \
        d2 != 'http:' and \
        d2 != 'http:/':
            return d2.strip()


def get_filename(path):
    """
    获取指定目录下的所有文件绝对路径.
    """
    pathname = []
    catalog = path
    for (dirpath, dirnames, filenames) in os.walk(catalog):     
        for filename in filenames:  
            pathname += [os.path.join(dirpath, filename)]
    
    return pathname

def get_filename_(path):
    """
    获取文件名称.
    """
    pathname = []
    catalog = path
    for (dirpath,dirnames,filenames) in os.walk(catalog):
        for filename in filenames:
            pathname.append(filename)
    return pathname


def regular(num):
    """
    正则匹配规则.
    1.匹配数字
    2.匹配字符
    3.匹配字符及数字

    例子:regular(1)
    返回结果:
        >>> \\d+
    """
    if num == 1:
        return '\d+'
    if num == 2:
        return '[a-zA-Z]+'
    if num == 3:
        return '[a-zA-Z0-9]'
    


def oBtain_resuLt(name):
    """
    返回subdns 工具结果.
    >>> o = oBtain_resuLt('xx.baidu.com.txt')
    >>> type(o)
    out[0] list
    >>> o[0][0] ==> domain
    >>> o[0][1] ==> ip
    """
    datas = []
    with open(name,'r') as r:
        for line in r.readlines():
            l1 = line.split('[')
            domain_ = l1[0].strip()
            ip = eval('['+l1[1].strip())
            datas.append([domain_,ip])

    return datas




class Libs(object):
    
    def __init__(self):
        self.root_ = self.commands_(cmd=['echo $HOME'])
        self.root = '{}/.Tools/Tools_list/'.format(self.root_)
        c1 = self.commands_(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])
        warning(c1)
        self.conn = sqlite3.connect('{}lib/GHack'.format(self.root))
        self.c = self.conn.cursor()
        if option_install:
            self.config_pip_source()
            c1 = self.Inspect_pip()
            self.Install_Basics()

    def etree_(self,xpath_,text):
        html = etree.HTML(str(text),etree.HTMLParser())
        return html.xpath(xpath_)

    def repair_html(self,text):
        html = etree.HTML(text)
        result = etree.tostring(html,encoding='utf-8')
        return result.decode('utf-8')

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

        # print_('查询成功...')


    def Write_Data(self,id_,page,type_,title,content):
        """
        写入数据.
        """
        try:
            expression = r"""INSERT INTO "Exploit" ("id","page","type","title","content") VALUES ('{}','{}','{}','{}','{}')""".format(id_,page,type_,title,content)
            # print_(expression)
            self.c.execute(expression)
            # print_('写入数据成功...')
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
            info('保存文件完成...')

    def Read_json(self,filename='id.json'):
        lines = []
        with open('{}lib/{}'.format(self.root,filename),'r') as r:
            for line in r.readlines():
                lines.append(line.strip())
        return lines


    def Save_text(self,filename,content):
        """
        参数: 1.filename 2.content
        
        绝对路径: /.../lib/<filename>
        """
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
            # print_(traceback.format_exc())
            pass
            

    def Read_text(self,filename):
        lines = []
        with open('{}lib/{}'.format(self.root,filename),'r') as r:
            for line in r.readlines():
                lines.append(line.strip())
        return lines

    def Save_text_(self,filename,content):
        with open('{}lib/{}'.format(self.root,filename),'a+') as w:
            w.write(str(content)+'\n')
            info('写入完毕...')

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
            # print_(traceback.format_exc())
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
            # print_(traceback.format_exc())
            return False   

    def config_pip_source(self):
        c1 = self.commands_(cmd=['echo $HOME'])
        if not os.path.exists(c1+'/.pip'):
            c2 = self.commands__(cmd='mkdir $HOME/.pip')
            cmd = 'sudo chmod +x {}lib/config_pip_source && {}lib/config_pip_source'.format(self.root,self.root)
            c = self.commands__(cmd=cmd)
            if c:
                info('pip 源配置完成...')
            else:
                info('pip.conf文件正常...')

    
    def Config_chromedriver(self):
        c1 = self.commands__(cmd=['hash chromedriver'])
        if not c1:
            info('正在配置 chromedriver...')
            c1 = self.commands__(cmd='sudo ln -s {}Chromedriver/chromedriver_70.0.3538.67 /usr/bin/chromedriver'.format(self.root))
            c2 = self.commands__(cmd='sudo chmod +x /usr/bin/chromedriver')
            if c1 and c2:
                info('chromedriver 配置完成...')
        else:
            info('chromedriver 正在运行...')

    # def Install_mechanize(self):
    #     c1 = self.commands__(cmd='python3 -m pip install mechanize==0.4.2')
    #     if c1:
    #         print_('mechanize 安装成功...')
    #     else:
    #         print_('mechanize 安装失败...')

    def Inspect_pip(self):
        c1 = self.commands_('python3 -m pip')
        c2 = self.commands_('python2 -m pip')
        if c1 and c2:
            info('pip3 pip2 运行正常...')
            return True
        else:
            info('pip3命令运行失败...')
            info('正在执行安装sudo apt-get install python3-pip')
            self.commands__('sudo apt-get -y install python3-pip')
            info('pip2命令运行失败...')
            info('正在执行安装sudo apt-get install python-pip')
            self.commands__('sudo apt-get -y install python-pip')
            return False

    def Install_Basics(self):
        self.commands__(cmd='python3 -m pip install lxml==4.3.3')
        self.Install_selenium()
        self.Install_requests()
        self.Config_chromedriver()
        self.Install_xSStrike()
        self.commands__(cmd='sudo apt-get -y install xfce4-terminal')
        self.commands__(cmd='sudo apt-get -y install pavucontrol')
        self.commands__(cmd='sudo python2 -m pip install nmapparser==0.2.5 --user')
        self.commands__(cmd='sudo apt-get -y install nmap')
        self.commands__(cmd='sudo apt-get -y install figlet')
        self.commands__(cmd='sudo apt-get -y install toilet')
        self.commands__(cmd='sudo apt-get -y install pdfgrep')

        # Install pyautogui...
        self.commands__(cmd='sudo pip3 install python3-xlib')
        self.commands__(cmd='sudo apt-get -y install scrot')
        self.commands__(cmd='sudo apt-get -y install python3-tk')
        self.commands__(cmd='sudo apt-get -y install python3-dev')
        self.commands__(cmd='python3 -m pip install pyautogui==0.9.44')
        
        info('依赖项安装完毕...')
        warning('如果要退出安装，设置 lib/setting.py option_install = False ...')
        exit(0)

    def Install_requests(self):
        c1 = self.commands__(cmd='python3 -m pip install requests==2.21.0')
        if c1:
            print_('requests 安装成功...')
        else:
            print_('requests 安装失败...')
    
    def Install_selenium(self):
        c1 = self.commands__(cmd='python3 -m pip install selenium==3.141.0')
        if c1:
            print_('selenium 安装成功...')
        else:
            print_('selenium 安装失败...')

    def Install_subdns(self):
        c2 = self.commands_(cmd=['python3 {}subdns/subdns.py --help'.format(self.root)])
        if not c2:
            print_('subdns.py 没有安装依赖项...')
            print_('subdns.py 正在安装依赖项...')
            c3 = self.commands__(cmd=['python3 -m pip install aiodns==2.0.0 colorlog==4.0.2'])
            if c3:
                print_('subdns.py 依赖项安装完成...')
            
            return False
        else:
            print_('subdns.py 正在运行...')
            return True

    def Install_DiscoverTarget(self):
        c1 = self.commands_(cmd=['sudo python2 {}DiscoverTarget/DiscoverTarget.py --help'.format(self.root)])
        if not c1:
            print_('DiscoverTarget.py 没有安装依赖项...')
            print_('DiscoverTarget.py 正在安装依赖项...')
            c2 = self.commands__(cmd=['sudo python2 -m pip install fofa==1.0.1 shodan==1.13.0 gevent==1.4.0 lxml==4.3.3 bs4==0.0.1 --user'])
            if c2:
                print_('DiscoverTarget.py 依赖项安装完成...')
            
            return False
        else:
            print_('DiscoverTarget.py 正在运行...')
            return True

    def Install_dirmap(self):
        c1 = self.commands_(cmd=['python3 {}dirmap/dirmap.py --help'.format(self.root)])
        if not c1:
            print_('dirmap.py 没有安装依赖项...')
            print_('dirmap.py 正在安装依赖项...')
            c2 = self.commands__(cmd=['python3 -m pip install -r dirmap/requirement2.txt'])
            if c2:
                print_('dirmap.py 依赖项安装完成...')
            
            return False
        else:
            print_('dirmap.py 正在运行...')
            return True

    def Install_fsociety(self):
        c1 = self.commands_(cmd=['echo "99" | fsociety'])
        if not c1:
            c2 = self.commands__(cmd='sudo chmod 777 -R {}fsociety && bash {}fsociety/install.sh'.format(self.root,self.root))
            if c2:
                print_('fsociety安装成功...')
            else:
                print_('fsociety安装失败...')
            return False
        else:
            print_('fsociety 正在运行...')
            return True

    def Install_dnsfind(self):
        c1 = self.commands_(cmd=['python2 {}dnsfind/run.py --help'.format(self.root)])
        if not c1:
            c2 = self.commands__(cmd='python2 -m pip install -r {}dnsfind/reqs.txt'.format(self.root))
            if c2:
                print_('dnsfind 安装成功...')
            else:
                print_('dnsfind 安装失败...')
        else:
            print_('dnsfind 正在运行...')

    def Install_xSStrike(self):
        c1 = self.commands_(cmd=['python3 {}XSStrike/xsstrike.py --help'.format(self.root)])
        if not c1:
            c2 = self.commands__(cmd='python3 -m pip install -r {}XSStrike/requirements.txt'.format(self.root))
            if c2:
                print_('XSStrike 安装成功...')
            else:
                print_('XSStrike 安装失败...')
        else:
            print_('XSStrike 正在运行...')    

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
        """
        libs = Libs()
        f1,f2 = libs.Result_DiscoverTarget()
        print(f1)
        >>> '/home/remix/.Tools/Tools_list/DiscoverTarget/URL.txt'
        print(f2)
        >>> 'URL.txt'
        """
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

    def sElect_Files_(self):
        """
        获取“subdns”工具日志的域名和ip地址。
        """
        filename = self.Result_subdns()
        i = 0
        for filename1 in filename[0]:
            print_('查看的文件 | {}.{}'.format(i,filename1))
            i += 1
        
        ipt1 = input('文件编号>')
        i = 0
        for filename2 in filename[0]:
            if ipt1 == str(i):
                d1 = oBtain_resuLt(filename2)
                try:
                    for d2 in d1:
                        time.sleep(1)
                        red('Domain ==> {}'.format(d2[0]))
                        blue('Ip ==> {}'.format(d2[1]))
                except:
                    pass

            i += 1



    def sElect_Files__(self):
        domains = []
        filename = self.Result_DiscoverTarget()[0]
        with open(filename,'r') as r:
            print_('收集的域名...')
            for line in r.readlines():
                print_('')
                print_('---------------------------------------------------')
                print_(line.strip())
                print_('---------------------------------------------------')
                print_('')
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



        





















# 获取当前文件绝对路径.
# os.getcwd()

# python 设置环境变量
# print_(os.path.dirname(os.path.abspath(__file__))+'/test')
# sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/test')

# pyc文件清理
# find ./ -name "*.pyc" | xargs rm -rf