import xlrd
from datetime import datetime, date
import win32com.client

data = []
path = r'E:\tableWebDir\outlook\mission.xlsx'
mailBody = ''

def read_xsls(xlsx_path):
    data_xsls = xlrd.open_workbook(xlsx_path) #打开此地址下的exl文档
    sheet_name = data_xsls.sheets()[0]  #进入第一张表
    count_nrows = sheet_name.nrows  #获取总行数
    # count_nocls = sheet_name.ncols  #获得总列数
    # line_value = sheet_name.row_values(0)
    for i in range(1, count_nrows):
        rowDate = datetime.date(xlrd.xldate.xldate_as_datetime(sheet_name.cell(i, 0).value, 0))
        if rowDate == date.today():
            global mailBody
            mailBody += sheet_name.cell(i, 2).value
read_xsls(path)

outlook = win32com.client.Dispatch("Outlook.Application")
# 创建一个邮件对象
mail = outlook.CreateItem(0)
# 对邮件的各个属性进行赋值
mail.To = '553706361@qq.com;1047743906@qq.com'
mail.Cc = '1047743906@qq.com'
mail.Subject = "windows定时任务"
mail.Body = mailBody
# mail.Attachments.Add("附件绝对路径")
# 添加多个附件
# mail.Attachments.Add("附件1绝对路径")

# 邮件发送
mail.Send()
print(mailBody, 'success')


