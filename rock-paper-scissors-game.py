###########ROCK,  PAPEL OR SCISSORS###########
def start_game():
    if user == computer:
        print("Draw")
    elif user == "rock" and computer == "paper":
        print("You lose")
    elif user == "rock" and computer == "scissor":
        print("You won!")
    elif user == "paper" and computer == "rock":
        print("You won!")         
    elif user == "paper" and computer == "scissor":
        print("You lose")         
    elif user == "scissor" and computer == "rock":
        print("You lose")         
    elif user == "scissor" and computer == "paper":
        print("You won!")
    else:
        ("This option is not valid")
options = ["rock", "paper", "scissor"]
print("""
Let's play rock, paper or scissors!
1 - rock
2 - paper
3 - scissor
4 - exit
""")
while True:
    user = input("Select your option: ")
    if user == "1":
        user = "rock"
    elif user == "2": 
        user = "paper"
    elif user == "3":
        user = "scissor"
    else:
        print("This option is not valid")
        break
    import random
    computer = random.choice(options)
    start_game()
    print(f"""
    Your option: {user} 
    Computer option: {computer}
    """)

    