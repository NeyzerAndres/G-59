from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def envio_correo(asunto, correos, html):
    msg = MIMEMultipart()
    msg['From']     = ''
    msg['To']       = ", ".join(correos)
    msg['Subject']  = asunto
    msg.attach(MIMEText(html, 'html'))
    try:
        with smtplib.SMTP('smtp.office365.com',587) as server:
            server.starttls()
            server.login('', '')
            server.sendmail(msg['From'],correos, msg.as_string())
            print("Correo electrónico enviado exitosamente.")

    except Exception as e:
        print(f'Se ha presentando un error: {e}')





