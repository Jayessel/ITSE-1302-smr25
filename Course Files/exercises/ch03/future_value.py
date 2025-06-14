#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    monthly_investment = float(input("Enter monthly investment:\t"))
    while monthly_investment <= 0:
        print("Entry must be greater than 0. Please try again.")
        monthly_investment = float(input("Enter monthly investment:\t"))
    # if monthly_investment <= 0:
    #     print("Monthly investment must be greater than zero. Please try again.")
    #     continue
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate >= 15:
        if yearly_interest_rate <= 0:
            print("Entry must be greater than 0. Please try again.")
        else:
            print("Entry must be less than 15. Please try again.")
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))
    while years <= 0 or years >= 50:
        if years <= 0:
            print("Entry must be greater than 0. Please try again.")
        else:
            print("Entry must be less than 50. Please try again.")
        years = int(input("Enter number of years:\t\t"))
    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if (i + 1) % 12 == 0 and i != 0:
            print(f"Year =\t{round((i + 1) / 12)}\t\t\tFuture value:\t{round(future_value, 2)}")
    print()

    # display the result
    # print(f"Future value:\t\t\t{round(future_value, 2)}")
    # print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
