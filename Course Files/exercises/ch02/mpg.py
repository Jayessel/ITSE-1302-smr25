#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallons_cost = float(input("Enter cost per gallon:\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
totCost = round(gallons_cost * gallons_used, 1)
cpm = round(totCost / miles_driven, 1)
            
# format and display the result
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas Cost:\t\t{totCost}")
print(f"Cost Per Mile:\t\t{cpm}")
print()
print("Bye!")


