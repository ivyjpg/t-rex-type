# https://docs.google.com/presentation/d/1KMRDk3jHZ7PLFFtZnoVRZgwl_YT4tqTmfaJgYK2N32Q/edit#slide=id.gfcce4bbe6c_0_797

import random

letters = {"A": ["waz wsx as", "esx edc sd", "rdc rfv df", "tfv tgb fg", "ygb yhn gh", "uhn ujm hj"],
           "B": ["wsz wedsdxz", "edx erfdfcx", "rfc rtgfgvc", "tgv tyhghbv", "yhb yujhjnb", "ujn uikjkmn"],
           "C": ["ewazx", "resxc", "trdcv", "ytfvb", "uygbn", "iuhnm"],
           "D": ["wsz wedxz", "edx erfcx", "rfc rtgvc", "tgv tyhbv", "yhb yujnb", "ujn uikmn"],
           "E": ["wsz we sd zx", "edx er df xc", "rfc rt fg cv", "tgv ty gh vb", "yhb yu hj bn", "ujn ui jk nm"],
           "F": ["wsz we sd", "edx er df", "rfc rt fg", "tgv ty gh", "yhb yu hj", "ujn ui jk"],
           "G": ["ewazxds", "resxcfd", "trdcvgf", "ytfvbhg", "uygbnjh", "iuhnmkj"],
           "H": ["waz asd edx", "esx sdf rfc", "rdc dfg tgv", "tfv fgh yhb", "ygb ghj ujn", "uhn hjk ikm"],
           "I": ["wsz", "edx", "rfc", "tgv", "yhb", "ujn"],
           "J": ["edxz", "rfcs", "tgvc", "yhbv", "ujnb", "ikmn"],
           "K": ["waz esa asx", "esx rds sdc", "rdc tfd dfv", "tfv ygf fgb", "ygb uhg ghn", "uhn ijh hjm"],
           "L": ["wszx", "edxc", "rfcv", "tgvb", "yhbn", "ujnm"],
           "M": ["waz wsedx", "esx edrfc", "rdc rftgv", "tfv tgyhb", "ygb yhujn", "uhn ujikm"],
           "N": ["waz wsxde", "esx edcfr", "rdc rfvgt", "tfv tgbhy", "ygb yhnju", "uhn ujmki"],
           "O": ["wazxdew", "esxcfre", "rdcvgtr", "tfvbhyt", "ygbnjuy", "uhnmkiu"],
           "P": ["wsz weds", "edx erfd", "rfc rtgf", "tgv tyhg", "yhb yujh", "ujn uikj"],
           "Q": ["wazxdew sc", "esxcfre dv", "rdcvgtr fb", "tfvbhyt gn", "ygbnjuy hm", "uhnmkiu j,"],
           "R": ["wsz wedsx", "edx erfdc", "rfc rtgfv", "tgv tyhgb", "yhb yujhn", "ujn uikjm"],
           "S": ["ewasdxz", "resdfcx" ,"trdfgvc", "ytfghbv", "uyghjnb", "iuhjkmn"],
           "T": ["qwe wsz", "wer edx", "ert rfc", "rty tgv", "tyu yhb", "yui ujn"],
           "U": ["wazxde", "esxcfr", "rdcvgt", "tfvbhy", "ygbnju", "uhnmki"],
           "V": ["wazse", "esxdr", "rdcft", "tfvgy", "ygbhu", "uhnji"],
           "W": ["wazsxde", "esxdcfr", "rdcfvgt", "tfvgbhy", "ygbhnju", "uhnjmki"],
           "X": ["wsx esz", "edc rdx", "rfv tfc", "tgb ygv", "yhn uhb", "ujm ijn"],
           "Y": ["wsd edxz", "edf rfcx", "rfg tgvc", "tgh yhbv", "yhj ujnb", "ujk ikmn"],
           "Z": ["weszx", "erdxc", "rtfcv", "tygvb", "yuhbn", "uijnm"]}

words = ["is", "was", "are", "be", "have", "had", "were", "can", "said", "use", "do", "will", "would", 
         "make", "like", "has", "look", "write", "go", "see", "could", "been", "call", "am", "find",
         "word", "time", "number", "way", "people", "water", "day",	"part",	"sound", "work", "place", 
         "year", "back", "thing", "name", "sentence", "man", "line", "boy",	"farm", "end", "men", "land", 
         "home", "hand"]

score = 0
user = input("enter your name: ")
print("welcome, " + user + ".\n")

to_do = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
random.shuffle(to_do)

print("LEVEL 1")
for letter in to_do:

    if score >= 0:
        print("looks like you're getting the hang of this! \ntime to move on to the next level.\n")
        break

    combos = letters[letter]
    selected = random.choice(combos)
    print(letter)
    user_type = input("type the following: " + selected + "\n")

    if (user_type == selected):
        print("correct!")
        score += 1
        print("score: " + str(score) + "\n")
    else:
        while (user_type != selected):
            print("sorry, try again")
            user_type = input(selected + "\n")
        print("score: " + str(score) + "\n")



print("LEVEL 2")
correct_flag = True
score = 0
random.shuffle(words)

print("rules: for each word, input one letter per line.\n")
for word in words:
    if score >= 3:
        print("congrats! you've passed the level!")
        break

    num_lines = len(word)
    print("type the following: " + word + "\n")
    user_type = ""

    for i in range(num_lines):
        letter = word[i]
        combos = letters[letter.upper()]
        selected = random.choice(combos)
        user_type = input(letter + ": " + selected + "\n")
        while (user_type != selected):
            correct_flag = False
            print("incorrect, try again: ")
            user_type = input()

    if correct_flag:
        score += 1
    print("score: " + str(score) + "\n")
    correct_flag = True


print("LEVEL 3")
score = 0
random.shuffle(words)

print("rules: for each word, input one letter per line.\n")
for word in words:

    if score >= 5:
        print("congrats! you've passed the level!")
        break

    num_lines = len(word)
    print("type the following: " + word + "\n")
    user_type = ""
    for i in range(num_lines):
        user_type += input() + "\n"
    
    user_type = user_type.split("\n")
    correct_flag = True

    for j in range(len(user_type)-1):
        cap_letter = word[j].upper()
        if user_type[j] in letters[cap_letter]:
            pass
        else:
            correct_flag = False
    
    if correct_flag:
        score += 1
        print("correct! score: " + str(score) + "\n")
    else:
        print("incorrect! score: " + str(score) + "\n")