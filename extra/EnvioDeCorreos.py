import smtplib
from email.message import EmailMessage
import stdiomask
import tkinter

def EDC():
    rem_email_address = input("Ingresar tu usuario: ")
    # hidden = Password(prompt="Ingresar contraseña: ", hidden="*")
    hiddenPassword = stdiomask.getpass(prompt="Ingresar contraseña: ", mask='*')
    email_smtp = "smtp.gmail.com"
    # puerto smtp
    server = smtplib.SMTP(email_smtp, '587')
    server.ehlo()
    server.starttls()


    # logear cuenta
    try:

        server.login(rem_email_address, hiddenPassword)
        print("Su acceso a su cuenta ha sido satisfactoria")
    except:
        print("No se ha podido acceder a su cuenta")
        exit()

    # passwordHidden = hidden.launch()
    # email_password = getpass.getpass('Ingresar contraseña: ')
    dest_email_address = input("Ingresar el destinatario: ")
    email_asunto = input("Ingrear el asunto del correo: ")
    email_mensaje = input("Ingresar el cuerpo del mensaje: \n")

    print("----------------------------------")
    message = EmailMessage()

    message['Subject'] = email_asunto
    message['From'] = rem_email_address
    message['To'] = dest_email_address

    # cuerpo del mensaje
    message.set_content(email_mensaje)



    # mandar email
    try:
        server.send_message(message)
        print("Su correo fue enviado exitosamente")

    except:

        print("Hubo un error al enviar el correo")
    # finalizar coneccion con el servidor de smtp

    server.quit()