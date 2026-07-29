print("Currency Converter EUR, BRL and USD")
print("1. BRL")
print("2. EUR")
print("3. USD") 
USD_BRL = 5.50
EUR_BRL = 6.40
USD_EUR = 0.86
EUR_USD = 1.16
BRL_USD = 0.18
BRL_EUR = 0.16
while True:
    sourcecurrency = input("Tell me what source currency do you wanna convert: ")
    if sourcecurrency == "1" or sourcecurrency == "BRL":
        sourcecurrency = "BRL"
        print("You selected Real Brazilian!")
    elif sourcecurrency == "2" or sourcecurrency == "EUR":
        sourcecurrency = "EUR"
        print("You selected Euro!")
    elif sourcecurrency == "3" or sourcecurrency == "USD":
        sourcecurrency = "USD"
        print("You selected American Dollar!")
    else:
        print("This currency are not avaible for convert, sorry.")
        exit()
    destinationcurrency = input("Tell me what destination currency do you wannna send: ")
    if destinationcurrency == "1" or destinationcurrency == "BRL":
        destinationcurrency = "BRL"
        print("You selected Real Brazilian!")
    elif destinationcurrency == "2" or destinationcurrency == "EUR":
        destinationcurrency = "EUR"
        print("You selected Euro!")
    elif destinationcurrency == "3" or destinationcurrency == "USD":
        destinationcurrency = "USD"
        print("You selected American Dollar!")
    else:
        print("This currency is not avaible for convert, sorry.")
        exit()
    if sourcecurrency == destinationcurrency:
        print("You selsected the same currency! You don't need to convert anything!")
        continue
    amount = float(input("How much do you wanna converty?"))
    if sourcecurrency == "BRL" and destinationcurrency == "USD":
        result = amount * BRL_USD
        print(f"US{result:.2f}")
    elif sourcecurrency == "BRL" and destinationcurrency == "EUR":
        result = amount * BRL_EUR
        print(f"EUR{result:.2f}")
    elif sourcecurrency == "EUR" and destinationcurrency == "BRL":
        result = amount * EUR_BRL
        print(f"R${result:.2f}")
    elif sourcecurrency == "EUR" and destinationcurrency == "USD":
        result = amount * EUR_USD
        print(f"US{result:.2f}")
    elif sourcecurrency == "USD" and destinationcurrency == "EUR":
        result = amount * USD_EUR
        print(f"EUR{result:.2f}")
    elif sourcecurrency == "USD" and destinationcurrency == "BRL":
        result = amount * USD_BRL
        print(f"R${result:.2f}")
    again = input("Do you want to convert again? (Y/N)")
    if again == "N":
        print("Thanks")
        break
    elif again == "Y":
        continue
    else:
        print("This option is unavaible")