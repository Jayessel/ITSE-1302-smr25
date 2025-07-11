import random

def rem_lowest(grades):
    print("Removing lowest grade")
    lowest = grades.index(min(grades))
    grades.pop(lowest)
    print(grades)

def rem_rand(grades):
    print("Removing random grade")
    random_grade = random.choice(grades)
    grades.remove(random_grade)
    print(grades)

def edit_grade(grades):
    print("Edit a grade")
    for num, grade in enumerate(grades, start=1):
        print(f"{num}.\t{grade}")

    while True:
        edit = int(input("Which grade do you want to edit?: ")) - 1
        if 0 <= edit <= (len(grades) - 1):
            break
        print("Please enter a valid grade")
    grades[edit] = int(input("Enter the new grade: "))
    print(grades)

def rev_and_sort(grades):
    print("Sorting and Reversing List")
    grades.sort()
    grades.reverse()
    print(grades)

def tot_and_ave(grades):
    total = sum(grades)
    print("Total: ",total)
    average = total / len(grades)
    print("Average", average)

def main():
    grades = []
    while (grade := int(input("Please enter the grade of -1 to stop: "))) != -1:
        grades.append(grade)
    print(grades)
    rem_lowest(grades)
    rem_rand(grades)
    edit_grade(grades)
    rev_and_sort(grades)
    tot_and_ave(grades)
    print("Completed by, James Light")

if __name__ == "__main__":
    main()
