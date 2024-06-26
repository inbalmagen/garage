
from os import name


def add_car(garage):
    new_car_model = input("enter car model: ")
    new_car_color = input("enter color: ")
    new_car_year = int(input("enter year: "))
    new_car = {
        "model": new_car_model,
        "color": new_car_color,
        "year": new_car_year
    }
    garage.append(new_car)

    print("car added")

def edit_car(garage):
    model = input("Enter the model of the car to edit: ")
    year = int(input("Enter the year of the car to edit:  "))
    color = input("Enter the color of the car to edit: ")
    for car in garage:
        if car ["model"] == model and car ["year"] == year and car ["color"] == color:
            new_model = input(f"Enter the new model of the car (current: {car['model']}): ")
            new_year = int(input(f"Enter the new year of the car (current: {car['year']}): "))
            new_color = input(f"Enter the new color of the car (current: {car['color']}): ")
            car["model"] = new_model
            car["year"] = new_year
            car["color"] = new_color
            print(f"car '{model}' updated successfully.")
            return
    print(f"car '{model}' not found.")


def delete_car(garage):
    print("****** Deleting car ******")
    model = input("Please enter the model of the car to delete: ")
    found = False
    i = 0
    
    while i < len(garage):
        if garage[i]["model"] == model:
            del garage[i]
            found = True
            print(f"car '{model}' deleted successfully.")
            break  
        i += 1
    
    if not found:
        print(f"car '{model}' not found.")


def car_list(garage):
    print("list of all garage:  ")
    if garage:
        for car in garage:
            print(f"Model: {car['model']}, Color: {car['color']}, Year: {car['year']}")
    else:
        print("No garage available.")