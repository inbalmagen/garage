

from crud.actions import add_car, car_list, delete_car,  edit_car
from crud.search import search_by_model, search_by_year, search_contains, serch_year_above_2000
from load_save.load_save import read_file, save_file


def garage_menu():
    garage = read_file()
    while True:
        print ("please choose an option:  ")
        print ("1. Add car")
        print ("2. Edit car")
        print ("3. Delete car")
        print ("4. Search car by year")
        print ("5. Search car above 2000")
        print ("6. Search by model")
        print ("7. Search cars containing word")
        print ("8. List of all cars")
        print ("x. Exit menu")
        choice = input("please enter your choice:  ")
        
        if choice == "1":           
            print("add car is your choice")
            add_car(garage)
            save_file(garage)
        elif choice == "2":
            print("edite car is your choice")
            edit_car(garage)
            save_file(garage)
        elif choice == "3":
            print("delete destination is your choice")
            delete_car(garage)
            save_file(garage)
        elif choice == "4":
            search_by_year(garage)
        elif choice == "5":
            serch_year_above_2000(garage)
        elif choice == "6":
            print("search car by model")
            search_by_model(garage)
        elif choice == "7":
            print("search car containing word")
            search_contains(garage)
        elif choice == "8":
            print("list of all cars")
            car_list(garage)
        elif choice == "x":
            print("you choose to exit")
            exit()