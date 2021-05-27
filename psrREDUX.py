import random #this is the imported random library to make the bot choice ramdom
hands=["paper","scissors","rock"]

user_score = 0

while user_score != 3:
    user_input = input("Choose rock, paper, scissors:")
    bot_choice = random.choice(hands)

#this is if the user and bot choice is the same
    if user_input.lower() == bot_choice:
        print("")
        print("Same choice please try again")
        print("")
        user_input = input("Choose: Rock, Paper, Scissors")

#these are the choices deciding who wins

    if user_input == "scissors" and bot_choice == "rock":
       print("")
       print("Bot chose Rock, Bot wins")
       print("")
       user_score += 1
       
    elif user_input == "rock" and bot_choice == "paper":
       print("")
       print("Bot chose paper, Bot wins")
       print("")
       user_score += 1
       
    elif user_input == "paper" and bot_choice == "scissors":
       print("")
       print("Bot chose scissors, Bot wins")
       print("")
       user_score +=1
       
    elif user_input == "rock" and bot_choice == "scissors":
       print("")
       print("Bot chose paper, You win")
       print("")
 
    elif user_input == "paper" and bot_choice == "rock":
       print("")
       print("Bot chose rock, You win")
       print("")
       
    elif user_input == "scissors" and bot_choice == "paper":
       print("")
       print("Bot chose paper, You win")
       print("")

#if you lose!
print("YOU LOSE!")       
print("")
print("Userscore = ", user_score)
