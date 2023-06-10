import random as rnd

possible_wizard_names = ["Uluq Ul Dudush", "Lost little boy",
                         "Ravenlord", "Johnny Sins",
                         "Xi Jingping", "Autismo",
                         "Joe Biden",
                         "Shrek"]

possible_spells = ["Alakablam", "Y0ur m0m ", "Karate Chop", "Abra-kadabra ", "12 Gauge Shotgun",
                   "Telekinesis", "Communist Propaganda", "Bitch Slap"]

possible_taunts = ["What's chilling my guy? I hope you are doing well! :)",
                   "I have lost my mommy, do you know where she is? :(",
                   "Never bring a gun to a spell fight!",
                   "This guy really thinks he is Merlyn, get this get this.",
                   "Huh? How did I end up here?",
                   "My iq is 400! You have no chance!"]

possible_death_messages = ["pants set on fire by", "shot in the face with a", "perished painfully with",
                           "sent to gulag"]


def generate_random_int():
    return rnd.randrange(1, 11)


def generate_death_message():
    death_msg_index = rnd.randrange(0, len(possible_death_messages))
    return possible_death_messages[death_msg_index]


def generate_random_spell():
    spell_index = rnd.randrange(0, len(possible_spells))
    return possible_spells[spell_index]


def generate_wizard_name():
    wizard_name_index = rnd.randrange(0, len(possible_wizard_names))
    return possible_wizard_names[wizard_name_index]


def generate_wizard_level():
    return rnd.randrange(0, 11)
