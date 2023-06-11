import wizard as w
import generator as gen


def interpret_user_input(inpt, wizard):
    if inpt.upper() == "A":
        if w.battle(wizard.Level, player_level=playerLevel):
            print(f"You killed {wizard.Name} with spell: \"{gen.generate_random_spell()}\"")
            return True
        else:
            print(f"{wizard.Name} killed you with spell: \"{gen.generate_random_spell()}\"")
            return False
    elif inpt.upper() == "B":
        if wizard.Level > gen.generate_random_int():
            print(f"You successfully escaped {wizard.Name}")
        else:
            print(f"{wizard.Name} killed you with spell: \"{gen.generate_random_spell()}\"")
            return False
    else:
        print("Invalid input.")


def game_loop():
    while True:
        enemy = w.Wizard(gen.generate_wizard_name(), gen.generate_random_int())
        print(f"A wild wizard named {enemy.Name} appeared. Wizard is level : {enemy.Level}")
        print("Press A to Attack || Press B to Run Away")
        stat = interpret_user_input(input(), enemy)
        if not stat:
            break


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


while True:
    playerName = player_name_prompt()
    playerLevel = gen.generate_random_int()
    print(f"Your name is {playerName}? What a stupid name! You are a level {playerLevel} wizard.")
    game_loop()
    print("Do you wish to play again? A (Yes) | B (No)")
    player_input = input()
    if player_input.upper() == "B":
        print("Goodbye!")
        break
