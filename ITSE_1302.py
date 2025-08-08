import os

def jl_sign():
    your_name_here = 'James Light'
    print(f"Completed by, {your_name_here}.")

def word():
    number = 2

    while number < 20:
        part1 = "D:/ITSE 1302/JLight - Lesson "
        part2 = " Assignment.docx"
        filename = part1 + str(number)+ part2
        print(filename)
        try:
            current_file = open(filename, "x")
        except FileExistsError:
            print("File exists")
            number += 1
            continue
        current_file.close()
        break

    os.startfile(filename)
    

def main():
    pass

if __name__ == '__main__':
    main()