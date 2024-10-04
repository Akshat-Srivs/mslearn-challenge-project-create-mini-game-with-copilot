import random

list = ["r" , "p" , "s"]   #R --> Rock ; P --> Paper ; S --> Scissors
h=True                  #variable for the loop termination 
rounds = 0              #stores the number of rounds
score = 0               #stores' the players scores
while (h) :

    print("r --> Rock ; p --> Paper ; s --> Scissors " )
    u_in = input(("Enter your Choice: ")).lower()

    print("Your Choice: ",u_in)
    c_in = random.choice ( list )
    
    print("Opponent's Choice: ",c_in)
    
    if (u_in not in list ) :
        print("Invalid Choice\nChoose again: ")
        continue
    elif ( c_in == u_in ):
        print ("DRAW ")
    elif ( (c_in == "r" and u_in == "s") or (c_in == "p" and u_in == "r") or (c_in == "s" and u_in == "p")):
        print ("LOSE\nBETTER LUCK NEXT TIME")
    else:
        print ("YOU WIN")
        score += 1
    
    rounds += 1

    h = True if input("Enter Y to play again or any other key to exit: ").lower() == "y" else False 

print(f"Number of Rounds: {rounds}")
print(f"Your Score: {score}")
