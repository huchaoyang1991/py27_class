"""
============================
Author:柠檬班-木森
Time:2020/3/12   20:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import openpyxl


wb = openpyxl.load_workbook(r"C:\project\py27_class\py27_16day\demo2\cases.xlsx")

sh = wb.get_sheet_by_name("register")

print(sh.cell(1,1).value)