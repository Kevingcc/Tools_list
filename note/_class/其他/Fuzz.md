# 渗透测试.


概述

    本文讲解个人的SRC挖掘经验、Fuzz测试方法、批量POC验证和信息收集.所谓FUZZ,即模糊测试简单的理解就是一半人工测试一半使用工具进行自动化测试.每个安全工具各具特色，要将每个工具的功能发挥到极致就需要彻底的了解该工具的运作过程.
    

正文

    1.信息收集.
    众所周知,src要想好信息收集不可少.信息收集将决定你下一步的好与坏,收集的线索越多,漏洞几率也就越大.
    下面将介绍信息收集的一些方法:
        
        1.搜索引擎:
            google hack 360 baidu 收集已知的域名、指纹、敏感目录;天眼查功能与shodan 相似;shodan 收集已知的ip 端口号 该服务器是否存在漏洞 指纹、中间件等等......
             
        2.DNS 查询.
            https://dnsdb.io/zh-cn/

        3.社工库.
            现有的或自己构建.

        4.子域名爆破,通过字典与域名拼接的方法暴力枚举子域名;
        
        5.xcdn 通过此工具获取domain真实ip address;
        
        6.敏感目录扫描.
            wwwscan
            DirBuster
            dirb
            iis_shortname_scanner 
            burpsuite
                跑字典.
            cscan
            https://pentest-tools.com
            https://hackertarget.com/

        7.whois查询这个厂商
            国内的whois查询:http://whois.chinaz.com
            国外的whois查询:https://who.is
            可以得到的信息：
            邮箱
            电话
            联系人
            域名注册商
            接着whois反查这个站点的主持人邮箱和公司名称
            可以得到的信息：
            部分子域名

        8.天眼查这个厂商
            可以获取到兄弟域名的信息

        9.子域名挖掘
            先进行在线查询
            推荐在线查询的站点:https://phpinfo.me/domain/
            然后在用国外的dns接口进行查询:https://dns.bufferover.run/dns?q=你的域名
            百度域名查询的接口:http://ce.baidu.com/index/getRelatedSites?site_address=你的域名

            使用subDomainsBrute工具进行查询
            仓库地址:https://github.com/lijiejie/subDomainsBrute
            可以得到的信息：
            一大批子域名

        10.是否有WAF
            一些直自己有SRC平台的厂商或安全做的很好厂商都有安装WAF
            对部分站点进行WAF判断，如果部分有的话那么绝大多数都有安WAF。当然也有单个安WAF的
            可获得的信息：
            站点是否安装了WAF

        11.端口扫描和系统判断
            对弄出来的子域名进行整理，获取IP然后用nmap扫描80,443,8080或指定端口
            可获得的信息：
            开放的端口
            系统类型

        12.判断存活的站点和获取HTTP响应头的Server头
            有些子域名是死掉的或者过期域名等其他类因数，要对其进行排除
            可获得的信息：
            还存活的域名
            web的容器服务

        13.反查IDC
            使用IP反查IDC
            推荐站点:https://myip.ms
            相同站点查询
            可获得信息
            服务器的IDC
            同类的站点

        14.信息整理
            获得了这么多信息当然要对他们进行整理，创建两个xls文件
            一个放查询到的信息，另一个放查询到的子域名

        15.先从补天哪里看到你要挖的厂商信息，可以得到这么几个信息
            1.厂商名称
            2.厂商的漏洞收集范围
            3.厂商提供的一些东东

        16.判断是否有CDN
            如果没有CDN就可以对厂商给的域名进行C段扫描和旁站查询
            因为一些大厂直接买了一个C段的
            推荐工具:whatweb
            可以得到的信息：
            C段的站点
            同IP站点

            有CDN则进行真实IP获取，有那么几个操作
            1.查询DNS解析记录
            2.站长超级ping（关注IP出现次数最多的IP绑定hosts文件访问）
            3.钟馗之眼等引擎进行搜索，查询真实IP
            4.DNS渊源
            5.DDOS打回原形

        17.SRC挖掘初探之随缘XSS挖掘
            挖掘点:
                1.登陆跳转处XSS
                2.Image处的XSS
                3.邮件提交处的XSS
                4.一个受阻的XSS

                https://www.360zhijia.com/anquan/455756.html

        18.maltego信息收集
            信息收集很全的工具，但是免费版本基本很多实体都被禁止使用。对服务器的信息收集很全。

        19.源码泄露
            各源码托管平台，搜索项目名称.平台有SVN、github、gitee、gitcafe、code.csdn.net 等等...

        20.邮箱信息
            1.收集邮箱信息主要有两个作用：
                1.通过发现目标系统账号的命名规律，可以用来后期登入其他子系统.
                2.爆破登入邮箱用.
            
            2.通常邮箱的账号有如下几种生成规律:
                zhangxiaosan@xxx.com     xiaosan.zhang@xxx.com        zxiaosan@xxx.com

            当我们收集几个邮箱之后，便会大致猜出对方邮箱的命名规律;除了员工的邮箱之外，通过公司会有一些共有的邮箱，比如人力的邮箱、客服的邮箱，hr@xxx.com/kefu@xxx.com,这种邮箱有时会存在弱口令，在渗透时可额外留意一下。
                
                1.我们可以通过手工或者工具的方式来确定搜集邮箱： 
                    1.手工的方式：
                        1.可以到百度等搜索引擎上搜索邮箱信息
                        2.github等第三方托管平台
                        3.社工库

                2.工具方式：
                    1.The Harvester:
                        1.Google
                        2.Bing
                        3.PGP服务器的电子邮件
                        4.主机以及子域名,因此需要翻墙运行该工具.
                            ./theHarvester.py -d 域名 -1 1000 -b all

        
        21.src挖掘思路:
            https://blog.csdn.net/skythesea/article/details/81050796
            1.常规操作–官方域名            
                基本上SRC都会提供相关域名，常以 *.xx.oo 形式告诉一级域名。
            2.常规操作–域名加工
                1.根据主域名，可以获取二级域名、三级域名、......主要姿势可以有：
            3.DNS域传送漏洞
            4.备案号查询
            5.SSL证书
            6.google搜索C段
            7.APP提取
            8.微信公众号
            9.比较普遍方法:
                1.常规操作–IP网段
                2.常规操作–指纹识别
                3.常规操作？–历史漏洞
                4.常规操作？–敏感信息
                5.QQ群备注或介绍….甚至混入企业qq工作群…


        22.任意文件下载漏洞学习:
            任意文件下载漏洞由于在处理下载脚本的时候没有做好对应的一个控制，导致下载文件的参数可控。从而下载其他路径下的文件
            上zoomye寻找关键字：download.php?path=
            https://422926799.github.io/posts/71ea52cb.html

            1.参数名总结:
                download.php?path=
                &RealPath=
                &FilePath=
                &ﬁlepath=
                &Filepath=
                &Path=
                &path=
                &inputFile=
                &Inputfile=
                &url=
                &urls=
                &Lang=
                &dis=
                &data=
                &Data=
                &readﬁle=
                &ﬁlep=
                &src=
                &menu=
                META-INF
                WEB-INF

            2.google search:
                inurl:"readfile.php?file="
                inurl:"read.php?filename="
                inurl:"download.php?file="
                inurl:"down.php?file="

            3.修复方案:
                过滤.(点)，使用户在url中不能回溯上级目录
                正则严格判断用户输入参数的格式
                php.ini配置open_basedir限定文件访问范围

            4.敏感文件如下:
                Windows：
                C:\boot.ini  //查看系统版本
                C:\Windows\System32\inetsrv\MetaBase.xml  //IIS配置文件
                C:\Windows\repair\sam  //存储系统初次安装的密码
                C:\Program Files\mysql\my.ini  //Mysql配置
                C:\Program Files\mysql\data\mysql\user.MYD  //Mysql root
                C:\Windows\php.ini  //php配置信息
                C:\Windows\my.ini  //Mysql配置信息
                ...
                Linux：
                /root/.ssh/authorized_keys
                /root/.ssh/id_rsa
                /root/.ssh/id_ras.keystore
                /root/.ssh/known_hosts
                /etc/passwd
                /etc/shadow
                /etc/my.cnf
                /etc/httpd/conf/httpd.conf
                /root/.bash_history
                /root/.mysql_history
                /proc/self/fd/fd[0-9]*(文件标识符)
                /proc/mounts
                /porc/config.gz

            5.python脚本扫描思路:
                1.遍历第一点的所有参数名<for parameter in filename.readlines():>;
                2.通过google hack 搜索可能存在漏洞的url;
                3.判断该url是否存在漏洞.<if parameter in url:>;
                4.漏洞验证:
                    1.payloads 构造:
                        {agreement}://{domain}/{filename}?{parameter}=/etc/passwd
                        {agreement}://{domain}/{filename}?{parameter}=../../../../../../../../etc/passwd
                        {agreement}://{domain}/{filename}?{parameter}=../../../../../../../../etc/passwd%00
                    
                    2.判断响应码:
                        if status_code == 200:
                            print('')
                            print(f'[+]{domain} -> 存在任意文件下载漏洞.')
                            print(f'[!]攻击载荷 -> {payloads}')
                        else:
                            print(f'[-]{domain} -> 不存在任意文件下载漏洞.')
            
            6.burp suite 替换目标,跑字典.

                    





        23.漏洞测试.
            shodan 是一个分布式爬虫,它内置许多cve 脚本,并且会帮我们提供简单的漏洞扫描工作.
            利用这一特性,上shodan 搜索 构造搜索语法<ip...>,显示结果页面遍历所有可靠性结果链接,是否有cve 或别的漏洞编号关键字的痕迹,如果有我们还可以尝试对有指定漏洞编号的漏洞服务器进行poc验证.
            





    2.维权访问.
        
        1.web端权限维持
            构造文件包含漏洞，，包括基本文件包含姿势，制作图片木马，文件包含漏洞是代码注入的一种，其原理就是注入一段用户能够控制的脚步或代码，并在服务器段执行，代码输入的典型代表即使“文件包含” ，文件包含可能出现在JSP、PHP、ASP等语言中，其原理基本都是一样的。
            https://www.cnblogs.com/xinxianquan/p/9302389.html


    3.我的安全视界观
     
        生活的艺术，就是艺术的生活；
        挖洞的思路，就是思考着挖洞。
        各路SRC的迅速崛起，无疑给广大白帽子带来了福音与福利。展露拳脚，占据排行，赚零花钱，获得认可，节日礼物，与小姐姐聊天.......可谓干劲十足，即使拖着疲倦的身躯回到家，也想打开电脑、关灯、戴上耳塞听着音乐，开始沉浸在自由自在的世界。
        信息收集是伊始，个人觉得也是重中之重。



