import pandas


alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

def generate_phonetic():
    user_input = input("Enter a word: ").upper()

    try:
        code_words = [nato_alphabet[char] for char in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_words)


generate_phonetic()