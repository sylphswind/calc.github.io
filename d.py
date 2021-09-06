import math

print("Hello")

index = ["A for adding", "D for Dividing", "M for Multiplying", "S for substracing", "For advanced type (random)"]

print(index)

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
    print(ad_index)
    ad = input("Enter function: ")

    if ad == "Sq":
        val1 = int(input("Enter value of the number: "))
        print(math.sqrt(val1))
    elif ad == "E":
        val1 = int(input("Enter value of the first number: "))
        print(math.exp(val1))

print("or else input shapes")

hauwa = [
    """Quad for Square or Rectangle,
    Tri for Triangle,
    circle for cirlce,
    trap for trapezoid
    """
]

print(hauwa)
yu = input("Input this: ")



if yu == "Quad":
    val1 = int(input("Enter value of the first number: "))
    val2 = int(input("Enter value of second number:" ))
    print(val1 * val2)
    
if yu == "Tri":
    val1 = int(input("Enter value of the base: "))
    val2 = int(input("Enter value of height:" ))
    print((val1 * val2)/2)

if yu == "cirlce":
    val1 = int(input("Enter value of radius: "))
    print(3.14 * math.exp(val1))

if yu == "trap":
    val1 = int(input("Enter value of the top: "))
    val2 = int(input("Enter value of base:" ))
    val3 = int(input("Enter value of height:" ))
    print(((val1 + val2)/2) * val3)

