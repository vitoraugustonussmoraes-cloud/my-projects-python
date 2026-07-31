#================ USER MANAGEMENT SYSTEM ==================
print("Welcome to user registration!")
look_user = {}
def show_menu():
    print("""
    Menu options:
    1 - Register User
    2 - Login
    3 - List Users
    4 - Search User
    5 - Edit User 
    6 - Delete User
    7 - Exit
    """)
    menuoption = input("Select: ")
    return menuoption
def register_user():
    username = (input("Tapy your username: "))
    fullname = (input("What's your full name? "))
    age = (input("How old are you? "))
    email = (input("What's your e-mail? "))
    password = (input("Write a safe password: "))
    look_user[username] = {
        "fullname": fullname,
        "age": age,
        "email": email,
        "password": password
    }
    print(look_user)
def login_user():
    username = input("Type your username: ")
    if username in len(look_user):
        password = input("Tapy your password: ")
        if password == password(look_user):
            print(f"Welcome {username}!")
def list_user():
    print(look_user)
def search_user():
    user = input("Type the username you want to found: ")
    if user in len(look_user):
        look_user.remove("password")
        print(f"{user}")
    else:
        print("User not found...")
def edit_user():
    def delete_user():
        user = input("Type the username of user you want to delete: ")
    if user in len(look_user):
        sure = input(f"Are you sure about delete {user}? (Y/N)")
        if sure.lower() == "y":
            look_user.remove(user)
        elif sure.lower() == "n":
            print("Press ENTER to return to the menu")
        else:
            print("Press ENTER to return to the menu")
while True:
    menuoption = show_menu()
    if menuoption == "1":
        user = register_user()
    elif menuoption == "2":
        login_user()
    elif menuoption == "3":
        list_user()
    elif menuoption == "4":
        search_user()
    elif menuoption == "5":
        edit_user()
    elif menuoption == "6":
        delete_user()
    elif menuoption == "7":
        break
    else:
        ("This option is not valid")
        break