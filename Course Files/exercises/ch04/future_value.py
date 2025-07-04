#!/usr/bin/env python3

from validation import *

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

# def get_float(message,low_range, high_range):
#     while True:
#         float_val = float(input(message))
#         if low_range < float_val < high_range:
#             break
#         print(f"Entry must be greater than {low_range} and less than or equal to {high_range}.")
#     return float_val
#
# def get_int(message,low_range, high_range):
#     while True:
#         int_val = int(input(message))
#         if low_range < int_val < high_range:
#             break
#         print(f"Entry must be greater than {low_range} and less than or equal to {high_range}.")
#     return int_val

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
        years = get_int("Enter number of years:\t\t",0,50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
