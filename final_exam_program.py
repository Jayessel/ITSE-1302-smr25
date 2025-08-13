from datetime import datetime
import csv

def read_and_store():
    # Reads text file, splits into list items, converts numbers to float type
    with open('unit_2_exam.txt','r') as file:
        data = file.read()
        data = data.split('\n')
        idx = 0
        for item in data:
            data[idx] = item.split('|')
            data[idx][1] = float(data[idx][1])
            idx += 1
    return data

def print_content(data):
    # Prints formatted current data
    print('Month',' '*8,'Amount')
    print('-'*30)
    for item in data:
        print(f'{item[0]+':':<15}{item[1]:.2f}')
    print()

def user_selection():
    # Creates user menu with input validation
    print('What operation would you like to perform?')
    while True:
        print('Enter 1 to edit a value')
        print('Enter 2 to delete a value')
        print('Enter 3 to write a data to csv file and close program')
        print('Enter -1 to close program without saving')
        try:
            choice = int(input('Enter your choice: '))
            if choice not in [-1] + [i for i in range(1,4)]: #checks if user input is a valid choice
                raise
        except:
            print('Please enter a valid input...')
            print()
            continue
        break
    return choice

def save_csv(data):
    # Writes the current data to csv file named by user
    while True:
        csv_name = input('Enter name to save file as (don\'t inlcude .csv): ')
        csv_name = csv_name + '.csv'
        print(f'File name: {csv_name}')
        try:
            with open(csv_name,'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except:
            print('Please enter a valid file name...')
        break

def edit_value(data):
    # Allows user to select and edit stored data values
    print('EDIT')
    print('-'*30)
    for i, item in enumerate(data,start=1):
        print(f'{i}. {item[0]+':':<10}{item[1]:.2f}') # Prints numbered current data to be selected from
    while True:
        try:
            edit_choice = int(input('Enter your choice to edit(-1 to cancel): '))
            if edit_choice not in [-1] + [i for i in range(1,len(data)+1)]:
                raise
        except:
            print('Please enter a valid input...')
            print()
            continue
        break
    if edit_choice == -1:
        return
    edit_item = data[edit_choice-1] # Stores chosen data to be printed
    print(f'Current value of {edit_item[0]} is {edit_item[1]:.2f}')
    while True:
        try:
            new_val = float(input('Enter the new value: '))
            if new_val < 0:
                raise
        except:
            print('Please enter a valid input...')
            print()
            continue
        break
    data[edit_choice-1][1] = new_val # New data is stored to list
    return data


def delete_value(data):
    # Allows user to select and delete stored data
    print('DELETE')
    print('-'*30)
    for i, item in enumerate(data,start=1):
        print(f'{i}. {item[0]+':':<10}{item[1]:.2f}')
    while True:
        try:
            delete_choice = int(input('Enter your choice to delete(-1 to cancel): '))
            if delete_choice not in [-1] + [i for i in range(1,len(data)+1)]:
                raise
        except:
            print('Please enter a valid input...')
            print()
            continue
        break
    if delete_choice == -1:
        return
    delete_item = data[delete_choice-1]
    print(f'Deleting {delete_item[0]} value of {delete_item[1]:.2f}')
    data.pop(delete_choice-1) # Data is deleted from list
    return data


def main():
    print('Budget Editor Program')
    start = datetime.now()
    start = start.strftime('%B/%d/%y %I:%M %p')
    print('Start time: ', start)
    print('-'*50)
    print()

    data = read_and_store()   # Reads text file and stores data in list "data"
    
    while True:
        print_content(data) # Current data is printed
        choice = user_selection() # Menu is displayed
        if choice == 1:
            edit_value(data)
        if choice == 2:
            delete_value(data)
        if choice == 3:
            save_csv(data)
            print('Closing program...')
            print()
            break
        if choice == -1:
            print('Closing program...')
            print()
            break
        
        
    print('-'*50)
    end = datetime.now()
    end = end.strftime('%B/%d/%y %I:%M %p')
    print('End time: ', end)

    print('Completed by James Light')


if __name__ == '__main__':
    main()