feetA = int(input("How far does the snail climb during one day (FT) ?>  "))
feetB = int(input("How far does the snail fall during one night (FT) ?>  "))
feetH = feetA - feetB
day = 12
night = 12
dayNight = day + night
totalPerDay = feetH/2
print("The total the snail moved in one day-night (24 Hours) cycle was: "+ str(totalPerDay) +" feet...")