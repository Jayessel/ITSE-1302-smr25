import csv

def create_file():
    #creates blank file and adds header
    print('Create new contact file')
    print('-----------------------------------------')
    with open('contact_file.csv','w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Phone','Email'])

def add_contact():
    #appends input info to file
    print('Add new contact')
    print('-----------------------------------------')
    Name = input('Enter contact name: ')
    Phone = input('Enter contact phone number: ')
    Email = input('Enter contact email: ')
    with open('contact_file.csv','a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Name,Phone,Email])

def list_contacts():
    #adds each row of file to list then prints from list
    print('List all contacts')
    print('-----------------------------------------')
    listContacts = []
    with open('contact_file.csv','r') as file:
        red = csv.reader(file)
        for row in red:
            listContacts.append(row)
    listContacts.pop(0)
    print(f'Name\t\tPhone Number\t\tEmail')
    for item in listContacts:
        print(f'{item[0]}\t\t{item[1]}\t\t{item[2]}')

def edit_contacts():
    #First part same as list function
    print('Modify existing contact')
    print('-----------------------------------------')
    editContacts = []
    with open('contact_file.csv','r') as file:
        red = csv.reader(file)
        for row in red:
            editContacts.append(row)
    editContacts.pop(0)
    print(f'Name\t\tPhone Number\t\tEmail')
    for i, item in enumerate(editContacts,start=1):
        print(f'{i}. {item[0]}\t\t{item[1]}\t\t{item[2]}')
    
    #Second part changes values that are now in a list
    contact_len = len(editContacts)+1
    print(f'{contact_len}. Cancel')
    while (contact_num := int(input('Choose contact: '))) not in range(1,contact_len+1):
        print('Please enter valid index')
    if contact_num == contact_len:
        print('Cancelled')
        return
    print()
    print(f'Contact {contact_num}.')
    print('-----------------------------------------')
    for i, detail in enumerate(editContacts[contact_num-1],start=1):
        print(f'{i}. {detail}')
    while (value_number := int(input('Choose value to change: '))) not in range(1,4):
        print('Please enter a valid index')
    new_value = input('Enter new value: ')
    editContacts[contact_num-1][value_number-1] = new_value
    
    #Third rewrites the file with the changed list
    with open('contact_file.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name','Phone','Email'])
            writer.writerows(editContacts)



def main():
    print('Purpose of program is ...')
    options = (f'1.Create new contact file\n2.Add new contact\n3.List all contacts\n4.Modify existing contact\n5.Exit program\nEnter: ') 
    while True:
        print(':::::::::::::::::::::::::::::::::::::::::')
        print('Choose an option:')
        while (x := int(input(options))) not in range(1,6):    #Not sure if we went over this but I found that you could use the 'in' keyword to check if something is in a list. Tried putting 'not' in front of it and that worked.
            print(f'\nPlease enter a valid option\n')          #Also found that the range function works for this. Was using [1,2,3,4,5] before
        print()
        if x == 1:
            create_file()
            print('File created')
        elif x == 2:
            add_contact()
            print('Contact created')
        elif x == 3:
            list_contacts()
        elif x == 4:
            edit_contacts()  
            print('Contact changed')
        elif x == 5:
           break 
    print('Goodbye...')
    print('Completed by James Light')

if __name__ == "__main__":
    main()