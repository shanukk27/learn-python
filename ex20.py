#From the sys module import argv identifier
from sys import argv

#Assign two variables script andn input_file to the aguments
script, input_file = argv

# Here, we define a function print_all() with a single argument. On the next line, we read the file
def print_all(f):
    print(f.read())

# We define a function rewind() to seek to the zeroeth position of the file we might have opened
def rewind(f):
    f.seek(0)

#We define a function to print the line number and print each lines from start starting with line 1 since we have already seeked to zeroeth position
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

#Open the file input_file which we inputted through command line and assign the file descriptor to current_file
current_file = open(input_file)
print("First, let's print the whole file:\n")

#Run function print_all
print_all(current_file)

print("Now, let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
