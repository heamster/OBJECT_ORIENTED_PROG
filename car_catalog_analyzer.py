# Car Catalog Analyzer
# This program reads car data from a CSV file and provides reports through a menu.

from pathlib import Path
import statistics

# Function to load car data from the CSV file
def load_cars():
    cars = []

    file_path = Path("cars.csv")

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines[1:]:  # skip header row
        clean_line = line.strip()

        make, model, year = clean_line.split(",")

        car = {
            "make": make.strip().title(),
            "model": model.strip().title(),
            "year": int(year.strip())
        }

        cars.append(car)

    return cars

# Function to show all cars of a certain make
def get_cars_by_make(cars, make="toyota"):

    make = make.title()

    matches = []

    for car in cars:
        if car["make"] == make:
            matches.append(car)
            print(f'{car["make"]} {car["model"]} - {car["year"]}')

    if len(matches) == 0:
        print("No cars found for that make.")

    return matches

# Function to show the oldest cars
def show_oldest_cars(cars):

    oldest_year = min(car["year"] for car in cars)

    print(f"\nOldest car year: {oldest_year}")

    for car in cars:
        if car["year"] == oldest_year:
            print(f'{car["make"]} {car["model"]} - {car["year"]}')

# Function to calculate the average car year
def get_average_year(cars):

    years = []

    for car in cars:
        years.append(car["year"])

    avg = statistics.mean(years)

    avg = int(round(avg, 0))

    return f"The average car year is {avg}"

# Function to show all cars sorted by make
def show_all_sorted(cars):

    sorted_cars = sorted(cars, key=lambda car: car["make"])

    for car in sorted_cars:
        print(f'{car["make"]} {car["model"]} - {car["year"]}')

# Main program
def main():

    cars = load_cars()

    while True:

        print("\nChoose a report:")
        print("1. View all cars sorted by make")
        print("2. Filter cars by make")
        print("3. Show the oldest car(s)")
        print("4. Show the average car year")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_all_sorted(cars)

        elif choice == "2":
            user_make = input("Enter a car make: ")
            get_cars_by_make(cars, user_make)

        elif choice == "3":
            show_oldest_cars(cars)

        elif choice == "4":
            print(get_average_year(cars))

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
main()