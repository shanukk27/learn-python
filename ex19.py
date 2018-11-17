# Here, we are defining a function named cheese_and_crackers()  with cheese_count and boxes_of_crackers as the argument variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #Here, are the contents of that funtion in the next four lines
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
#Call the function with arguments as numerals
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#Call the function with arguments as two variables amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese,  amount_of_crackers)


print("We can even do math inside too: ")
#Call the function cheese_and_crackers with arguments as a sum
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
#Call the function cheese_and_crackers as a sum of a variable and numeral
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)


cheese_and_crackers(input("Now, please type the number of cheese"), input("and the number of crackers?"))
