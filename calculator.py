print("The Calculator...")
def addition():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = (num1 + num2)
    return(f"{num1} + {num2} = {result}")
def subtraction():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    result = (num1 - num2)
    return(f"{num1} - {num2} = {result}")
def multiplication():
    num1 = float(input("First number: "))
    num2 = float(input("Second number"))
    result = (num1 * num2)
    return(f"{num1} * {num2} = {result}")
def division():
    num1 = float(input("First number: "))
    num2 = float(input("Second number"))
    if num2 == 0:
        return("You cannot divide by zero...")
    result = (num1 / num2)
    return(f"{num1} / {num2} = {result}")
def raised():
    num1 = float(input("First number: "))
    num2 = float(input("Second number"))
    result = (num1 ** num2)
    return(f"{num1} ^ {num2} = {result}")
def square_root():
    num1 = float(input("First number: "))
    result = (num1 ** 0.5)
    return(f"√{num1} = {result}")
historical_list = []
while True:
    print("Menu options: ")
    print("1 - Calculator")
    print("2 - Historical")
    print("3 - Delete Historical")
    print("4 - Exit")
    option = input("Select the Menu option: ")
    if option == "1":
        print("+. addition")
        print("-. subtraction")
        print("*. multiplication") 
        print("/. division")
        print("^. raised")
        print("r. square root")
        while True:
            operation = input("Select the operation: ")
            if operation == "+":
                result = addition()
                historical_list.append(result)
                print(result)
            elif operation == "-":
                result = subtraction()
                historical_list.append(result)
                print(result)
            elif operation == "*":
                result = multiplication()
                historical_list.append(result)
                print(result)
            elif operation == "/":
                result = division()
                historical_list.append(result)
                print(result)
            elif operation == "^":
                result = raised()
                historical_list.append(result)
                print(result)
            elif operation.lower() == "r":
                result = square_root()
                historical_list.append(result)
                print(result)
            else:
                print("Invalid operation")
                break
            dnv = input("Do you want to do another calculation? (Y/N)")
            if dnv == "Y":
                continue
            elif dnv == "N":
                print("Thanks for use this calculator, see you later!")
                break
            else:
                print("Thanks for use this calculator, we will direction you to the menu")
                break
    elif option == "2":
        if len(historical_list) == 0:
            print("The historical is empty")
        else:
            for calculation in historical_list:
                print(calculation)
            input("Press Enter to return to the menu")
            continue
    elif option == "3":
        delet = input("Do you really want to delete your historical? (Y/N)")
        if delet == "Y":
            historical_list.clear()
            print("Historical deleted sucessfully")
        elif delet == "N":
            print("Okay, return to the menu...")
        else:
            print("This option is not valid, back to the menu...")
    elif option == "4":
        print("Thanks for use this calculator! See you later...")
        exit()
    else:
        print("This option is not valid, return to the menu...")
        continue