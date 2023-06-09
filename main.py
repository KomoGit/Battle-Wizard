import random as rnd

# Generates number from 0 to 10
def GenerateRandomInt():
    return rnd.randrange(0,11)

def GameLoop(gameActive,rawUserInput):
    while(gameActive):
        print("Hello Game is running...")

def TakeUserInput(rawUserInput):
    userInput = rawUserInput.upper()
    if(userInput == "A"):
        print(f"Player pressed {userInput}")
    elif(userInput == "B"):
        print(f"PLayer pressed {userInput}")


   
playerName = input("Greetings Wizard, Insert your name: ")
playerLevel = GenerateRandomInt()
print(f"Your name is {playerName}? What a stupid name! You are a level {playerLevel} wizard.")
input("Press any key to being...")
gameLoopActive = True
userInput = input()
GameLoop(gameLoopActive,userInput)

