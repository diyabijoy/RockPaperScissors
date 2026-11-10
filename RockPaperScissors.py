import random
game_list = ("R","P","S")
gen_score = 0
user_score = 0

print("ROCK - PAPER - SCISSORS\n")

while(gen_score<5 and user_score<5):
     gen_choice = random.choice(game_list)
     user_choice = input(f"Score:{user_score}-{gen_score}. Choose (R/P/S):").upper()

     if (gen_choice == "R" and user_choice == "R"):
        print("R--Play again!")
     elif (gen_choice == "P" and user_choice == "R"):
          print("P--You lose!")
          gen_score += 1
     elif (gen_choice == "S" and user_choice == "R"):
          print("S--You win!")
          user_score += 1

     elif (gen_choice == "R" and user_choice == "P"):
        print("R--You win!")
        user_score += 1
     elif (gen_choice == "P" and user_choice == "P"):
          print("P--Play again!")
     elif (gen_choice == "S" and user_choice == "P"):
          print("S--You lose!")
          gen_score += 1

     elif (gen_choice == "R" and user_choice == "S"):
        print("R--You lose!")
        gen_score += 1
     elif (gen_choice == "P" and user_choice == "S"):
          print("P--You win!")
          user_score += 1
     elif (gen_choice == "S" and user_choice == "S"):
          print("S--Play again!")
     else:
          print("Invalid choice")
if(user_score >= 5):
  print("Congrats!You WON the game!")
else:
  print("You LOST...")