import random as rnd
import wizard_generator as wiz_gen


# Generates number from 0 to 10
def generate_random_int():
    return rnd.randrange(1, 11)


def game_loop(game_active):
    while game_active:
        print("Press A to Attack || Press B to Run Away")
        print(wiz_gen.generate_wizard_name())
        input("Generate another")


def player_name_prompt():
    name_prompt_active = True
    while name_prompt_active:
        userinput = input("Greetings wizard, insert your name: ")
        if userinput.lower() == "exit":
            name_prompt_active = False
            print("Goodbye!")
            quit(0)
        elif userinput != "":
            name_prompt_active = False
            return userinput


playerName = player_name_prompt()
playerLevel = generate_random_int()
print(f"Your name is {playerName}? What a stupid name! You are a level {playerLevel} wizard.")
input("Press any key to being...")
gameLoopActive = True
userInput = input()
game_loop(gameLoopActive)
