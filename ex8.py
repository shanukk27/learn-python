formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I have a family. \n",
    "It has Vapa, Umma, Shinu, Arif, Shynu and Reyah.",
    "And, I have some one special.",
    "It's my Nasri. I call her Nasriakaran."
))
