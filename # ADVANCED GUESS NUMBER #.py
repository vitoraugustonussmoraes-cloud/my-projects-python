# ADVANCED GAME GUESS NUMBER #
def choose_dificult():
    dif = input("""
    Select the difficult:
    1 - easy (1 - 50)
    2 - medium (1 - 100)
    3 - hard (1 - 1000)
    """)
    return(dif)
def check_secret(dif):
    import random
    if dif == "1":
        secret_number = random.randint(1, 50)
    elif dif == "2":
        secret_number = random.randint(1, 100)
    elif dif == "3":
        secret_number = random.randint(1, 1000)
    else:
        print("Option is not valid")
        return
    return(secret_number)
def play_game(attemps, secret_number):
    guess = int(input("Guess the number: "))
    attemps += 1
    if guess == secret_number:
        print(f"You won in {attemps} attemps!")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")
    return(attemps)
while True:
    players = input("""
Welcome to guess number!
Do you want to play with 1 or 2 players?
""")
    if players == "1":
        while True:
            dif = choose_dificult()
            attemps = 0
            secret_number = check_secret(dif)
            while True:
                attemps = play_game(attemps, secret_number)


