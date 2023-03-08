import java.util.Random;

public class Wizard {
    Random rnd = new Random();
    private static String wizName;
    private static String wizTaunt;
    private static int wizLevel;
    private static String wizDeathMessage;
    private static String wizUsedSpell;

    private final String[] WizardNames = new String[]{
            "Mario",
            "Homer",
            "Jack McFly",
            "Panda",
            "Uluq Ul Dudu-sh",
            "Grukk",

    };
    private final String[] WizardTaunts = new String[]{
            "Doh!",
            "Uh oh, this isn't a wizard, it is a lost child!",
            "Shadows will consume you!",
            "Hah Got-em",
    };
    public static void GenerateWizard(){
        Wizard wiz = new Wizard();
        RandomGenerator rng = new RandomGenerator();
        wizName = wiz.GetWizardName();
        wizTaunt = wiz.getWizardTaunt();
        wizDeathMessage = rng.getDeathMessage();
        wizUsedSpell = rng.getSpells();
        wizLevel = wiz.GetWizardLevel();
        System.out.println("A wild wizard named "+wizName + " appeared. Saying: " + wizTaunt + " Wizard is level " + wizLevel);
    }
    public void generateWizard(){
        GenerateWizard();
    }

    public String GetWizardName(){
        int randomName = rnd.nextInt(WizardNames.length);
        return WizardNames[randomName];
    }
    public String getWizardTaunt(){
        int randomTaunt = rnd.nextInt(WizardTaunts.length);
        return WizardTaunts[randomTaunt];
    }

    public int GetWizardLevel(){
        return rnd.nextInt(11);
    }
    public static int returnLevel(){
        return wizLevel;
    }
    public static String returnDeathMessage(){
        return wizDeathMessage;
    }
    public static String returnUsedSpell(){
        return wizUsedSpell;
    }
    public static String returnWizName(){
        return wizName;
    }

}
