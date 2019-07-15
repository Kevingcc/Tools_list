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
           'regular','Libs',
           '_grep','grep']



from lib.setting import option_install
import os

if option_install:
    os.system('python3 -m pip install colorlog==4.0.2')


try:
    import random
    import traceback
    import subprocess
    import re
    import os
    import sys
    import json
    import time
    from lxml import etree
    import requests
    from json import load
    from json import loads
    from json import dump
    from json import dumps
except Exception as e:
    pass

from lib.setting import option_install
from lib.setting import system_platform
from lib.setting import key_config
from lib.setting import kali_user
from lib.setting import Ichrome

if system_platform == 'deepin':
    system_platform = 'deepin'
elif system_platform == 'kali':
    system_platform = 'kali'

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

# sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/'


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



def get_domain(domain):
    """
    获取域名.
    domain = get_domain('https://www.baidu.com/')
    print(domain)
    >>> www.baidu.com
    """
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
    
    for p in pathname:
        if pathname:
            return pathname
        else:
            return False


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
        self.root = root
        c1 = self.commands_(cmd=['sudo chmod +x {}lib/pyc_clear && bash {}lib/pyc_clear'.format(self.root,self.root)])
        warning(c1)
        
        import sqlite3
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
        if system_platform == 'deepin':
            c1 = self.commands__(cmd=['hash chromedriver'])
            if not c1:
                print_('正在配置 chromedriver...')
                c1 = self.commands__(cmd='sudo ln -s {}Chromedriver/chromedriver_70.0.3538.67 /usr/bin/chromedriver'.format(self.root))
                c2 = self.commands__(cmd='sudo chmod +x /usr/bin/chromedriver')
                if c1 and c2:
                    print_('chromedriver 配置完成...')
            else:
                print_('chromedriver 正在运行...')

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

    def phpmyadmin_config(self):
        """
        phpmyadmin_sqlite config
        """
        c1 = self.commands__('sudo cp -v -r {}lib/phpmyadmin_sqlite /var/www/html'.format(root))
        c2 = self.commands__('sudo chmod -R 777 /var/www/html/*')
        c3 = self.commands__('sudo /etc/init.d/apache2 restart')
        c4 = self.commands__('sudo cp -v -r {}Webfinger/lib/web.db /var/www/html/phpmyadmin_sqlite'.format(root))
        c5 = self.commands__('sudo /etc/init.d/apache2 restart')
        if c1 and c2 and c3 and c4 and c5:
            print_('phpmyadmin 配置完成...')
        else:
            print_('phpmyadmin 配置失败...')

    def Install_TideFinger(self):
        c1 = self.commands_(cmd=['python2 {}TideFinger/TideFinger.py --help'.format(self.root)])
        if not c1:
            c2 = self.commands__(cmd='sudo python2 -m pip install lxml requests bs4 --user')
            if c2:
                print_('TideFinger 依赖项安装完成...')
            else:
                print_('TideFinger 依赖项安装失败...')
        else:
            print_('TideFinger 正在运行...')

    def Install_information_gathering_jiushi(self):
        """
        安装九世信息收集工具依赖项.
        """
        print_('安装九世信息收集工具依赖项.')
        try:
            c1 = 'python3 -m pip install python-whois==0.7.1 --user'
            c2 = 'python3 -m pip install dnspython==1.16.0 --user'
            c3 = 'python3 -m pip install IPy==1.0 --user'
            self.commands__(c1)
            self.commands__(c2)
            self.commands__(c3)
            print_('安装九世信息收集工具依赖项完成.')
        except:
            print_('安装九世信息收集工具依赖项失败.')

    def source_config(self):
        print_(f'{system_platform}源配置.')
        if system_platform == 'kali':
            c1 = self.commands__(cmd=f'sudo cp -v -r {self.root}bak/sources.list.kali /etc/apt/sources.list')
            c2 = self.commands__(cmd='sudo apt-get update')
            if c1:
                print_('kali 源配置完成.')
            else:
                print_('kali 源配置失败.')
        elif system_platform == 'deepin':
            c1 = self.commands__(cmd=f'sudo cp -v -r {self.root}bak/sources.list.deepin /etc/apt/sources.list')
            c2 = self.commands__(cmd='sudo apt-get update')
            if c1:
                print_('deepin 源配置完成.')
            else:
                print_('deepin 源配置失败.')
    
    def Install_chrome(self):
        if Ichrome:
            print_('kali 安装 google_chrome...')
            self.commands__(cmd='sudo apt-get -y install axel')
            self.commands__(cmd='sudo apt-get -y install gdebi')
            self.commands__(cmd='mkdir $HOME/download_chrome')
            self.commands__(cmd='cd $HOME/download_chrome && axel -n 60 "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"')
            self.commands__(cmd='cd $HOME/download_chrome && sudo echo "y" | gdebi ./google-chrome-stable_current_amd64.deb')
            self.commands__(cmd='cd $HOME/download_chrome && axel -n 60 "http://cdn.npm.taobao.org/dist/chromedriver/75.0.3770.140/chromedriver_linux64.zip"')
            self.commands__(cmd='cd $HOME/download_chrome && unzip ./chromedriver_linux64.zip && sudo ln -s $HOME/download_chrome/chromedriver /usr/bin/chromedriver && sudo chmod +x /usr/bin/chromedriver')
            print_('kali 安装 google_chrome 完毕...')

    
    def kali_establish_user(self):
        if kali_user:
            print_('kali 添加user...')
            ipt1 = input_('kali add username>')
            self.commands__(cmd=f'useradd -m {ipt1}')
            self.commands__(cmd=f'passwd {ipt1}')
            self.commands__(cmd=f'usermod -a -G sudo {ipt1}')
            self.commands__(cmd=f'chsh -s /bin/bash {ipt1}')
            print_('kali 添加user 完毕...')


    def Install_Basics(self):
        self.source_config()
        self.commands__(cmd='sudo cp -v -r ~/.pip /root/')
        self.commands__(cmd='python3 -m pip install lxml==4.3.3')
        self.Install_selenium()
        self.Install_requests()
        self.Config_chromedriver()
        self.Install_xSStrike()
        self.Install_POC_T()
        self.phpmyadmin_config()
        self.Install_TideFinger()
        self.Install_information_gathering_jiushi()
        self.commands__(cmd='sudo apt-get -y install xfce4-terminal')
        self.commands__(cmd='sudo apt-get -y install pavucontrol')
        self.commands__(cmd='sudo python2 -m pip install nmapparser==0.2.5 --user')
        self.commands__(cmd='sudo apt-get -y install nmap')
        self.commands__(cmd='sudo apt-get -y install figlet')
        self.commands__(cmd='sudo apt-get -y install toilet')
        self.commands__(cmd='sudo apt-get -y install pdfgrep')
        self.commands__(cmd='python2 -m pip install sqlmap --user')
        self.commands__(cmd='python3 -m pip install asyncio==3.4.3 --user')
        self.commands__(cmd='python3 -m pip install gevent==1.4.0 --user')
        self.commands__(cmd='python3 -m pip install virtualenv==16.6.1 --user')
        self.commands__(cmd='python2 -m pip install virtualenv==16.6.1 --user')
        self.commands__(cmd='python3 -m pip install gevent==1.4.0 --user')
        self.commands__(cmd='sudo apt-get -y install fping')
        self.commands__(cmd='sudo apt-get -y install gedit')
        self.commands__(cmd='sudo apt-get -y install gdebi')
        self.commands__(cmd='sudo apt-get -y install axel')

        if system_platform == 'kali':
            self.commands__(cmd='python3 -m pip install exp10it==2.7.21 --user')
            self.Install_chrome()
            self.kali_establish_user()

        if system_platform == 'deepin':
            self.commands__(cmd='sudo apt-get -y install python-scapy')
            self.commands__(cmd='sudo apt-get -y install evince')
            self.commands__(cmd='sudo apt-get -y install code')
            if key_config:
                self.commands__(cmd='sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6')
                self.commands__(cmd='sudo apt-get update')
        
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

    
    def Install_POC_T(self):
        c1 = self.commands_(cmd='python2 {}/POC-T/POC-T.py --help'.format(self.root))
        if not c1:
            c2 = self.commands__(cmd='python2 -m pip install -r {}POC-T/requirement.txt'.format(self.root))
            if c2:
                print_('POC_T 安装成功...')
            else:
                print_('POC_T 安装失败...')
        else:
            print_('POC_T 正在运行...')


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



