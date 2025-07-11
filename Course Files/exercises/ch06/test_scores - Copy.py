#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    score_total = 0
    counter = 0
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            if len(scores) < 2:
                exit()
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
                score_total += score
                counter += 1 
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    score_total = 0
    count = len(scores)
    for i in scores:        
        score_total += i        
    average = score_total // count
    low_score = min(scores)
    high_score = max(scores)
    if (count % 2) == 1:
        med_score = scores[int((count+1) /2) -1]
    else:
        med_score = (scores[int(count/2) -1] + scores[int((count/2) +1) -1]) // 2
                
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", med_score)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


