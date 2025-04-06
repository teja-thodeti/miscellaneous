import random
while True:
    choices=["rock","paper","scissors"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock or paper or scissors ? :").lower()
    if player==computer:
        print("computer choice :",computer)
        print("your choice :",player)
        print("tie :)")
    elif player == "rock":
        if computer == "paper":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you lose")
        if computer=="scissors":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you win")
    elif player=="scissors":
        if computer=="rock":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you lose")
        if computer=="paper":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you win")
    elif player=="paper": 
        if computer=="rock":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you win")
        if computer=="scissors":
            print("computer choice :",computer)
            print("your choice :",player)
            print("you lose")
    again=input("want to play again(yes/no) : ")
    if again !="yes":
        break
print("see you again!!")

      
