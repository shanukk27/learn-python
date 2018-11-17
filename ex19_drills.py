from sys import argv
from os.path import exists

def car_type(manufacturer, make):
    print(f"Your car manufacturer is {manufacturer} and the car make is {make}")

script, manufacturer, make = argv
car_type(manufacturer, make)

print("Is that the one being used by most of the people in 2018?")
car_type("Mercedes","Benz")

car_type("Mercedes" + "Benz", "A8")

car_type(len("Mercedes"), "Benz")

from_file = "test.txt"
to_file = "text.txt"
car_type(exists(from_file), exists(to_file))
