print("The Calculator...")
def show_menu():
    print("Menu options: ")
    print("1 - Calculator")
    print("2 - Historical")
    print("3 - Delete Historical")
    print("4 - Exit")
def show_operations():
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication") 
    print("4 - division")
    print("5 - raised")
    print("6 - square root")
def get_numbers():
    while True:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            return num1, num2
        except ValueError:
            print("Type just numbers")
def addition():
    num1, num2 = get_numbers()
    result = (num1 + num2)
    return(f"{num1} + {num2} = {result}")
def subtraction():
    num1, num2 = get_numbers()
    result = (num1 - num2)
    return(f"{num1} - {num2} = {result}")
def multiplication():
    num1, num2 = get_numbers()
    result = (num1 * num2)
    return(f"{num1} * {num2} = {result}")
def division():
    num1, num2 = get_numbers()
    if num2 == 0:
        return("You cannot divide by zero...")
    result = (num1 / num2)
    return(f"{num1} / {num2} = {result}")
def raised():
    num1, num2 = get_numbers()
    result = (num1 ** num2)
    return(f"{num1} ^ {num2} = {result}")
def square_root():
    num1 = float(input("First number: "))
    result = (num1 ** 0.5)
    return(f"√{num1} = {result}")
historical_list = []
while True:
    show_menu()
    option = input("Select the Menu option: ")
    if option == "1":
        show_operations()
        while True:
            operation = input("Select the operation: ")
            if operation == "1":
                result = addition()
                historical_list.append(result)
                print(result)
            elif operation == "2":
                result = subtraction()
                historical_list.append(result)
                print(result)
            elif operation == "3":
                result = multiplication()
                historical_list.append(result)
                print(result)
            elif operation == "4":
                result = division()
                historical_list.append(result)
                print(result)
            elif operation == "5":
                result = raised()
                historical_list.append(result)
                print(result)
            elif operation == "6":
                result = square_root()
                historical_list.append(result)
                print(result)
            else:
                print("Invalid operation")
                break
            dnv = input("Do you want to do another calculation? (Y/N)")
            if dnv.lower() == "y":
                continue
            elif dnv.lower() == "n":
                print("Thanks for using this calculator, see you later!")
                break
            else:
                print("Thanks for using this calculator, we will return you to the menu")
                break
    elif option == "2":
        if len(historical_list) == 0:
            print("The history is empty")
        else:
            for calculation in historical_list:
                print(calculation)
            input("Press Enter to return to the menu")
            continue
    elif option == "3":
        delet = input("Do you really want to delete your history? (Y/N)")
        if delet.lower() == "y":
            historical_list.clear()
            print("History deleted sucessfully")
        elif delet.lower() == "n":
            print("Okay, return to the menu...")
        else:
            print("This option is not valid, back to the menu...")
    elif option == "4":
        print("Thanks for using this calculator! See you later...")
        break
    else:
        print("This option is not valid, return to the menu...")
        continue