# enter and verify amount to invest
amount_invested = int(input("Enter the amount you would like to invest each month: "))
while amount_invested <= 0 or amount_invested >= 50000:
    if amount_invested <= 0:
        print("Amount is too low, please try again...")
    elif amount_invested >= 50000:
        print("Amount is too high, please try again...")
    amount_invested = int(input("Enter the amount you would like to invest each month: "))

# enter and verify interest rate value
interest_rate = int(input("Enter the yearly interest rate: "))
while interest_rate <= 0 or interest_rate >= 15:
    if interest_rate <= 0:
        print("Interest rate is too low, please try again...")
    elif interest_rate >= 15:
        print("Interest rate is too high, please try again...")
    interest_rate = int(input("Enter the yearly interest rate: "))

# enter and verify investment period
investment_duration = int(input("Enter the number of years: "))
while investment_duration <= 0:
    print("Investment duration is too low, please try again...")
    investment_duration = int(input("Enter the number of years: "))

# calculate compounded investment
investment_duration_months = investment_duration * 12
interest_rate_months = (interest_rate / 12) / 100
total_investment = 0

for i in range(investment_duration_months):
    total_investment += amount_invested
    total_investment += interest_rate_months * total_investment
    if (i + 1) % 12 == 0:
        print(f"Year {(i + 1) // 12}: {total_investment:.2f}")
        # found this way to format strings https://docs.python.org/3/library/string.html#formatspec

print(f"\nInvestment duration: {investment_duration} years")
print(f"Yearly interest rate: {interest_rate:.2f}%")
print(f"Amount invested monthly: ${amount_invested}")
print(f"Total investment after compounding: ${total_investment:.2f}")

print("\nCompleted by, James Light")