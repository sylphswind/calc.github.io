import math
import html

print("Hello")

index = ["A for adding", "D for Dividing", "M for Multiplying", "S for substracing", "For advanced type (random)"]

print(index, ": Please enter the function you want capitalized")

a = input("Enter function here: ")

if a == "A":
    val1 = int(input("Enter value of the first number: "))
    val2 = int(input("Enter value of second number:" ))
    print(val1 + val2)

elif a == "M":
    val1 = int(input("Enter value of the first number: "))
    val2 = int(input("Enter value of second number:" ))
    print(val1 * val2)

elif a == "D":
    val1 = int(input("Enter value of the first number: "))
    val2 = int(input("Enter value of second number:" ))
    print(val1/val2)

elif a == "S":
    val1 = int(input("Enter value of the first number: "))
    val2 = int(input("Enter value of second number:" ))
    print(val1 - val2)

elif a == "random":
    ad_index = ["Sq for square root", "E for exponentation"]
    ad = input("Enter function: ")
    if ad == "Sq":
        val1 = int(input("Enter value of the number: "))
        print(math.sqrt(val1))
    elif ad == "E":
        val1 = int(input("Enter value of the first number: "))
        print(math.exp(val1))


