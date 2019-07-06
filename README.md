# </> Eagle


### 概述
    一个工具集合的黑盒测试框架，选择指定编号的工具即可使用，工具依赖环境将自动配置，
    工具会提供帮助信息.框架使用python3开发，kali linux平台运行，基本的环境请自行安装.


### 使用
    Eagle --help


### 安装
    sudo chmod +x ./install && ./install


### 下载
    推荐：百度云盘 https://pan.baidu.com/s/1g_qBZhC1oajd0zH5SGVouQ 提取码: bpcz
    不推荐：git clone ... 速度有点慢.

### 配置说明

lib/setting.py:
    
    提供基本的属性设置.

lib/batch 目录:

    存放批量url字典的目录.

dict 目录:

    存放字典.

output 目录:

    存放subdns工具输出结果.

lib/INIT:

    初始化工具,提供初始化操作.

### 使用

笔记搜索:
    
    # PDF search
    pdfgrep <keyword> -r -n ./note/*
    
    # text search
    grep <keyword> -r -n ./note/*







