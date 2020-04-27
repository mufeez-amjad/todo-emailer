import smtplib
from getpass import getpass
from .email import Email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER_ADDRESS = 'smtp-mail.outlook.com'
SMTP_SERVER_PORT = 587


class Emailer:
    def __init__(self):
        self.emails: [Email] = []
        self.email_address = ''
        self.password = ''

    def add_email(self, email: Email):
        self.emails.append(email)

    def connect_to_smtp(self):
        server = smtplib.SMTP(SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT)
        server.ehlo()
        server.starttls()
        server.login(self.email_address, self.password)
        return server

    def send_emails(self):
        if not self.email_address:
            print('No emails to send.')
            return
        try:
            server = self.connect_to_smtp()

            for email in self.emails:
                msg = MIMEMultipart()
                msg['From'] = f'ToDoEmailer <{self.email_address}>'
                msg['To'] = f'{self.email_address}>'
                msg['Subject'] = email.subject
                msg.attach(MIMEText(email.body, 'plain'))
                server.send_message(msg)

            server.quit()
            print('Successfully sent emails.')
        except Exception as e:
            print(e)
            # TODO: print/save emails to avoid having to re-enter details
