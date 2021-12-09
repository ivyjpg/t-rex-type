# https://docs.google.com/presentation/d/1KMRDk3jHZ7PLFFtZnoVRZgwl_YT4tqTmfaJgYK2N32Q/edit#slide=id.gfcce4bbe6c_0_797

import random

letters = {"A": ["waz wsx as", "esx edc sd", "rdc rfv df", "tfv tgb fg", "ygb yhn gh", "uhn ujm hj"],
           "C": ["ewazx", "resxc", "trdcv", "ytfvb", "uygbn", "iuhnm"],
           "T": ["qwe wsz", "wer edx", "ert rfc", "rty tgv", "tyu yhb", "yui ujn"]}

user = input("Enter your name: ")
print("Welcome, " + user + ".\n")
print("For best results, play this game using only your pointer finger to type.\n")

to_do = ["A", "C", "T"]
random.shuffle(to_do)

print("LEVEL 1")
for letter in to_do:
    combos = letters[letter]
    selected = random.choice(combos)

    print("Let's type " + letter + " two ways.")
    user_type = input("First, type the following: " + selected + "\n")

    if (user_type == selected):
        print("Correct!\n")
    else:
        while (user_type != selected):
            print("Sorry, try again:")
            user_type = input(selected + "\n")

    selected2 = random.choice(combos)
    while selected2 == selected:
        selected2 = random.choice(combos)

    user_type = input("Now try typing " + letter + " another way: " + selected2 + "\n")
    if (user_type == selected2):
        print("Correct!\n")

    else:
        while (user_type != selected2):
            print("Sorry, try again:")
            user_type = input(selected2 + "\n")
    
    print("")


print("LEVEL 2")
correct_flag = True
score = 0
# random.shuffle(words)

print("Now we'll learn how to type words. For each word, we'll need to input one letter per line.\n")

word = "cat"
num_lines = len(word)
print("Type the following: " + word + "\n")
user_type = ""

for i in range(num_lines):
    letter = word[i]
    combos = letters[letter.upper()]
    selected = random.choice(combos)
    user_type = input(letter + ": " + selected + "\n")
    if (user_type == selected):
        print("Correct!\n")
    while (user_type != selected):
        correct_flag = False
        print("Incorrect, try again: ")
        user_type = input()

correct_flag = True

print("\nNice job!")

print("\nLEVEL 3")
print("Now try typing the word without any guidance!")
word = "cat"
num_lines = len(word)
print("Type the following: " + word + "\n")
user_type = ""
correct_flag = True

for i in range(num_lines):
    user_type = input()
    cap_letter = word[i].upper()
    if user_type in letters[cap_letter]:
        print("\nCorrect! You typed " + cap_letter.lower() + "\n")
    else:
        correct_flag = False
        while (user_type not in letters[cap_letter]):
          print("\nIncorrect, try again: ")
          user_type = input()
        print("Correct! You typed " + cap_letter.lower() + "\n")
        
print("\nNice job, you typed "+ word + "!")

# user_type = user_type.split("\n")


# for j in range(len(user_type)-1):
#     cap_letter = word[j].upper()
#     if user_type[j] in letters[cap_letter]:
#         print("\nCorrect! You typed " + cap_letter + "\n")
#     else:
#         correct_flag = False
#         print("\nIncorrect!\n")

# if correct_flag:
#     print("\nNice job, you typed "+ word + "!")