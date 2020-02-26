"""
============================
Author:柠檬班-木森
Time:2020/2/25   21:54
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
linux命令                os模块中的方法
pwd：                      os.getcwd()
cd                         os.chdir()
ls                         os.listdir()
mkdir                      os.mkdir()
rmdir                      os.rmdir()
"""
import os

# 获取当前的工作路径
# print(os.getcwd())

# 切换路径
# os.chdir("..")
# print(os.getcwd())

# 获取当前工作路径下的文件和文件夹信息
# print(os.listdir("."))

# os.mkdir("test01")

# os.rmdir("test01")

# 判断给定的路径是否是文件
# res= os.path.isfile(r"C:\project\py27_class\py27_04day\01序列类型数据的切片操作（进阶）.py")
# print(res)
# 判断给定的路径是否是文件夹路径
# res= os.path.isdir(r"C:\project\py27_class\py27_04day")
# print(res)
