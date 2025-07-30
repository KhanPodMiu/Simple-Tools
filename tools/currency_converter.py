import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    data = response.json()

    if to_currency.upper() in data['rates']:
        rate = data['rates'][to_currency.upper()]
        return amount * rate
    else:
        raise ValueError("Currency not supported.")

def run():
    print("=== Currency Converter ===")
    from_currency = input("From currency (e.g. USD): ")
    to_currency = input("To currency (e.g. EUR): ")
    
    try:
        amount = float(input("Amount: "))
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    except ValueError:
        print("Invalid amount. Please enter a number.")
    except Exception as e:
        print("Error:", e)
