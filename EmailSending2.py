import smtplib
from email.mime.text import MIMEText

sender_email = 'mockjoke0@gmail.com'
receiver_email = 'rockyharshit24@gmail.com'
sender_pass = 'tgjscfecslfpotax'   # app pass generated on gmail


def send_mail(temperature):
    message = MIMEText("Temperature is %0.2f degrees" % temperature)
    message['Subject'] = "%0.2f degrees" % temperature
    message['From'] = sender_email
    message['To'] = receiver_email
    print(message)

    # server = smtplib.SMTP('smtp.gmail.com', 587)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.starttls()    # tls is transport layer security
    server.login(sender_email, sender_pass)
    server.sendmail(sender_email, [receiver_email], message.as_string())
    server.quit()
    print('mail sent')


send_mail(7.7)
