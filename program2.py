#a simple car rental system
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()

    
    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        model TEXT NOT NULL,
                        daily_rate REAL NOT NULL,
                        availability TEXT DEFAULT 'Available'
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        car_id INTEGER NOT NULL,
                        renter_name TEXT NOT NULL,
                        rental_days INTEGER NOT NULL,
                        total_cost REAL NOT NULL,
                        FOREIGN KEY(car_id) REFERENCES cars(id)
                    )''')
     conn.commit()
    conn.close()

# Adding  neiw car to the system
def add_car(model, daily_rate):
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cars (model, daily_rate) VALUES (?, ?)", (model, daily_rate))
    conn.commit()
    conn.close()

# available cars
def view_available_cars():
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE availability = 'Available'")
    cars = cursor.fetchall()
    conn.close()
    return cars

# Rent a car
def rent_car(car_id, renter_name, rental_days):
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()

    # Check car availability
    cursor.execute("SELECT daily_rate FROM cars WHERE id = ? AND availability = 'Available'", (car_id,))
    car = cursor.fetchone()

    if car:
        daily_rate = car[0]
        total_cost = daily_rate * rental_days

        # Update car availability
        cursor.execute("UPDATE cars SET availability = 'Rented' WHERE id = ?", (car_id,))

        # Record the rental
        cursor.execute("INSERT INTO rentals (car_id, renter_name, rental_days, total_cost) VALUES (?, ?, ?, ?)",
                       (car_id, renter_name, rental_days, total_cost))
        conn.commit()
        print(f"Car rented sucessfully! Total cost: ${total_cost:.2f}")
    else:
        print("Sorry,the car is not available.")

    conn.close()

# Return a car
def return_car(car_id):
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()

    # Check if car is rented
    cursor.execute("SELECT id FROM cars WHERE id = ? AND availability = 'Rented'", (car_id,))
    car = cursor.fetchone()

    if car:
        # Update car availability
        cursor.execute("UPDATE cars SET availability = 'Available' WHERE id = ?", (car_id,))
        conn.commit()
        print("Car returned successfully!")
    else:
        print("This car is notcurrently rented.")

    conn.close()

# View rental history
def view_rentals():
    conn = sqlite3.connect("car_rental.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT rentals.id, cars.model, rentals.renter_name, rentals.rental_days, rentals.total_cost
                      FROM rentals
                      JOIN cars ON rentals.car_id = cars.id''')
    rentals = cursor.fetchall()
    conn.close()
    return rentals

# Simple text-based UI
def menu():
    setup_database()
    while True:
        print("\n--- Car Rental System ---")
        print("1. Add a car")
        print("2. View available cars")
        print("3. Rent a car")
        print("4. Return a car")
        print("5. View rental history")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            model = input("Enter car model: ")
            daily_rate = float(input("Enter daily rental rate: "))
            add_car(model, daily_rate)
            print("Car added successfully!")
        elif choice == "2":
            cars = view_available_cars()
            if cars:
                print("\nAvailable Cars:")
                for car in cars:
                    print(f"ID: {car[0]}, Model: {car[1]}, Daily Rate: ${car[2]:.2f}")
            else:
                print("No cars available.")
        elif choice == "3":
            car_id = int(input("Enter car ID to rent: "))
            renter_name = input("Enter your name: ")
            rental_days = int(input("Enter number of rental days: "))
            rent_car(car_id, renter_name, rental_days)
        elif choice == "4":
            car_id = int(input("Enter car ID to return: "))
            return_car(car_id)
        elif choice == "5":
            rentals = view_rentals()
            if rentals:
                print("\nRental History:")
                for rental in rentals:
                    print(f"Rental ID: {rental[0]}, Car: {rental[1]}, Renter: {rental[2]}, "
                          f"Days: {rental[3]}, Total Cost: ${rental[4]:.2f}")
            else:
                print("No rentals yet.")
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
