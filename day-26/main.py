import pandas


nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alpha_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}


def nato_translate():
    word = input("What word would you like to translate?: ")
    try:
        translation = [nato_alpha_dict[letter.upper()] for letter in word]
    except KeyError:
        print("please use letters, ONLY.")
        nato_translate()
    else:
        print(translation)


nato_translate()
