import qrcode

def generate_qr():
    print("\n=== QR Code Generator ===")
    data = input("Enter the text or URL to generate QR Code: ").strip()

    if not data:
        print("No data entered. QR code generation cancelled.")
        return

    try:
        img = qrcode.make(data)
        file_name = "qr_code.png"
        img.save(file_name)
        print(f"✅ QR Code saved as '{file_name}'")
    except Exception as e:
        print(f"❌ Failed to generate QR Code: {e}")

def run():
    while True:
        print("\n=== QR Code Tool ===")
        print("1. Generate QR Code")
        print("0. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_qr()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")
