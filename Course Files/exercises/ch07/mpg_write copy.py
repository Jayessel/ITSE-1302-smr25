#!/usr/bin/env python3
import csv

def write_trip(miles_driven,gallons_used,mpg):
    with open("trips.csv","a",newline='') as sheet:
        writer = csv.writer(sheet)
        writer.writerow([miles_driven,gallons_used,mpg])

def read_trips(): 
    with open("trips.csv","r") as sheet:
        output = csv.reader(sheet)
        trips = []
        for row in output:
            trips.append([row[0],row[1],row[2]])
        return trips

def list_trips(trips):
    print(f'Distance\tGallons\t\tMPG')
    for row in trips:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    with open("trips.csv","w",newline='') as sheet:
        sheet.write('')
 
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
          
        write_trip(miles_driven,gallons_used,mpg)
        trips = read_trips()      
        list_trips(trips)
        more = input("More entries? (y or n): ")
        print()
    
    print("Bye!")

if __name__ == "__main__":
    main()

