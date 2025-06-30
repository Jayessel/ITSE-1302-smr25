#!/usr/bin/env python3
        
def get_float(message,low_range, high_range):
    while True:
        float_val = float(input(message))
        if low_range < float_val < high_range:
            break
        print(f"Entry must be greater than {low_range} and less than or equal to {high_range}.")
    return float_val

def get_int(message,low_range, high_range):
    while True:
        int_val = int(input(message))
        if low_range < int_val < high_range:
            break
        print(f"Entry must be greater than {low_range} and less than or equal to {high_range}.")
    return int_val

def main():
    choice = "y"
    while choice.lower() == "y":
        # function tests
        float_test = get_float("Enter monthly investment:\t",0,1000)
        print("Monthly investment:\t",float_test)
        int_test = get_int("Enter number of years:\t\t",0,50)
        print("Number of years:\t",int_test)

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