def get_POC_T_script():
    """
    获取POC_T工具script目录下的所有文件名.
    script/
        |zhimeng-cms.py

    f1,f2,f3 = get_POC_T_script()
    
    f1
    >>> ['zhimeng-cms',...] -> list
    f2
    >>> ['zhimeng',...] -> list
    f3
    >>> ['zhimeng-cms.py',...] -> list
    """
    filenames_1 = []
    filenames_2 = []
    filenames_3 = []
    _get_filename = get_filename_('{}POC-T/script'.format(root))
    for f1 in _get_filename:
        filename = f1.replace('.py','')
        filenames_1.append(filename)

        filename1 = f1.replace('.py','')
        filename2 = filename1.split('-')
        filename3 = filename2[0]
        filenames_2.append(filename3)

        filename1 = f1
        filenames_3.append(filename1)

    return [filenames_1,filenames_2,filenames_3]
    

def _grep(keyword,path,regex=0,highlight=1):
    """
    文本文件关键字搜索.
    行号.
    关键字高亮.
    正则判断.
    obj = _grep(keyword,path,regex=0)
    obj -> 迭代
    for o in obj:
        line_number,line_content = o
    """
    result1 = []
    count = -1
    for count,line in enumerate(open(r"{}".format(path),'r')):
        count += 1
        line_number = count
        line_content = line
        if regex:
            find1 = re.findall(keyword,line_content)
            if find1:
                if highlight:
                    lc1 = _red(line_content)
                else:
                    lc1 = line_content
                result1.append([str(line_number),lc1.strip()])
        else:
            if line_content.find(keyword) != -1:
                lc1 = line_content.replace(keyword,_red(keyword))
                result1.append([str(line_number),lc1.strip()])
    
    return result1


