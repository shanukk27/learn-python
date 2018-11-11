# From sys module import argv identifier
from sys import argv

#Assign all arguments for this script to two variables script and input_file
script, input_file = argv

#Define a function print_all() with a single argument and print that opened file
def print_all(f):
    print(f.read())

#Define a function rewind() to go to the start of the file.
def rewind(f):
    f.seek(0)

#Define a function print_a_line() to print the line number and that particular line
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Open the file and assign it to file object current_file
current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
