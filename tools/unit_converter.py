def run():
    print("Welcome to Unit Converter!")
    while True:
        print("\nChoose a unit to convert:")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            miles = km * 0.621371
            print(f"{km} km = {miles:.2f} miles")

        elif choice == "2":
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")

        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
