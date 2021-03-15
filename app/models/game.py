from app.models.player import *
from random import randint

choice = ["rock", "paper", "scissors"]

computer = choice[randint(0,2)]
player = input()

if player == computer:
    print("Draw!")
elif player == "rock" and computer == "paper":
    print("Computer Wins!")
elif player == "rock" and computer == "scissors":
    print("Player Wins!")
elif player == "paper" and computer == "rock":
    print("Player Wins!")
elif player == "paper" and computer == "scissors":
    print("Computer Wins!")
elif player == "scissors" and computer == "rock":
    print("Computer Wins!")    
elif player == "scissors" and computer == "paper":
    print("Player Wins!")






# player_wins = 0
# computer_wins = 0

# def choose_option():
#     player_choice = input("rock, paper, scissors")
#     if player_choice in ["rock"]:
#         player_choice = "Rock"
#     elif player_choice in ["paper"]:
#         player_choice = "Paper"
#     elif player_choice in ["scissors"]:
#         player_choice = "Scissors"   
#     else:
#         print("try again")
#     return player_choice

# def computer_option():

    