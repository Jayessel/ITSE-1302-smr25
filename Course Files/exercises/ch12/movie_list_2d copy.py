#!/usr/bin/env python3

def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(i, movie['name'], movie['year'])
            # print(f"{i}. {movie[0]} ({movie[1]})")
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = {"name": name, "year": year}
    movie_list.append(movie)
    print(f"{movie['name']} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie['name']} was deleted.\n")

def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    
        
def main():
    movie_list = [{"name": "Monty Python and the Holy Grail", "year": 1975},
                  {"name": "On the Waterfront", "year": 1954},
                  {"name": "Cat on a Hot Tin Roof", "year": 1958}]
    
    display_menu()
    
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
