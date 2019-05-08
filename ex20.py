#From sys module import argv variable
from sys import argv

#Assign the argument variable to two variables script which is the script name and input_file which is the file name to process
script, input_file = argv

#Define a function print_all() and read the file.
def print_all(f):
    print(f.read())

#Define a function rewind and seek to seek to the start of the file
def rewind(f):
    f.seek(0)

#Define a function 
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file")

print_all(current_file)

print("Now, let's rewind, kind of like a tape")

rewind(current_file)

print("Let's print three lines")

current_line =  1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file )

current_line = current_line + 1
print_a_line(current_line, current_file)
