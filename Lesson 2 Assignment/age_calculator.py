# input values
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
current_year = int(input("Please enter the current year: "))
birth_year = int(input("Please enter the birth year: "))

# calculate current age
age = current_year - birth_year

# output greeting and age
print()
print("Hello " + first_name + " " + last_name + "!\nYou are " + str(age) + " years old.")
# print("Hello", first_name, last_name, "\b!\n", "\bYou are", age, "years old.")    # alternative print statement

# calculate next year's age
age += 1

# output next year statement
print()
print(f"In the next year {current_year + 1}, you will be {age} years old.")
print()
print('------------------------')
print(f"Completed by, {first_name} {last_name}.")