def grep(keyword,content):
    """
    文本文件关键字搜索.
    关键字高亮.
    obj = _grep(keyword,content)
    print(obj)
    >>> xxx
    type(obj)
    >>> str
    """
    if content.find(keyword) != -1:
        lc1 = content.replace(keyword,_red(keyword))
        return lc1




poc_t_helps = """
usage: python POC-T.py -s bingc -aZ "port:8080"

powered by cdxy <mail:i@cdxy.me>

ENGINE -- 发动机:
  -eT                   Multi-Threaded engine (default choice) -- 多线程引擎（默认选项）
  -eG                   Gevent engine (single-threaded with asynchronous) -- GEvent引擎（单线程异步）
  -t NUM                num of threads/concurrent, 10 by default -- 线程数/并发数，默认为10个

SCRIPT -- 脚本:
  -s NAME               load script by name (-s jboss-rce) or path (-s ./script/jboss.py) -- 按名称加载脚本 (-s jboss-rce) 或路径 (-s ./script/jboss.py)

TARGET -- 目标:
  -iS TARGET            scan a single target (e.g. www.wooyun.org) -- 扫描单个目标（如www.wooyun.org）
  -iF FILE              load targets from targetFile (e.g. ./data/wooyun_domain) -- 从targetfile加载目标（例如/data/wooyun_域）
  -iA START-END         generate array from int(start) to int(end) (e.g. 1-100) -- 从int（开始）到int（结束）生成数组（例如1-100）
  -iN IP/MASK           generate IP from IP/MASK. (e.g. 127.0.0.0/24) -- 从IP/屏蔽生成IP。（例如127.0.0.0/24）

API:
  -aZ DORK, --zoomeye DORK ZoomEye dork (e.g. "zabbix port:8080") -- Zoomeye Dork（例如“Zabbix端口：8080”)　zoomeye search.
  -aS DORK, --shodan DORK Shodan dork. -- shodan search.
  -aG DORK, --google DORK Google dork (e.g. "inurl:admin.php") -- google search.
  -aF DORK, --fofa DORK FoFa dork (e.g. "banner=users && protocol=ftp") -- fofa search.
  --limit NUM           Maximum searching results (default:10) -- 最大搜索结果（默认值：10）
  --offset OFFSET       Search offset to begin getting results from (default:0) -- 开始获取结果的搜索偏移量（默认值：0）
  --search-type TYPE    [ZoomEye] search type used in ZoomEye API, web or host (default:host) -- [ZoomEye]在ZoomEye API、Web或主机中使用的搜索类型（默认：主机）
  --gproxy PROXY        [Google] Use proxy for Google (e.g. "sock5 127.0.0.1 7070" or "http 127.0.0.1 1894" -- [Google]使用Google代理（例如“sock5 127.0.0.1 7070”或“http 127.0.0.1 1894”

OUTPUT -- 输出:
  -o FILE               output file path&name. default in ./output/ -- 输出文件路径和名称。默认输入/输出/
  -oF, --no-file        disable file output -- 禁用文件输出
  -oS, --no-screen      disable screen output -- 禁用屏幕输出

MISC:
  --single              exit after finding the first victim/password. -- 找到第一个受害者/密码后退出。
  --show                show available script names in ./script/ and exit -- 在./script/和exit中显示可用的脚本名称
  --browser             Open notepad or web browser to view report after task finished. -- 任务完成后，打开记事本或Web浏览器查看报告。

SYSTEM:
  -v, --version         show program's version number and exit -- 显示程序的版本号并退出
  -h, --help            show this help message and exit -- 显示此帮助消息并退出
  --update              update POC-T from github source -- 从github源更新poc-t

"""





dirmap_helps = """
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


discovertarget_helps = """
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



subdns_helps = """
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


xsstrike_helps = """
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

dirbrute_helps = """
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


TideFinger_helps = """

Usage: python TideFinger.py -u http://www.123.com [-p 1] [-m 50] [-t 5] 

-u: 待检测目标URL地址
-p: 指定该选项为1后，说明启用代理检测，请确保代理文件名为proxys_ips.txt,每行一条代理，格式如: 124.225.223.101:80
-m: 指纹匹配的线程数，不指定时默认为50
-t: 网站响应超时时间，默认为5秒


"""


# 获取当前文件绝对路径.
# os.getcwd()

# python 设置环境变量
# print_(os.path.dirname(os.path.abspath(__file__))+'/test')
# sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/test')

# pyc文件清理
# find ./ -name "*.pyc" | xargs rm -rf