import pandas as pd
import win32com.client

def convertToHtml(result,title):
    #将数据转换为html的table
    #result是list[list1,list2]这样的结构
    #title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h
result = [[u'2016-08-25',u'2016-08-26',u'2016-08-27'],[u'张三',u'李四',u'王二']]
title = [u'日期',u'姓名']
# convertToHtml(result,title)
# print(convertToHtml(result,title))


outlook = win32com.client.Dispatch("Outlook.Application")
# 创建一个邮件对象
mail = outlook.CreateItem(0)
# 对邮件的各个属性进行赋值
mail.To = '553706361@qq.com;1047743906@qq.com'
# mail.Cc = '1047743906@qq.com'
mail.Subject = "windows定时任务"
mail.HTMLBody = convertToHtml(result,title)
# mail.Attachments.Add("附件绝对路径")
# 添加多个附件
# mail.Attachments.Add("附件1绝对路径")

# 邮件发送
mail.Send()
print('success')