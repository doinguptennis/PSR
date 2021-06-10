import random #this is the imported ramdom code flie to make the bot choice ramdom
hands=["paper","scissors","rock"]

user_input = input("Chose rock, paper, scissors:")
bot_choice = random.choice(hands)

#this is
if user_input.lower() == bot_choice:
    print("")
    print("same choice please try again")
    print("")
    user_input = input("Chose Rock, Paper, Scissors")


elif user_input == "scissors" and bot_choice == "rock":
   print("Bot chose Rock Bot wins")
 
elif user_input == "rock" and bot_choice == "paper":
   print("Bot chose paper Bot wins")

elif user_input == "paper" and bot_choice == "scissors":
   print("Bot chose scissors Bot wins")

elif user_input == "scissors" and bot_choice == "rock":
   print("Bot chose Rock Bot wins")
