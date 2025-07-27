#!/usr/bin/env python3
import pickle

def write_trip(miles_driven,gallons_used,mpg):
    with open("trips.bin","wb") as sheet:
        trip = [miles_driven,gallons_used,mpg]
        pickle.dump(trip,sheet)
        

def read_trips(goose): 
    with open("trips.bin","rb") as sheet:
        trips = pickle.load(sheet)
        goose.append(trips)

    return goose

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

    # with open("trips.bin","wb") as sheet:
    #     pickle.dump('',sheet)
    goose = []
    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()
          
        write_trip(miles_driven,gallons_used,mpg)
        triple = read_trips(goose)      
        list_trips(triple)
        more = input("More entries? (y or n): ")
        print()
    
    print("Bye!")

if __name__ == "__main__":
    main()
