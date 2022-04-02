from smtplib import SMTP
from email.message import EmailMessage

def enviarEmail(correo, link):
    msg = EmailMessage()
    msg.set_content('Para confirmar su usuario ingrese al siguiente link.{}'.format(link))

    msg['Subject'] = 'Confirmación de correo'
    msg['From'] = "davidvivas2020@itp.edu.co"
    msg['To'] = correo

    username = 'davidvivas2020@itp.edu.co'
    password = '1085340013'

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)

    server.quit()

def emailBienvenida(correo):
    msg = EmailMessage()
    msg.set_content('Su cuenta ha sido confirmada exitosamente')

    msg['Subject'] = 'Bienvenido'
    msg['From'] = "davidvivas2020@itp.edu.co"
    msg['To'] = correo

    username = 'davidvivas2020@itp.edu.co'
    password = '1085340013'

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)

    server.quit()