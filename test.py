import smtplib
from email.mime.text import MIMEText
 
mailserver = "smtp.qq.com"  #邮箱服务器地址
sender = '1047743906@qq.com'  #邮箱用户名
password = 'jfjccgievnfbbfbb'   #邮箱密码：需要使用授权码

to_reciver = ['1047743906@qq.com']  #收件人，多个收件人用逗号隔开
cc_reciver = ['553706361@qq.com']
reciver = to_reciver + cc_reciver
print(reciver)

mail = MIMEText('邮件内容')
mail['Subject'] = '邮件主题120'
mail['From'] = sender  #发件人
mail['To'] = ';'.join(to_reciver)
mail['Cc'] = ';'.join(cc_reciver)
print(mail['To'],mail)

# smtp = smtplib.SMTP(mailserver,port=995) # 连接邮箱服务器，smtp的端口号是25
smtp=smtplib.SMTP_SSL('smtp.qq.com',port=465) #QQ邮箱的服务器和端口号
smtp.login(sender, password)  #登录邮箱
smtp.sendmail(sender, reciver, mail.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
smtp.quit() # 发送完毕后退出smtp
print ('success')