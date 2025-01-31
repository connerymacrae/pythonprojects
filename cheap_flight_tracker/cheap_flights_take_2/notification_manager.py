import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
from datetime import datetime

load_dotenv()

class NotificationManager:

    def __init__(self, sheet_data, flight_data):
        self.account_sid = os.getenv("TWIL_ACCT_SID")
        self.auth_token = os.getenv("TWIL_AUTH_TOKEN")
        self.sheet_data = sheet_data
        self.flight_data = flight_data

    def format_date(self, date):
        form_date = datetime.strptime(date, '%Y-%m-%d')
        simp_date = form_date.strftime('%b %d')
        return simp_date

    def create_message(self):
        for num in range(len(self.flight_data)):
            if self.flight_data[num]['price']<self.sheet_data[num]['pricePoint']:
                date = self.format_date(self.flight_data[num]['dept_date'])
                message = (f"Low Price Found! Flights from {self.flight_data[num]['itinerary']} "
                           f"starting on {date} "
                           f"are only {self.flight_data[num]['price']}!")
                self.cheap_flight_notification(message)

    def cheap_flight_notification(self, cheap_flight):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            from_=os.getenv("TWIL_SENDER"),
            body=cheap_flight,
            to=os.getenv("TWIL_RECEIVER")
        )
        print(message.status)


