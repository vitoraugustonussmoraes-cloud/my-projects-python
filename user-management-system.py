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
    while True:
        username = (input("Type your username: "))
        if username in look_user:
            print("This username is in use")
            continue
        break
    fullname = (input("What's your full name? "))
    while True:
        age = int(input("How old are you? "))
        if not 14 <= age <= 120:
            print("Type you real age")
            continue
        break
    while True:
        email = (input("What's your e-mail? "))
        if "@" not in email:
            print("This email is not valid")
            continue
        break 
    while True:
        password = (input("Write a safe password: "))
        min = len(password)
        if min >= 8:
            if not any(char.isalpha() for char in password):
                print("Your password needs to have 8 characters, 1 letter and 1 number")
                continue
            if not any(char.isdigit() for char in password):
                print("Your password needs to have 8 characters, 1 letter and 1 number")
                continue
            confirm = input("Confirm your password: ")
            if password == confirm:
                print("Acepted password!")
            else:
                print("Invalid password")
                continue
        else:
            print("Your password needs to have 8 characters, 1 letter and 1 number")
            continue
        break
    look_user[username] = {
        "fullname": fullname,
        "age": age,
        "email": email,
        "password": password
    }
    print(look_user)
def login_user():
    username = input("Type your username: ")
    if username in look_user:
        password = input("Type your password: ")
        if password == look_user[username]["password"]:
            print(f"Welcome {username}!")
        else:
            print("Incorrect password")
            return
    else: 
        print("Username was not found")
        return
def list_user():
    if not look_user:
        print("There are no users registed")
        return
    for username in look_user:
        print(username)
def search_user():
    username = input("Type the username you want to find: ")
    if username in look_user:
        print(f"Username: {username}")
        print(f"Fullname: {look_user[username]['fullname']}")
        print(f"Age: {look_user[username]['age']}")
        print(f"Email: {look_user[username]['email'] }") 
    else:
        print("User was not found")
def edit_user():
    username = input("Type the username you want to edit: ")
    if username in look_user:
        edit = input("""What do you want to edit?: 
        1 - Full name
        2 - Age
        3 - Email
        4 - Password tapy
        """)
        if edit == "1":
            newfullname = input("Type the new full name: ")
            look_user[username]['fullname'] = newfullname
        elif edit == "2":
            newage = input("Type the new age: ")
            look_user[username]['age'] = newage
        elif edit == "3":
            newemail = input("Type your new email: ")   
            look_user[username]['email'] = newemail
        elif edit == "4":
            probablypassword = input("To edit your password, type the actual password: ")
            if probablypassword == look_user[username]['password']:
                newpassword = input("Type your new password: ")
                look_user[username]['password'] = newpassword
            else:
                print("Password Invalid")
        else: 
            print("Option is not valid")
    else:
        print("User was not found")
def delete_user():
    username = input("Type the username of user you want to delete: ")
    if username in (look_user):
        sure = input(f"Are you sure about delete {username}? (Y/N)")
        if sure.lower() == "y":
            del look_user[username]
        else:
            print("Press ENTER to return to the menu")
    else:
        print("User was not found")
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
        exit()
    else:
        print("This option is not valid")
        break