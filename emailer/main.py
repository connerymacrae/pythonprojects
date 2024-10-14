import smtplib
import datetime as dt
from random import choice

with open("quotes.txt", 'r') as quotes_file:
    quotes_list = quotes_file.readlines()

today_quote = choice(quotes_list)

now = dt.datetime.now()

my_email = "crypticactuarial@gmail.com"
password = 'dtnhrafldzsivkhu'

# use this format to keep from needing to use connection.close()
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    # email security layer
    connection.starttls()
    connection.login(user=my_email, password=password)
    if now.weekday() == 4:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ellingw4@yahoo.com",
            msg=f"Subject:Weekly Inspiration\n\n{today_quote}"
        )

# connection.close()


