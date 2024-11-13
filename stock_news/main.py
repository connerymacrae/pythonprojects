import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from math import floor, ceil

load_dotenv()

STOCK_Endpoint = "https://www.alphavantage.co/query?"

stock_api_key = os.getenv("STOCK_API_KEY")
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "BITX",
    "apikey" : stock_api_key,
}

News_Endpoint = "https://newsapi.org/v2/everything?"
news_api_key = os.getenv("NEWS_API_KEY")
news_params = {
    "q" : "BITX",
    "apiKey" : news_api_key,
}

account_sid = os.getenv("TWIL_ACCT_SID")
auth_token = os.getenv("TWIL_AUTH_TOKEN")


stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey={stock_api_key}'
stock_info = requests.get(STOCK_Endpoint, params=stock_params)
stock_info.raise_for_status()
stock_data = stock_info.json()
print(stock_data)


d1 = list(stock_data["Time Series (Daily)"].keys())[0]
d2 = list(stock_data["Time Series (Daily)"].keys())[1]


d1_close = float(stock_data["Time Series (Daily)"][d1]["4. close"])
d2_close = float(stock_data["Time Series (Daily)"][d2]["4. close"])

percent_diff = (d1_close-d2_close)/((d1_close+d2_close)/2)*100
#
# percent_diff = -7
#
print(d1_close, d2_close, percent_diff)
if abs(percent_diff) >= 5:

    news_info = requests.get(News_Endpoint, params=news_params)
    news_info.raise_for_status()
    news_data = news_info.json()

    article = news_data["articles"][0]["title"]
    if percent_diff > 0:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"{stock_params["symbol"]} UP by {floor(percent_diff)}% 🔺\n{article}",
            to="whatsapp:+17735805744",
        )
        # print(f"{stock_params["symbol"]} UP by {percent_diff}% 🔺\n{article}")
    else:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"{stock_params["symbol"]} DOWN by {ceil(percent_diff)}% 🔻\n{article}",
            to="whatsapp:+17735805744",
        )
        # print(f"{stock_params["symbol"]} DOWN by {percent_diff}% 🔻\n{article}")