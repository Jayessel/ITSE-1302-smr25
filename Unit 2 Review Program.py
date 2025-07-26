import random
#Gradebook program
#Base completion
#Advanced completion

def enter_info(curr_gradebook, student_list: list):
    while True:
        name: str
        grades = []
        name = input("Enter student name: ")
        # if name in student_list:
            # print('Student already in list. Please enter a different name.')
            # continue

        # lowercase_names = [name.lower() for name in names]
        stud_lower = [stud.lower() for stud in student_list]
        print(stud_lower)
        if name.lower() in stud_lower:
            print('Student already in list. Please enter a different name.')
            continue

        student_list.append(name)
        while (numgrades := int(input('How many grades do they have?: '))) <= 0:
            print('Number must be more than zero.')
        grades = [random.randrange(0,101) for i in range(numgrades)]
        student_dict = {name:grades}
        curr_gradebook.append(student_dict)
        break

def printgrades(student):
    total = counter = 0
    cur_stu = list(student.items())[0]
    print('Student name: ',cur_stu[0])
    for grade in cur_stu[1]:
        counter += 1
        print(f'Grade {counter}: {grade}')
        total += grade
    avg_g = total // counter
    print('Average grade: ',avg_g)

def main():
    print("Gradebook Program")
    gradebook = []
    students = []
    stud_num: int
    stud_num = int(input('Please enter number of students: '))
    for i in range(stud_num):
        enter_info(gradebook,students)    
    print(gradebook)
    print()
    for a in gradebook:
        printgrades(a)
        print()

    print("Done.")

if __name__ == "__main__":
    main()