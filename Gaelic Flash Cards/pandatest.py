import pandas
import random

# if words_to_learn does not exist:
# read from gaelic_flash
# if check mark is clicked do n ot add word to words_to_learn
# if x  mark is pressed, add word to words_to_learn
# create file word_to_learn, add current card to file

data = pandas.read_csv('data/short_sheet.csv')

language_dict = data.to_dict(orient="records")

# try:
#     data = pandas.read_csv('data/words_to_learn.csv')
# except FileNotFoundError:
#     data = pandas.read_csv('data/short_sheet.csv.csv')
# finally:
#     language_dict = data.to_dict(orient="records")

current_card = language_dict[0]

language_dict.remove(current_card)


print(language_dict)







