import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user ="achillegaglo@gmail.com"
    password = "Achille12$"

    server = smtplib.smtp("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)

    server.quit()


if __name__ == '__main__':
    email_alert ("Hey","Hello World",)
