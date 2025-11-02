import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

useful_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def game_start():

    response = str(input("What's a word you want to spell? "))

    word_list = list(response)
    use_list = [letter.upper() for letter in word_list]
    return_list = [useful_dict[letter] for letter in use_list]

    print(return_list)


game_is_on = True

while game_is_on:

    game_start()

    check = input("Would you like to check a new word? [yes or no]")
    if check == "yes":
        game_is_on = True
    else:
        game_is_on = False
