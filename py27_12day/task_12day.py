# 1、类属性怎么定义？ 实例属性怎么定义？
# 类属性：在类之后，方法之前定义
# 实例属性：在方法体中定义

# 2、实例方法中的self代表什么？（简答）
# 代表该类的对象，调用该方法自动传

# 3、类中__init__方法在什么时候会调用的？（简答）
# 初始化方法，每次创建对象会调用

# 4、定义一个登录的测试用例类LoginTestCase
# 登录url地址为："http://www.xxxx.com/login"
# 请求方法为："post"     、
# 请自行分辨下列属性，应该定义为类属性还是实例属性
# -  属性：用例编号
# url地址
# 请求参数
# 请求方法
# 预期结果
# 实际结果
class LoginTestCase:
    url = "http://www.xxxx.com/login"
    method = "post"

    def __init__(self, test_case_no, expecter_result, acutrl_result):
        self.test_case_no = test_case_no
        self.expected_result = expecter_result
        self.acturl_result = acutrl_result


# 5、封装一个学生类，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
#
# -  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
#
# -  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx, 性别：xxx。
class Student:
    identity = "学生"

    def __init__(self, name, age, sex, english_grade, math_grade, chinese_grade):
        self.name = name
        self.age = age
        self.sex = sex
        self.english_grade = int(english_grade)
        self.math_grade = int(math_grade)
        self.chinese_grade = int(chinese_grade)

    def total_grade(self):
        total = self.english_grade + self.math_grade + self.chinese_grade
        return total

    def avg_grade(self):
        avg = self.total_grade() / 3
        return int(avg)

    def student_info(self):
        print("我的名字叫{},年龄:{}，性别:{}".format(self.name, self.age, self.sex))


if __name__ == '__main__':
    student = Student(name="Mary", age=18, sex="女", english_grade=100, math_grade=80, chinese_grade=89)
    total_grade = student.total_grade()
    print(total_grade)
    avg_grade = student.avg_grade()
    print(avg_grade)
    student.student_info()
