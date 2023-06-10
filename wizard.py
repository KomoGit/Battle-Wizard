class Wizard:

    # How class constructors are created. Use __init__():
    def __init__(self, name, level):
        self.Name = name
        self.Level = level


def battle(enemy_level, player_level):
    if enemy_level <= player_level:
        return True
    else:
        return False


Name = ""
Level = 0
