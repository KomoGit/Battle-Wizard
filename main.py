import random as rnd

# Generates number from 0 to 10
def GenerateRandomInt():
    return rnd.randrange(0,11)

def GameLoop(gameActive):
    while(gameActive):
        print("Press A to Attack || Press B to Run Away")
        userInput = input().upper
        # ValidateUserInput(userInput)

# def ValidateUserInput(userInput):
#    if(userInput == "A"):
#        return  
   
playerName = input("Greetings Wizard, Insert your name: ")
playerLevel = GenerateRandomInt()
print(f"Your name is {playerName}? What a stupid name! You are a level {playerLevel} wizard.")
input("Press any key to being...")
gameLoopActive = True
userInput = input()
GameLoop(gameLoopActive,userInput)

