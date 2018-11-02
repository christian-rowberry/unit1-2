name1 = input("User 1 ")
name2 = input("User 2 ")
name3 = input("User 3 ")
name4 = input("User 4 ")


while True:
    userIn = input("""
    Cont
    Exit

    (MUST BE EXACT)
    """)
    if userIn == "Cont":
        gpa1 = int(input("GPA 1 "))
        gpa2 = int(input("GPA 2 "))
        gpa3 = int(input("GPA 3 "))
        gpa4 = int(input("GPA 4 "))
        print("")
        print("Their Average GPA is:")
        calc = (gpa1 + gpa2 + gpa3 + gpa4)/4
        print(str(calc))
        print("")
    elif userIn == "Exit":
        break
        exit