from smtplib import SMTP 
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('Este es un mensaje de pruebas')

msg['Subject'] = 'Asunto de prueba'
msg['From'] = "davidvivas2020@itp.edu.co"
msg['To'] = "davidvivas2020@itp.edu.co"

username = 'davidvivas2020@itp.edu.co'
password = '1085340013'

server = SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.send_message(msg)

server.quit()

 