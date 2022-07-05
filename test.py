
"""
import xlwings as xw
#  = xw.Book('/Users/jerry/Desktop/python_excel')
wb = xw.Book() # 创建一个Excel进程App, 并在App中新建一个Book,Book下自动创建一个Sheet
wb.save('/Users/jerry/Desktop/python_excel/new5.xlsx')
wb.close()
"""
from re import A


def hello_func(a,b):
    print("hello world")
    c = a+b
    print(a+b)
    return c

# hello_func(1,3)
a = hello_func(1,3)
# print(a)



