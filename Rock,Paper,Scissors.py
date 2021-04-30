# Start Of The Code :)

import random
# Welcome Note
print("Welcome To The Rock,Paper,Scissors Game :)")

# The Blank Prints Are For Spaces
print()

# Score Vars Declaration(Take Them Inside While Loop For Resetting the scores with the game)
comp_score = 0
user_score = 0
# Max Score Input
u = int(input("Enter The Maximum Score ,You Want:"))

# Forever Loop
while user_score !=  10 or comp_score !=  10:
    # vars declaration
    x = input("Choose Rock,Paper,Scissors:")
    y = ["Rock","Paper","Scissors"]
    z = random.choice(y)


    # Paper Situations
    if x == "Paper" and z == "Scissors":
        print("You Lost, Ai Chose",z)
        comp_score = comp_score + 1

    if x == "Paper" and z == "Rock":
        print("You Won, Ai Chose",z)
        user_score = user_score + 1

    if x == "Paper" and z == "Paper":
        print("Tie")   
  
    # Rock Situations
    if x == "Rock" and z == "Paper":
        print("You Lost, Ai Chose",z)
        comp_score = comp_score+1

    if x == "Rock" and z == "Scissors":
        print("You Won, Ai Chose",z)
        user_score = user_score + 1

    if x == "Rock" and z == "Rock":
        print("Tie")  

    # Scissors Situations
    if x == "Scissors" and z == "Paper":
        print("You Won, Ai Chose",z)
        comp_score = comp_score + 1

    if x == "Scissors" and z == "Rock":
        print("You Lost, Ai Chose",z)
        user_score = user_score + 1

    if x == "Scissors" and z == "Scissors":
        print("Tie") 

    print()    
    print("Ai Score:",comp_score)
    print("Your Score:",user_score)
    print()
    
    if comp_score == u:
     print("You Lost, Try Again")
     break 
    if user_score == u:
     print("You Won, GG's")
     break 

    
# End Of The Code :)