import random

# Display available operations
options=["rock","paper","scissors"]

# score
my_score=0
com_score=0

running= True
while running:
    player=None
    computer=random.choice(options)

# Input from the user
    while player not in options:
        player=input("enter a choice(  rock,    paper,  scissors  ): ")
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if (player==computer):
        print("Tie!!❇️")

    elif(player==   "rock⛰️"   and computer==   "scissors✂️"   ):
        my_score+=1
        print("You Win! 😎")
    elif(player==   "paper📝"    and computer ==  "rock⛰️"      ):
        my_score+=1
        print("You Win!😎 ")

    elif(player==   "scissors✂️" and computer== "paper📝"    ):
        my_score+=1
        print("You Win! 😎")

# Display the result
    else:
    

        com_score+=1
    print("Computer Win! :computer:","My_Score",my_score,"Computer _Score",com_score)
    play_again= input("play again?(yes/no):").lower()


    if not play_again=="yes":
        running=False


print("Thanks For Playing")

#THANKYOU

    