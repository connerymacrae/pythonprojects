##################### Extra Hard Starting Project ######################

# 1. Update the contacts.csv

# 2. Check if today matches a birthday in the contacts.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from contacts.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import smtplib
import random

letter_library = [
    "./letter_templates/letter_1.txt",
    "./letter_templates/letter_2.txt",
    "./letter_templates/letter_3.txt"
]

now = dt.datetime.now()

data = pandas.read_csv('contacts.csv')
contacts_dict = data.to_dict(orient="records")
is_birthday = False
# birthdays_today = {}

for x in range(len(contacts_dict)):
    if contacts_dict[x]["month"] == now.month and contacts_dict[x]['day'] == now.day:
        birthdays_today = (contacts_dict[x])

        with open(f'{random.choice(letter_library)}') as letter_file:
            letter_text = letter_file.read()
            addressed_letter = letter_text.replace("[NAME]", birthdays_today['name'])

            my_email = "crypticactuarial@gmail.com"
            password = 'dtnhrafldzsivkhu'

            # use this format to keep from needing to use connection.close()
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                # email security layer
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                        from_addr=my_email,
                        to_addrs=f"{birthdays_today['email']}",
                        msg=f"Subject:Happy Birthday, {birthdays_today['name']}!\n\n{addressed_letter}"
                )
