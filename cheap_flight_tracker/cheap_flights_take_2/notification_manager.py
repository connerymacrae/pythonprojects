import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client
from datetime import datetime

load_dotenv()

class NotificationManager:

    def __init__(self, flight_data):
        self.client = Client(os.getenv("TWIL_ACCT_SID"), os.getenv("TWIL_AUTH_TOKEN") )
        # self.account_sid = os.getenv("TWIL_ACCT_SID")
        # self.auth_token = os.getenv("TWIL_AUTH_TOKEN")
        self.flight_data = flight_data

    def format_date(self, date):
        form_date = datetime.strptime(date, '%Y-%m-%d')
        simp_date = form_date.strftime('%b %d')
        return simp_date

    def send_message(self):
        for flight in self.flight_data:
            date = self.format_date(flight['dept_date'])
            message = self.client.messages.create(
                from_=os.getenv("TWIL_SENDER"),
                body=f"Low Price Found! Flights from {flight['itinerary']} "
                        f"starting on {date} "
                        f"are only {flight['price']}!",
                to=os.getenv("TWIL_RECEIVER")
            )
            print(message.status)

    # def cheap_flight_notification(self, cheap_flight):
    #     client = Client(self.account_sid, self.auth_token)
    #     message = client.messages.create(
    #         from_=os.getenv("TWIL_SENDER"),
    #         body=cheap_flight,
    #         to=os.getenv("TWIL_RECEIVER")
    #     )
    #     print(message.status)


