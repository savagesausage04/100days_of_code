account_sid = "AC47cefb54da23e053f6131749d8e567ae"
auth_token = "764edbf047cafd5a70adf53756b8be77"
from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):

        message = self.client.messages \
            .create(
            body=message,
            from_='+18456608440',
            to='9494008938'
        )

        print(message.sid)