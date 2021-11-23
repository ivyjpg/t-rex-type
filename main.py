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

score = 0
user = input("enter your name: ")
print("welcome, " + user + ".")

to_do = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
random.shuffle(to_do)

print("LEVEL 1")
for letter in to_do:

    if score >= 7:
        print("looks like you're getting the hang of this! \ntime to move on to the next level.")
        break

    combos = letters[letter]
    selected = random.choice(combos)
    print(letter)
    user_type = input("type the following: " + selected + "\n")

    if (user_type == selected):
        print("correct!")
        score += 1
        print("score: " + str(score))
    else:
        while (user_type != selected):
            print("sorry, try again")
            user_type = input(selected + "\n")
        print("score: " + str(score))



print("LEVEL 2")
