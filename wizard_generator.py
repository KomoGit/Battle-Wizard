import random as rnd

possible_wizard_names = ["Uluq Ul Dudush",
                         "Lost little boy",
                         "Ravenlord",
                         "Johnny Sins",
                         "Xi Jingping",
                         "Autismo",
                         "Shrek"]


def generate_wizard_name():
    wizard_name_index = rnd.randrange(0, len(possible_wizard_names))
    return possible_wizard_names[wizard_name_index]


def generate_wizard_level():
    return rnd.randrange(0, 11)
