from twilio.rest import Client
TWILIO_SID = "AC141cc63df051ac3ce413e912636d7fb8"
TWILIO_AUTH_TOKEN = "f35e95c3ba288dfa56fb651a1860b93a"
TWILIO_VIRTUAL_NUMBER = "+12182824624"
TWILIO_VERIFIED_NUMBER = "+14372466748"
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)