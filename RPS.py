# import random
# li=["1.ROCK","2.PAPER","3.SCISSORS"]
# print("----Please enter '0' or 'Exit' to exit from game----")
# print("----------------------------------------------------")
# while (True):
#     for i in li:
#         print(i)
#     option=int(input("----Please select from below---"))
#     print("You Choose",li[option-1])
#     computer_choice=(random.choice(li))
#     print("Computer Choose",computer_choice)
#     if option==1:
#         if computer_choice=="SCISSORS":
#             print("You Won")
#         elif computer_choice=="ROCK":
#             print("No result")
#         else:
#             print("Computer Won")
#     if option==2:
#         if computer_choice=="ROCK":
#             print("You Won")
#         elif computer_choice=="PAPER":
#             print("No result")
#         else:
#             print("Computer Won")
#     if option==3:
#         if computer_choice=="SCISSORS":
#             print("You Won")
#         elif computer_choice=="SCISSORS":
#             print("No result")
#         else:
#             print("Computer Won")






# import random

# li = ["1.ROCK", "2.PAPER", "3.SCISSORS"]

# print("----Please enter '0' to exit from game----")
# print("----------------------------------------------------")

# while True:
#     for i in li:
#         print(i)

#     option = int(input("----Please select from below---: "))

#     if option == 0:
#         print("Game Exited")
#         break

#     user_choice = li[option - 1]
#     computer_choice = random.choice(li)

#     print("You Choose", user_choice)
#     print("Computer Choose", computer_choice)

#     # OPTION 1: ROCK
#     if option == 1:
#         if computer_choice == "3.SCISSORS":
#             print("You Won")
#         elif computer_choice == "1.ROCK":
#             print("No result")
#         else:
#             print("Computer Won")

#     # OPTION 2: PAPER
#     if option == 2:
#         if computer_choice == "1.ROCK":
#             print("You Won")
#         elif computer_choice == "2.PAPER":
#             print("No result")
#         else:
#             print("Computer Won")

#     # OPTION 3: SCISSORS
#     if option == 3:
#         if computer_choice == "2.PAPER":
#             print("You Won")
#         elif computer_choice == "3.SCISSORS":
#             print("No result")
#         else:
#             print("Computer Won")

#     print("----------------------------------------------------")


# Rock Paper Scissor Game
import random as re

def game(li:list)->str:
    return re.choice(li)

def cheeck(User:str,Computer:str)->str:
    return "Game Tie" if (User == Computer) else "Game Winner is You" if(User == "Rock" and Computer == "Scissors") else "Game Winner is You" if (User == "Paper" and Computer == "Rock") else "Game Winner is You" if (User == "Scissors" and Computer == "Paper") else "Game Winner is Compuer" 
print("----- Welcome To Rock 🪨, Paper 📃 and Scissors ✂️  Game -----")
print("You can Enter Upper case or Lower Case => R/P/S\nR => Rock\nP => Paper\nS => Scissors")
li = {"R":"Rock","P":"Paper","S":"Scissors"}

while True:
    temp = input("Your Tuen Enter R/P/S or Q for Quit : ").upper()
    if temp == "Q":
        print("-----Game Over-----")
        break
    elif temp in list(li.keys()):
        user_response = li[temp]
        Computer_response = game(list(li.values()))
        print(f"\nYou Choice : {user_response}\nComputer Choice : {Computer_response} \n-----"+cheeck(user_response,Computer_response)+"-----\n")
    else:
        continue