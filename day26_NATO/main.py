import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def make_phonetic():

    user_word = input("Enter a word: ").upper()
    try:
        code_list = [phonetics_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        make_phonetic()
    else:
        print(code_list)


make_phonetic()

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}