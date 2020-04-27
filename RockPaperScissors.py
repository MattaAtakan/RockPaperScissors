import time

print("Welcome to ROCK PAPER SCISSORS !")

loose = ("The computer wins")
win = ("You Win !")
lives = 5
score = 0
drew = 0
computer_lives = 7

print("_________________________________________________________________________________________")
print("_________________________________________________________________________________________")
print("")
print("  ________      _________        _________      _   __")
print(" |   __   |    |  _____  |      |  _______|    | | / /")
print(" |  |__| _|    | |     | |      | |            | |/ /")
print(" |  __  \      | |     | |      | |            |   /")
print(" |  | \  \     | |_____| |      | |_______     | |\ \ ")
print(" |__|  \__|    |_________|      |_________|    |_| \_\ ")
print("  ________        _          ________    ________    ________")
print(" |   ___  |      /_\        |   ___  |  |  ______|  |   __   |")
print(" |  |___| |     //_\\        |  |___| |  | |______   |  |__| _|") 
print(" |  ______|    / ___ \      |  ______|  |  ______|  |  __  \ ") 
print(" |  |         / /   \ \     |  |        | |______   |  | \  \ ")
print(" |__|        /_/     \_\    |__|        |________|  |__|  \__|") 
print("  _______                       _______     _______                             _______")
print(" / ______|     _________    _  / ______|   / ______|    _________    ________  / ______|")
print(" \ \_____     |  _______|  | | \ \_____    \ \_____    |  _____  |  |   __   | \ \_____")
print("  \_____ \    | |          | |  \_____ \    \_____ \   | |     | |  |  |__| _|  \_____ \ ") 
print("        \ \   | |          | |        \ \         \ \  | |     | |  |  __  \          \ \ ")
print("   _____/ /   | |_______   | |   _____/ /    _____/ /  | |_____| |  |  | \  \    _____/ /")
print("  |______/    |_________|  |_|  |______/    |______/   |_________|  |__|  \__|  |______/")
print("")
print("__________________________________________________________________________________________")
print("__________________________________________________________________________________________")

while True:
    rps = input("rock, paper, scissors?  ")
    time.sleep(5)
    import random
    computer = ("rock", "paper", "scissors")
    computer = random.choice(computer)
    

    if rps == "rock" and computer == "paper":
        print("The computer choose", computer)
        print()
        print(loose)
        print()
        lives -= 1
        print("You lose one point, your nb of lives now is",lives)    
    if rps == "rock" and computer == "scissors":
        print("The computer choose", computer)
        print()
        print(win)
        print()
        score += 1 
        computer_lives -= 1  
        print("You have won a point, your score is", score)
        print()
        print("Computer lost one life, it has", computer_lives, "lives")
        print()
        

    if rps == "paper" and computer == "scissors":
        print("The computer choose", computer)
        print()
        print(loose)
        print()
        lives -= 1 
        print("You lose one point, your nb of lives now is",lives)
        print()
    if rps == "paper" and computer == "rock":
        print("The computer choose", computer)
        print()
        print(win)
        print()
        score += 1 
        computer_lives -= 1 
        print("You have won a point, your score is", score)
        print()
        print("Computer lost one life, it has", computer_lives, "lives")
        print()

    if rps == "scissors" and computer == "rock":
        print("The computer choose", computer)
        print()
        print(loose)
        print()
        lives -= 1
        print("You lose one point, your nb of lives now is",lives)
        print()
    if rps == "scissors" and computer == "paper":
        print("The computer choose", computer)
        print()
        print(win)
        print()
        score += 1 
        computer_lives -=  1
        print("You have won a point, your score is", score) 
        print()
        print("Computer lost one life, it has", computer_lives, "lives")
        print()

    if rps == "rock" and computer == "rock":
        print("The computer choose", computer)
        print()
        print("You drew")
        print()
        drew += 1
    if rps == "paper" and computer == "paper":
        print("The computer choose",computer)
        print()
        print("Your drew")
        print()
        drew += 1
    if rps == "scissors" and computer == "scissors":
        print("The computer choose", computer)
        print()
        print("You drew")
        print()
        drew += 1  

    if lives == 0:
        print("You lost loser!")
        break  

    if score >= 5:
        lives += 1
        print("You scored 5 times you get one life","Your lives", lives)

    if computer_lives == 0:
        print("Computer died! You have won!")  
        break  
    
    else:
        print()
        print("Please enter one of the following : rock, paper of scissors")  
        print()                    
    


        