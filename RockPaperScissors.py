import random

choices = {
    "R": "rock",
    "P": "paper",
    "S": "scissors"
}

# The key beats the value
beats = {
    "R": "S",
    "P": "R",
    "S": "P"
}

computer_score = 0
user_score = 0

while computer_score < 5 and user_score < 5:
    user_choice = input("Choose R (rock), P (paper), or S (scissors): ").upper()

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(list(choices))

    print(f"You chose {choices[user_choice]}.")
    print(f"Computer chose {choices[computer_choice]}.")

    if user_choice == computer_choice:
        print("Draw!")
    elif beats[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score: You {user_score} - Computer {computer_score}\n")

if user_score == 5:
    print("You won the game!")
else:
    print("Computer won the game!")