#Unit 2 Exam 
"""
New Employee Entry Program

Allows user to add a new employee to the employee registry.

Automatically generate unique employee id number between 1-500.

Prints a list of employees that were added and their id numbers.

"""

from random import randrange                            #used to generate new employee id number

def print_employee(employee_dict):
    """
    Prints each of the newly added employees and thier generated id numbers.
    Arguments: 
        -Main list of employee dictionary objects
    """
    employee = list(employee_dict.items())[0]           #converts dictionary object to a tuple that can be indexed
    print("Created Employee:     ",employee[0])
    print('Employee ID:          ',employee[1])

#funtion to add a single employee
def add_employee(registry,idlist,elist):
    """
    New employee name is entered, is given an id number, and added to the system.
    Arguments:
        -Main list of employee dictionary objects
        -List of employee id numbers
        -List of employee names   
    """
    while True:
        name = input("Enter employee's name: ")
        elist_lower = [emp.lower() for emp in elist]    #list comprehension to convert each employee name already in the list to all lowercase
        if name.lower() in elist_lower:                 #checks if new name is already in list
            print('Employee already exists')
            continue

        elist.append(name)                              #adds employee name to name list
        while (id := randrange(1,501)) in idlist:       #generates new unique id number
            pass

        idlist.append(id)                               #adds id to list of ids
        new_employee = {name:id}                        #creates new employee dictionary object
        registry.append(new_employee)                   #adds dictionary to list of employee dictionay objects
        break


def main():
    print("Employee Registry Program")
    print('------------------------------------------')
    employee_registry = []
    employee_id = []
    employee_list = []

    #loop to create entered number of employees
    new = int(input('How many new employees are you adding?: '))       
    for i in range(new):                                                
        print('------------------------------------------')
        add_employee(employee_registry,employee_id,employee_list)
    print()
    
    #loop to print each created employee
    print('Created User Information')
    for e in employee_registry:                                         
        print('------------------------------------------')
        print_employee(e)
    print()

    print('------------------------------------------')
    print("Completed by James Light")

if __name__ == "__main__":
    main()