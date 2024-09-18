"""
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

{new_key:new_value for (key, value) in dict.items()}
{new_key:new_value for (index, row) in data_frame.iterrows()}
"""

#TODO 1. Create dictionary in format: {"A": "Alpha", "B": "Bravo", "C":"Connery", ...}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs

import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# print(nato_alpha_dict)


# word_choice = input("What word would you like translate?")
translation = [nato_alpha_dict[letter.upper()] for letter in input("What word would you like translate?")]
# for letter in word_choice:
#     translation.append(nato_alpha_dict[letter.upper()])

print(translation)

#
# for letter in word_choice:
#     translation = []
#     if letter == nato_alpha_dict[]:
# for letter in input("What word do you need to translate?"):
# translation = [value for (key, value) in nato_alpha_dict.items() if key == letter in word_choice]
#
# print(translation)
