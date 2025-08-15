from twilio.rest import Client
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

class NotificationManager:

    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.getenv('TWILIO_VIRTUAL_NUMBER'),
            to=os.getenv('TWILIO_VERIFIED_NUMBER'),
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, clients):
        print(f"All clinets: {clients}\nMessage: {message}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(os.getenv('MY_EMAIL'), os.getenv('MY_PASSWORD'))

            message = 'Subject: Flight deal\n\n' + message

            for client_email in clients:
                connection.sendmail(
                    from_addr=os.getenv('MY_EMAIL'),
                    to_addrs=client_email,
                    msg=message.encode('utf-8')
                )


