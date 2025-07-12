
def main():
    stud_inf = {}

    stud_inf["John"] = {'id':123,'gpa':3.4,'credits-completed':15.0,'grades':[87,98,65,78]}
    stud_inf["Anna"] = {'id':456,'gpa':3.8,'credits-completed':23.0,'grades':[54,98,78,86,87,68]}

    print(stud_inf)
    print()

    print('List of Students:')
    for name in stud_inf.keys():
        print(name)
    print()

    print(f'Student Information\nStudent ID\tGPA\tCredits Completed\tGrades')
    for student in stud_inf.items():
        info = student[1]
        print(f'{student[0]}\t{info["id"]}\t{info["gpa"]}\t{info['credits-completed']}\t\t\t{info['grades']}')
    print()

    name = list(stud_inf.items())
    print(f'{name[0][0]} has dropped out, removing from student info registry')
    stud_inf.pop(name[0][0])
    print(stud_inf)
    print()

    name = list(stud_inf.items())
    print(f'Getting {name[0][0]}\'s GPA')
    print(name[0][1]['gpa'])
    print()

    print('Students have graduated, clearing the student registry')
    stud_inf.clear()
    print(stud_inf)
    print()

if __name__ == "__main__":
    main()