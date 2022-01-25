import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, receiver_address, subject, message):
        self.receiver_address = receiver_address
        self.sender_address = "ariahmackie@gmail.com"
        self.subject = subject
        self.message = message
        self.setup_mail()

    def setup_mail(self):
        self.setup_mime()
        self.create_smtp_session()

    def setup_mime(self):
        self.mime = MIMEMultipart()
        self.mime['From'] = self.sender_address
        self.password = "Icandoit!"
        self.mime['To'] = self.receiver_address
        self.mime['Subject'] = self.subject
        self.mime.attach(MIMEText(self.message, 'plain'))

    def create_smtp_session(self):
        self.session = smtplib.SMTP('smtp.gmail.com', 587)
        self.session.starttls()
        self.session.login(self.sender_address, self.password)
        self.text = self.mime.as_string()

    def send(self):
        self.session.sendmail(self.sender_address, self.receiver_address, self.text)
        self.session.quit()
        print("sent email")
