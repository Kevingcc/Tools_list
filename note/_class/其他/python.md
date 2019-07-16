# python



python 可靠性方法:

    判断文件是否存在
    import os
    os.path.exists(test_file.txt)
    #True

    os.path.exists(no_exist_file.txt)
    #False


    判断文件夹是否存在
    import os
    os.path.exists(test_dir)
    #True

    os.path.exists(no_exist_dir)
    #False


    其实这种方法还是有个问题，假设你想检查文件“test_data”是否存在，但是当前路径下有个叫“test_data”的文件夹，这样就可能出现误判。为了避免这样的情况，可以这样:

    只检查文件
    import os
    os.path.isfile("test-data")
    通过这个方法，如果文件”test-data”不存在将返回False，反之返回True。

    即是文件存在，你可能还需要判断文件是否可进行读写操作。

参考链接：
    https://www.cnblogs.com/jhao/p/7243043.html






import subprocess

s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
s.stdin.write(b"import sys\n")
s.stdin.write(b"print(sys.version)")
s.stdin.close()

out = s.stdout.read().decode("GBK")
s.stdout.close()
print(out)



s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
s.stdin.write(b"import sys\n")
s.stdin.write(b"print(sys.version)")
s.stdin.close()

out = s.stdout.read().decode("GBK")
s.stdout.close()
print(out)


"""
results
"""

"""
Python 3.6.5 (default, May 11 2018, 13:30:17) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
>>> s.stdin.write(b"import sys\n")
11
>>> s.stdin.write(b"print(sys.version)")
18
>>> s.stdin.close()
>>> out = s.stdout.read().decode("GBK")
>>> s.stdout.close()
>>> print(out)
2.7.15 (default, May  1 2018, 05:55:50) 
[GCC 7.3.0]

>>> s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
>>> s.stdin.write(b"import sys\n")
11
>>> s.stdin.write(b"print(sys.version)")
18
>>> s.stdin.close()
>>> out = s.stdout.read().decode("GBK")
>>> s.stdout.close()
>>> print(out)
2.7.15 (default, May  1 2018, 05:55:50) 
[GCC 7.3.0]

>>> 
>>> import subprocess
>>> s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
>>> s.stdin.write(b"import sys\n")
11
>>> s.stdin.write(b"print(sys.version)")
18
>>> s.stdin.close()
>>> out = s.stdout.read().decode("GBK")
>>> s.stdout.close()
>>> print(out)
2.7.15 (default, May  1 2018, 05:55:50) 
[GCC 7.3.0]

>>> s = subprocess.Popen("python", stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
>>> s.stdin.write(b"import sys\n")
11
>>> s.stdin.write(b"print(sys.version)")
18
>>> s.stdin.close()
>>> out = s.stdout.read().decode("GBK")
>>> s.stdout.close()
>>> print(out)
2.7.15 (default, May  1 2018, 05:55:50) 
[GCC 7.3.0]

>>> 
>>> 
"""
    