
def search_by_year(garage):
    print("list of cars with year by choice: ")
    if garage:
        year_to_search = int(input("enter year to search: "))
        for car in garage:
            if car['year'] == year_to_search:
                 print(f"Model: {car['model']}, Year: {car['year']}, Color: {car['color']}")
    else:
        print("No cars available.")

def search_by_model(garage):
    if garage:
        model_to_search = input("enter car model to search: ")
        for car in garage:
            if car['model'] == model_to_search:
                 print(f"Model: {car['model']}, Year: {car['year']}, Color: {car['color']}")
    else:
        print("No garage available.")

def search_contains(garage):
    print("list of cars containing a word: ")
    if garage:
        car_to_search = input("enter search word: ").lower()
        for car in garage:
            if car_to_search in car['model'].lower():
                 print(f"Model: {car['model']}, Year: {car['year']}, Color: {car['color']}")
    else:
        print("No garage available.")


def serch_year_above_2000(garage):
    print("list of cars with year by choice: ")
    if garage:
        for car in garage:
            if car['year'] > 2000 :
                 print(f"Model: {car['model']}, Year: {car['year']}, Color: {car['color']}")
    else:
        print("No garage available.")
