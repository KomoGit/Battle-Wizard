class Wizard:

    # How class constructors are created. Use __init__():
    def __init__(self,name,level):
        self.Name = name #GenerateWizardName() 
        self.Level = level #GenerateWizardLevel()

def BattleWizard(playerLevel ):
    if(Level <= playerLevel):
        return True
    else:
        return False
             
Name = ""
Level = 0

