import java.util.Scanner;

public class MainClass {

    static Scanner _userInput = new Scanner(System.in);
    public static String UserName;
    public static void main(String[] arguments){
        GenerateSession();
    }
    private static void GeneratePlayer(){
        UserName = _userInput.nextLine();
        if(UserName.equals("")){
            System.out.println("Please enter your name: ");
            GeneratePlayer();
        }
    }
    private static void StartGame(boolean loop){
        boolean gameLoop = loop;
        while (gameLoop){
            Wizard.GenerateWizard();
            GameLogic.GameLoop(_userInput);
        }
    }
    public static void GenerateSession(){
        System.out.println("Greetings Wizard, please insert your name: ");
        GeneratePlayer();
        System.out.println("Your name is " + UserName + "" + "? What a stupid name. \nPress Enter to Start!");
        _userInput.nextLine();
        StartGame(true);
    }
}
