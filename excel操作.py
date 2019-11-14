import xlwt as x
#创建一个workbook工作表
workbook=x.Workbook(encoding="utf-8")
#创建一个worksheet
worksheet=workbook.add_sheet("第一个sheet")
'''
style=x.XFStyle() #初始化样式
font=x.Font() #为样式创建字体
font.name="Times New Roman"
font.bold=True #黑体
font.underline=True# 带有下划线
font.italic=True #斜体
style.font=font
#写入excel
#写入行、列、值
worksheet.write(0,0,"unformatted value") #不带样式的写入
worksheet.write(1,0,"Formated value",style) #带样式的写入
#设置单元格的宽度
worksheet.col(0).width=5000
'''
#向单元格添加公式
worksheet.write(0,0,5) #填写数字5
worksheet.write(0,1,2)#填写数字2
worksheet.write(1,0,x.Formula("A1*B1")) #填入公式
worksheet.write(1,1,x.Formula("SUM(A1,B1)")) #计算该区域相加的和
workbook.save("excel_test.xls")

