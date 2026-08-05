# VIRTUAL STORE #
show_stock = {}
code = 0
def show_menu():
    print("""
    Welcome to your Virtual Store!
    Menu Select:
    1 - Add products
    2 - Delete products
    3 - Show Stock
    4 - 
    5 - 
    6 -
    7 -
    8 -
    """)
    select = input("Select: ")
    return select
def add_product(code):
    add = input("Type ENTER if you you want to add a product, if you want to return to the menu press any key")
    if add == "":
        name = input("Type the product name: ")
        price = float(input("Type the price: "))
        quantity = int(input("Type the quantity you want to add: "))
        priceinstock = price * quantity
        print(f"""
            Product registered sucessfully!
            "Product:" {name}
            "Price:" {price}
            "Quantity:" {quantity}
            "Price in stock:" {priceinstock}
        """)
    else: 
        return code
    code = code + 1
    print(f"The product code is 000{code}")
    show_stock[code] = {
        "Product": name,
        "Price": price,
        "Quantity": quantity,
        "Price in stock:": priceinstock
               }
    return code
def delete_product():
    pass
def show_products():
    if show_stock == {}:
        print("No products yet")
    else:
        print(f"""
        This is your products list!
        show_stock[code] = 
            "Product: {show_stock[code]['product']}"
            "Price: {show_stock[code]['price']}"
            "Quantity: {show_stock[code]['quantity']}"
            "Price in stock: {show_stock[code]['priceinstock']}"
        """)

while True:
    print("""
    Welcome to your Virtual Store!
    Menu Select:
    1 - Add products
    2 - Delete products
    3 - Show Stock
    4 - Sell
    5 - History Sell
    6 - Show low stock
    7 - Edit Products
    8 - Exit
    """)
    select = input("Select: ")
    if select == "1":
        code = add_product(code)
    elif select == "8":
        exit()