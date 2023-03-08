import java.util.Random;

public class RandomGenerator {

    Random rnd = new Random();
    private final String[] deathMessages = new String[]{
            " pants set on fire ",
            " got shot in the face ",
            " perished painfully ",
            " got sent to gulag ",
            " got eradicated ",
            " purged ",
    };
    private final String[] Spells = new String[]{
            "Alakablam! ",
            "Communist Propaganda ",
            "12 Gauge Shotgun ",
            "Lightning bolt! ",
            "Your mom ",
            "Karate Chop ",
            "Bitch slap ",
            "Abra-Kadabra ",
            "Telekinesis "
    };
    public static int GenerateAttack(){
        Random rnd = new Random();
        int Attack = rnd.nextInt(11);
        return Attack;
    }
    public static void GenerateRandomWizard(){
        Wizard wizard = new Wizard();
        wizard.generateWizard();
    }
    public static int GeneratePlayerRoll(){
        Random rnd = new Random();
        int playerRoll = rnd.nextInt(11);
        return playerRoll;
    }
    public String getDeathMessage(){
        int randomDeathMessage = rnd.nextInt(deathMessages.length);
        return deathMessages[randomDeathMessage];
    }
    public String getSpells(){
        int randomSpell = rnd.nextInt(Spells.length);
        return Spells[randomSpell];
    }
}
