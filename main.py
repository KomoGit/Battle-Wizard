import random as rnd
import wizard as w
import wizard_generator as wiz_gen


# Generates number from 0 to 10
def generate_random_int():
    return rnd.randrange(1, 11)


def interpret_user_input(inpt, wizard):
    if inpt.upper() == "A":
        if w.battle(wizard.Level, player_level=playerLevel):
            print(f"You killed {wizard.Name} with a spell.")
        else:
            print(f"{wizard.Name} killed you with a spell.")
            exit(0)
    elif inpt.upper() == "B":
        print("Player Pressed B")
    elif inpt.upper() == "C":
        print(f"You are level - {playerLevel}, While the enemy is {wizard.Level}")
    else:
        print("Invalid input.")


def game_loop(game_active):
    while game_active:
        enemy = w.Wizard(wiz_gen.generate_wizard_name(), generate_random_int())
        print(f"A wild wizard named {enemy.Name} appeared. Wizard is level : {enemy.Level}")
        print("Press A to Attack || Press B to Run Away || Press C to Show Stats")
        interpret_user_input(input(), enemy)


# This thing is only used once at the start of the game.
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
gameLoopActive = True
game_loop(gameLoopActive)
