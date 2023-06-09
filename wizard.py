import random as rnd

class Wizard:
    def __init__():
        Name = GenerateWizardName() 
        Level = GenerateWizardLevel()
        
def GenerateWizardName():
        wizard_name_index = rnd.randrange(0,len(possible_wizard_names))
        return possible_wizard_names[wizard_name_index]

def GenerateWizardLevel():
        return rnd.randrange(0,11)

possible_wizard_names = ["Uluq Ul Dudush", 
                             "Lost little boy", 
                             "Ravenlord", 
                             "Johnny Sins", 
                             "Xi Jingping",
                             "Autismo",
                             "Shrek"]

Name = ""
Level = 0


    
