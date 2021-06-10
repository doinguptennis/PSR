import random #this is the imported random library to make the bot choice random

hands = ["paper","scissors","rock"] # this is the list of possible bot choices
user_compliments = ["Although you played well", "Please play again!", "This code is the best"] # this is the list of compliments given to the user at the end of the program to boost the morale

lose_tokens = 0 # each time a match is lost a token will be given to a user

print("Welcome to a program written by Leon ford and Liam howden!")
print("")
print("Rules:")
print("1. If you lose 3 times the program will end")
print("")
while lose_tokens != 3:
    user_input = input("Choose rock, paper, scissors:")
    bot_choice = random.choice(hands)

# this is if the user and bot choice is the same
    if user_input.lower() == bot_choice:
        print("")
        print("Same choice please try again")
        print("")

# these are the choices deciding who wins

    if user_input == "scissors" and bot_choice == "rock":
       print("")
       print("Bot chose Rock, Bot wins")
       print("")
       lose_tokens += 1
       
    elif user_input == "rock" and bot_choice == "paper":
       print("")
       print("Bot chose paper, Bot wins")
       print("")
       lose_tokens += 1
       
    elif user_input == "paper" and bot_choice == "scissors":
       print("")
       print("Bot chose scissors, Bot wins")
       print("")
       lose_tokens +=1
       
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

# The statement that prints if 3 lose_tokens are reached
print("YOU LOSE!")       
print("")
print(random.choice(user_compliments))
print("")
print("Rounds lost = ", lose_tokens)
