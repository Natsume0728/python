import win32com.client
# from datetime import datetime
from datetime import datetime

fullTime = datetime.now()
# time = datetime.time()
today = datetime.date.today()
print(today)
# print(fullTime.date())
# print(fullTime.time())
# # 获取年
# print(today.year)
# # 获取月
# print(today.month)
# # 获取日
# print(today.day)
# # 获取星期几，0-6代表周一到周天
# print(today.weekday())
# # 获取星期几，1-7代表周一到周天
# print(today.isoweekday())

# outlook = win32com.client.Dispatch("Outlook.Application")
# # 创建一个邮件对象
# mail = outlook.CreateItem(0)
# # 对邮件的各个属性进行赋值
# mail.To = '553706361@qq.com;1047743906@qq.com'
# # mail.Cc = '1047743906@qq.com'
# mail.Subject = "windows定时任务"
# mail.Body = "邮件正文win32"
# # mail.Attachments.Add("附件绝对路径")
# # 添加多个附件
# # mail.Attachments.Add("附件1绝对路径")

# # 邮件发送
# mail.Send()
# print('success')