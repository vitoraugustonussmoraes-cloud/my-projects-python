shopping_list = []
while True:
    print("Shopping list")
    print("1 - Add product")
    print("2 - Look products")
    print("3 - Delete product")
    print("4 - Total")
    print("5 - Exit")
    option = (input("Select: "))
    if option == "1":
        while True:
            name = input("Type the product: ")
            if name == "":
                print("The name cannot be empty!")
                continue
            price = float(input("Tapy the product price: "))
            if price == "":
                print("The price cannot be empty!")
                continue
            product = {
                "name": name,
                "price" : price
            }
            shopping_list.append(product)
            again = input("Press ENTER to add another product or type N to return to the menu").upper()
            if again == "":
                continue
            elif again == "N":
                break
            else:
                print("This opition is not valid, back to menu!")
                break
    elif option == "2":
        for product in shopping_list:
            print(f"{product['name']} - R${product['price']:.2f}")
        input("press ENTER to return to the menu...")
    elif option == "3":
        while True:
            product_name = input("What product do you want to remove? or press ENTER to return to the menu!")
            if product_name == "":
                break
            for product in shopping_list:
                if product_name == product["name"]:
                    shopping_list.remove(product)
                    print(f"{product_name} removed sucessfully!")
                    break
            else:
                print("This product is not in your list...")
    elif option == "4":
        total = 0
        for product in shopping_list:
            total += product["price"]
        print(f"Total = R${total:.2f}")
        input("Press ENTER to return to the menu...")
    elif option == "5":
        print("Thank you for use this app!")
        exit()
    else:
        becomemenu = input("This opition is not valid, do you want to return to the menu? (Y/N)")
        if becomemenu == "Y":
            continue
        elif becomemenu == "N":
            exit()
        else:
            print("This opition is not valid, we will direction you to menu :)")
            continue