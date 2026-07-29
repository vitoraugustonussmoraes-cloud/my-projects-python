print("Try to guess the number!")
players = int(input("Do you wanna play with 1 or 2 players?"))
if players == 1:
        name = (input("What's your name?"))
        import random
        secret_number = random.randint(1, 100)
        attempts = 0
        while True:
            guess = int(input("Guess the number: "))
            attempts = attempts + 1
            if guess == secret_number:
                print(f"Congratulations {name} you won in {attempts} attempts!")
                break
            elif guess > secret_number:
                print("Too high")
            else:
                print("Too low")
elif players == 2:
        player1 = (input("What's the name of player 1?"))
        player2 = (input("What's the name of player 2?"))
        import random
        secret_number = random.randint(1, 100)
        attempts = {
              player1: 0,
              player2: 0
        }
        while True:
            guess = int(input(f"{player1}, guess the number: "))
            attempts[player1] = attempts[player1] + 1
            if guess == secret_number:
                print(f"Congratulations {player1}, you won in {attempts[player1]} attempts!")
                break
            elif guess > secret_number:
                 print("Too high")
            else:
                 print("Too low")
            guess = int(input(f"{player2}, guess the number: "))
            attempts[player2] = attempts[player2] + 1
            if guess == secret_number:
                print(f"Congratulations {player2}, you won in {attempts[player2]} attempts!")
                break
            elif guess > secret_number:
                    print("Too high")
            else:
                   print("Too low")
else:
        print("Invalid option")