from ITSE_1302 import *
import locale as lc
lc.setlocale(lc.LC_ALL,'us')


def get_input(message):
    while True:
        value = input(message)
        try:
            fl_val = float(value)
            if fl_val < 0:
                raise ValueError('value must be greater than zero.')
        except ValueError as e:
            print('Value error occurred:',e)
            continue
        except Exception:
            print('Something went wrong...')
            continue
        return fl_val

def get_expenses(expense_list):
    while True:
        while (expense := int(get_input('Enter an expense amount (or 0 to exit): '))) < 0:
            print('Please enter a valid input')
        if expense == 0:
            return expense_list
        expense_list.append(expense)

def main():
    print("Welcome to Budget Buddy")
    print('----------------------------')

    tot_income = get_input('Enter your total income: ')
    expense_list = []
    expenses = get_expenses(expense_list)
    expense_sum = 0
    for val in expenses:
        expense_sum += val
    remaining = tot_income - expense_sum
    print()
 

    form = '.2f'
    print('Budget Results:')
    print('----------------------------')
    print(f'Total Income:     ${tot_income:{form}}')
    print(f'Total Expenses:   ${expense_sum:{form}}')
    print(f'Remaining Budget: ${remaining:{form}}')
    print()

    print('Complete Expense List')
    print('----------------------------')
    for i,val in enumerate(expenses,start=1):
        exp = lc.currency(val)
        print(f'{i}.{exp:>10}')
    print()

    jl_sign()   #Made a function to print "Completed by, James Light"


if __name__ == '__main__':
    main()