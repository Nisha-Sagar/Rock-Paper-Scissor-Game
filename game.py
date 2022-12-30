import random

options = ("rock", "paper", "scissor")
running = True
u_score = 0
c_score = 0

while running:

    You = None
    computer = random.choice(options)

    while You not in options:
        You = input("\nEnter a choice (rock, paper, scissor):")
        if You not in options:
            print("Please enter a valid choice!")

    print(f"\n You: {You}")
    print(f" Computer: {computer}")

    if You == computer:
        print(" It's a Tie!")
        u_score = u_score + 0
        c_score = c_score + 0
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "rock" and computer == "scissor":
        print(" You win!")
        u_score = u_score + 1
        c_score = c_score + 0
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "rock" and computer == "paper":
        print(" Computer Wins!")
        u_score = u_score + 0
        c_score = c_score + 1
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "paper" and computer == "rock":
        print(" You win!")
        u_score = u_score + 1
        c_score = c_score + 0
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "paper" and computer == "scissor":
        print(" Computer Wins!")
        u_score = u_score + 0
        c_score = c_score + 1
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "scissor" and computer == "paper":
        print(" You win!")
        u_score = u_score + 1
        c_score = c_score + 0
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    elif You == "scissor" and computer == "rock":
        print(" Computer wins!")
        u_score = u_score + 0
        c_score = c_score + 1
        print("\nuser's score: ", u_score)
        print("computer's score: ", c_score)

    play_again = input("\nPlay again? (y/n): ").lower()
    if not play_again == "y":
        running = False
print("\nThanks for playing!\n")
