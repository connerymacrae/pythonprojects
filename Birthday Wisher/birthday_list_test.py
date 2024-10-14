import pandas
import datetime as dt

now = dt.datetime.now()
data = pandas.read_csv('contacts.csv')

contacts_dict = data.to_dict(orient="records")

for x in range(len(contacts_dict)):
    if contacts_dict[x]["month"] == now.month and contacts_dict[x]['day'] == now.day:
        print(contacts_dict[x])




