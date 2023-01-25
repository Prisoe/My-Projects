from twilio.rest import Client
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_message(self, message):
        account_sid = "ACd433d5f9ca80db05553dd231bac21d6b"
        auth_token = "1c32a92a85c2dd67c27138fe0bc01fc1"
        twilio_phone = "+16722021137"
        verified_phone = "14379952977"

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_phone,
            to=verified_phone
        )
        print(message.status)


    def send_email(self, user_email, message):
        my_email = "prosperalabi@outlook.com"
        password = "Probol@26"
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in user_email:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=message
                )

