from sys import argv # From the sys module import the argv object used to get arguments from command line

script, filename = argv # Here we are breaking the arguments, the script name ex15.py to script variable and the file name ex15_sample.txt to filename variable.

txt = open(filename, 'r') # Here, we are opening the filename and assigning it to the variable txt

print(f"Here's your file {filename}: ")
print(txt.read())
txt.close()

print("Now, we are appending the file")
txt = open(filename, 'r+')
txt.seek(0, 0)
txt.write("Understood!")
txt.close()

txt = open(filename, 'r')
print(f"Here's the updated {filename}: \n")
print(txt.read())
txt.close()

# print("Type the filename again: ")
# file_again = input("> ") # Asking for the file name again
#
# txt_again = open(file_again) # Opening the file and assigning it to variable  txt_again
#
# print (txt_again.read()) # Reads the content of file and prints it
#
# txt_again.close()
