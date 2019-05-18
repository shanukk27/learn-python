def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiple(a , b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a , b):
    return(f"Dividing {a} / {b}")
    return a / b


print("Let's do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiple(90, 2)
iq = divide(100, 2)

print(f"Age: {age} \n Height: {height} \n Weight: {weight} \n IQ: {iq}")


# A puzzle for extra credit, type it in anyway.
print("Here's the puzzle.")

what = add(age, subtract(height, multiple(weight, divide(iq, 2))))

print("That becomes", what, "\nCan you do it by hand?")
