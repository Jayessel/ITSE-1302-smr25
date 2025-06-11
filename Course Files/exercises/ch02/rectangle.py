#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = float(input("Please enter the length: "))
width = float(input("Please enter the width:  "))

# calculate miles per gallon
area = round(length * width)
perimeter = round(2 * (length + width))
            
# format and display the result
print()
print(f"Area = \t{area}")
print(f"Perimeter = {perimeter}")
print()
print("Bye!")


