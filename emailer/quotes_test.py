from random import choice


with open("quotes.txt", 'r') as quotes_file:
    quotes_list = quotes_file.readlines()

today_quote = choice(quotes_list)
print(today_quote)
