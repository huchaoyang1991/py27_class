# 1、输出
#print("hello python")
# 2、输入
#name = input("请输入你的名字:")
# 3、获取用户输入的内容
#print(name)
# 4、变量
"""
变量的命名规范
1、可以由数字、字母、下划线组合，不能使用数字开头
2、不能使用python的关键字
注解：关键字：python中内置的一些特有功能的单词（35）
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

查看python的关键字：
import keyword

3、变量命名尽量做到见名知意
比如：name、age、gender(不推荐拼音)

变量的命名风格
第一种：下划线命名法（推荐）：如果变量有多个单词组成，单词和单词之间使用下划线
age_max age_min

第二种：小驼峰命名法
ageMax  ageMin

第三种：大驼峰命名法
AgeMax  AgeMin

扩展：常量命名：纯大写字母

标识符：变量、函数名、类名、文件名、
"""
import keyword
print(keyword.kwlist)
input()
prints=1
