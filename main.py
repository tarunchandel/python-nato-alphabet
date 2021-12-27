import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input("Enter your name: ").upper()
output = [alpha_dict[alpha] for alpha in user_input]
print(output)
