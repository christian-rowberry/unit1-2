pi = 3.14159
userInput = str(input("Name > "))
print("User is: " + userInput + " ...")
# x = float(input("x > "))
# y = float(input("y > "))
# z = float(input("z > "))
while True:
    userInput2 = input("""Which Shape:
    cube
    rect
    cyl
    """)
    if userInput2 == "cube" or userInput2 == "Cube":
        x = float(input("x > "))
        y = float(input("y > "))
        z = float(input("z > "))
        print("Calculating Volume...")
        volume = x + y + z
        print("Volume: " + str(volume))
    elif userInput2 == "rect" or userInput2 == "Rect":
        x = float(input("x > "))
        y = float(input("y > "))
        z = float(input("z > "))
        print("Calculating Volume...")
        volume = x + y + z
        print("Volume: " + str(volume))
    elif userInput2 == "cyl" or userInput2 == "Cyl":
        rad = float(input("radius >"))
        y = float(input("y > "))
        print("Calculating Volume...")
        volume = y + (pi*(rad ^ 2))
        print("Volume: " + str(volume))
    else:
        break
