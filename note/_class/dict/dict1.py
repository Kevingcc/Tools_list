#!/usr/bin/env python3
# coding:utf-8

from lib import Libs


class dict1(Libs):

    def __init__(self):
        super(dict1,self).__init__()

    def content(self):
        content = """
# 字典构造思路


## **_目录_**
>[<h4>指纹信息</h4>](#1)
>[<h4>常见爆破组合</h4>](#2)

<h3 id="1">指纹信息<h3>

<h4> 
    
    1.该后台的指纹信息,通过搜索引擎搜索该后台的弱口令.

    2.与该后台相关的user 邮箱 指纹信息.

    3.生日日期.

    若以上方法都不通则尝试通过现有的指纹信息构造字典.
    
</h4>


<h3 id="2">常见爆破组合</h3>

    evince -p 1 {}note/class/dict/pdf/1.pdf

<h4>



</h4>
        """.format(self.root)

        w = open('{}note/_class/dict/dict1.md'.format(self.root),'w')
        w.write(content)
        w.close()
        self.commands__(cmd='code {}note/_class/dict/dict1.md'.format(self.root))



