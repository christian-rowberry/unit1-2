def centuryFromYear(year):
    return (year) // 100 + 1


userYear = input("What Year would you like to convert ?>> ")
print("Year: " + str(userYear) + " is to the " + str(centuryFromYear(int(userYear))) + "-th Century")
