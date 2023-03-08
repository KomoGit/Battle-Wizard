import java.util.Scanner;

public class GameLogic extends MainClass {
    RandomGenerator rng = new RandomGenerator();
    private static String deathMessage;
    private static String usedSpell;


    public static void GameLoop(Scanner input){
        System.out.println("What do you wish to do?\nPress A) To Attack\nPress B) To Run Away");
        String userInput = input.nextLine();
        if(userInput.equals("A")){
            determineAttackWinner();
        }
        if(userInput.equals("B")){
            determineEscape();
        }
    }
    private static void determineAttackWinner(){
        RandomGenerator rng = new RandomGenerator();
        int playerRoll = RandomGenerator.GeneratePlayerRoll() + 1;
        int wizardRoll = RandomGenerator.GenerateAttack();
        deathMessage = rng.getDeathMessage();
        usedSpell = rng.getSpells();
        String wizName = Wizard.returnWizName();
        System.out.println("You rolled " + playerRoll + " While the wizard rolled " + wizardRoll);
        if(playerRoll > wizardRoll){
            System.out.println(wizName + deathMessage + usedSpell);
        }
        else
        {
            System.out.println(MainClass.UserName + deathMessage + " with " +usedSpell);
            terminateGame();
        }
    }
    private static void determineEscape(){
        int wizLevel = Wizard.returnLevel();
        String wizName = Wizard.returnWizName();
        if(wizLevel < 5){
            System.out.println("You were successfully able to flee!");
        }
        else{
            System.out.println("While trying to flee "+ wizName + deathMessage + usedSpell);
            terminateGame();
        }
    }
    public static void GameEndMenu(Scanner input){
        System.out.println("Would you like to try again\n");
        System.out.println("Press A To Try Again\nPress B To Quit");
        String userInput = input.nextLine();
        if(userInput.equals("A")){
            MainClass.GenerateSession();
        }
    }
    public static boolean terminateGame(){
        return true;
    }
}
