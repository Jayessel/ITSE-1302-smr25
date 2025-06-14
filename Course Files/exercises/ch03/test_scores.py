#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")

enter_again = 'y'
while enter_again.lower() == "y":
    print()
    print("Enter test scores")
    print("Enter 999 to end input")
    print("======================")

    # initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    ts_input = 0

    while ts_input != "end":
        ts_input = input("Enter test score: ")
        if ts_input.lower() == "end":
            if score_total == 0:
                print('Please enter at least one test score.')
                ts_input = 0
                continue
            else:
                break
        else:
            test_score = int(ts_input)
            if test_score >= 0 and test_score <= 100:
                score_total += test_score
                counter += 1
            else:
                print(f"Test score must be from 0 through 100. "
                      f"Score discarded. Try again.")


    # while test_score != 999:
    #     test_score = int(input("Enter test score: "))
    #     if test_score >= 0 and test_score <= 100:
    #         score_total += test_score
    #         counter += 1
    #     elif test_score == "end":
    #         break
    #     else:
    #         print(f"Test score must be from 0 through 100. "
    #               f"Score discarded. Try again.")

    # calculate average score
    average_score = round(score_total / counter)

    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()
    enter_again = input("Enter another set of test scores (y/n)? ")

print()
print("Bye!")


