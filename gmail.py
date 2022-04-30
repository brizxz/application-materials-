import email.message 
#準備設定
msg=email.message.EmailMessage()
msg["From"]="yussp8787@gmail.com" #寄件人
msg["To"]="yussp6969@gmail.com" #收件人
msg["Subject"]="早啊" #主題
#msg.set_content("haha") #文字檔
msg.add_alternative("<h3>==</h3>幫我買飲料", subtype="html") #html格式
import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com", 465) #gmail smtp server
server.login("yussp8787@gmail.com","a14831086") #登錄
server.send_message(msg) #寄出
server.close() #關閉