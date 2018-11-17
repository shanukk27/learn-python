#From sys module import argv argument variable
from sys import argv

#Unpack script and filname using argv variable to two other variables namely script and filename
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL+C (^C).")
print("If you want that, hit RETURN.")

#Prompt for user input
input("?")

print("Opening the file...")

#Open the file for writing and assign it to a variable named target. This will only assign the content to the variable.
target = open(filename, 'w')

print("Truncating the file. Good bye!")
#Truncate the contents of the entire file using the target variable.
target.truncate()

print("Now, I'm going to ask you to enter three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file.")

#Using the target variable, write some contents onto the file. Remember that write function only takes a  single argument
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
#Close the file. Like File -> Save
target.close()
