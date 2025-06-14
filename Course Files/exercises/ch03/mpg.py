#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()
entry = 'y'

while entry == 'y':
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
    print()

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
        continue
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)
        # calculate and display total gas cost
        tgc = gallons_used * cost_per_gallon
        print("Total Gas Cost:            ", tgc)
        # calculate and display cost per mile
        cpm =  round(tgc / miles_driven,1)
        print("Cost Per Mile:             ", cpm)
        print()

    entry = input("Get entries for another trip (y/n)? ")
    print()

print("Bye!")
