import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_specials=True):
    characters = list(string.ascii_lowercase)
    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_specials:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def run():
    print("\n=== 🔐 Password Generator ===")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_specials = input("Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_specials)
        if password:
            print(f"\n✅ Generated Password: {password}")
        else:
            print("❌ No characters selected to generate password.")
    except ValueError:
        print("❌ Invalid input. Please enter numbers for password length.")
