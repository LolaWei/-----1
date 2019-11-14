import xlwt as x
import os
import json
def read_file(path):  #先读出来，然后放在一个字典中
    d={}
    with open(path) as f:
        d=json.loads(f.read())  #把字符串转换为字典
        #print(type(d)) 测试d的类型 type(d)=dict
        #print(type(f.read()))  测试f.read()的类型 type(f.read)=string
        return d

def write_in_excel(d):
    workbook=x.Workbook(encoding="utf-8")  #创建一个excel文件
    worksheet=workbook.add_sheet("StuInfo")  #创建一个工作表
    row=0
    for k in d.keys():                       #遍历字典的键
        col=0
        worksheet.write(row,col,k)
        for i in d[k]:                            #遍历字典的值（因为字典的值是一个列表）
            col += 1
            worksheet.write(row,col,i)
        row+=1
    workbook.save("excel_write_in.xls")

if __name__=="__main__":
    d=read_file(r"C:\Users\hp\Desktop\student.txt")
    write_in_excel(d)


