from sys import argv

script, filename = argv

target = open(filename, 'r')

print(f"We're going to print the contents of the file {filename}: \n-----------------")
print(target.read())
print("-----------------")

target.close()
