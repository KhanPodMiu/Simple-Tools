import sys
from tools import unit_converter, currency_converter, qr_generator, password_generator

def main():
    while True:
        print("\n🛠️ Simple Tools Hub")
        print("1. Unit Converter")
        print("2. Currency Converter")
        print("3. QR Code Generator")
        print("4. Password Generator")
        print("0. Exit")

        choice = input("\nSelect a tool: ")

        if choice == '1':
            unit_converter.run()
        elif choice == '2':
            currency_converter.run()
        elif choice == '3':
            qr_generator.run()
        elif choice == '4':
            password_generator.run()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
