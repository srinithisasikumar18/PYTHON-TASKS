
#Rock Paper Scissors Game 

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

import random

li = ["ROCK", "PAPER", "SCISSORS"]

print("----Please enter '0' to exit from game----")
print("-----------------------------------------")

while True:
    print("1.ROCK")
    print("2.PAPER")
    print("3.SCISSORS")

    option = input("----Please select from below--- ")

    if option == "0" or option.lower() == "exit":
        print("Game Exited")
        break

    option = int(option)

    user_choice = li[option - 1]
    print("You Choose:", user_choice)

    computer_choice = random.choice(li)
    print("Computer Choose:", computer_choice)

    if user_choice == computer_choice:
        print("No result (Draw)")

    elif user_choice == "ROCK":
        if computer_choice == "SCISSORS":
            print("You Won")
        else:
            print("Computer Won")

    elif user_choice == "PAPER":
        if computer_choice == "ROCK":
            print("You Won")
        else:
            print("Computer Won")

    elif user_choice == "SCISSORS":
        if computer_choice == "PAPER":
            print("You Won")
        else:
            print("Computer Won")

    print("-----------------------------------------")
