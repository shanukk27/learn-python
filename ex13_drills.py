from sys import argv

script, name1, name2 = argv

iname1 = input("What's is your name?")
iname2 = input("What's your spouse's name?")

print("You inputted your name",name1 == iname1,
"and that of your wife's", name2==iname2)
