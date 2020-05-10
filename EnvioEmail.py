import smtplib

email_from = "email_remetente_@gmail.com"
email_to = "email_destinatario_@gmail.com"

smtp = "smtp.gmail.com"

server = smtplib.SMTP(smtp, 587)
server.starttls()
server.login(email_from, open('pass.txt').read().strip())

msg = "Text"
server.sendmail(email_from, email_to, msg)

server.quit()
print("Sucesso ao enviar o email")
