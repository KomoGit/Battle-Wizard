using System;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;

namespace Battle_Wizard
{
    class Program
    {
        static void Main(string[] args)
        {
        gameStart:
        
        Game Game = new Game();
        Game.gameStart();

            int playerLevel = NumberGenerator.generator.generateLevel();
            Console.WriteLine("You are a level " + playerLevel + " Wizard ");
            string Input;
            

            while (true) 
            {
                int EnemyLevel = NumberGenerator.generator.generateLevel();
                int enemyRoll = NumberGenerator.generator.generateEnemyRoll();
                int playerRoll = NumberGenerator.generator.generatePlayerRoll();
                string deathMessage = NumberGenerator.generator.generateDeathMessage();
                string spells = NumberGenerator.generator.generatespells();
                string wizardName = NumberGenerator.generator.generateWizardName();
                string wizardtaunts = NumberGenerator.generator.generatetaunts();


                if (playerRoll == enemyRoll)
                {
                    playerRoll += 1; //playerRoll can never be the same as enemyRoll and player has an advantage over this.
                }
                
                Console.WriteLine("A wild wizard named " + wizardName + " appeared " + "saying: " + wizardtaunts + " Foe is at level " + EnemyLevel); //Enemy Spawn
                if (playerLevel > EnemyLevel)
                {
                    Console.WriteLine("You have a chance to win this fight as he is lower level." + " What thy shall do?" + "\n Press A) To Cast spell." + "\n Press B) Run away!");
                    Input = Game.UserInput();
                }
                else if (playerLevel == EnemyLevel)
                {
                    Console.WriteLine("You are both level " + EnemyLevel + " What thy shall do?" + "\n Press A) To Cast spell." + "\n Press B) Run away!");
                    Input = Game.UserInput();
                }
                else
                {
                    Console.WriteLine("He is a higher level foe, you might want to be careful." + " What thy shall do?" + "\n Press A) To Cast spell." + "\n Press B) Run away!");
                    Input = Game.UserInput();
                }

                if ((Input == "a") || (Input == "A"))
                {
                    Console.WriteLine("You rolled " + playerRoll + " while enemy rolled " + enemyRoll); //Attacks
                    if (playerRoll < enemyRoll)
                    {
                        Console.WriteLine("You got " + deathMessage + "with" + spells);
                        break; //You should probably add playerlevel reference to here.

                    }
                    else
                    {
                        Console.WriteLine("He got " + deathMessage + "with " + spells);
                        Game.WaitAndClear();
                    }
                }
                else //Retreats.
                {
                    if (playerLevel < EnemyLevel)
                    {
                        Console.WriteLine("You ran away, how dishonorable.");
                        Game.WaitAndClear();
                    }
                    else
                    {
                        Console.WriteLine("You tried to run away, yet you perished by " + spells);
                        break;
                    }
                }
            }

            Console.WriteLine("Game over, do you wish to play again? Type 'Yes' to play"); //Game Over. Try again? Should move it to its own class.
            Input = Game.UserInput();
            if ((Input == "Yes") || (Input == "YES") || (Input == "yes"))
            {
                Console.Clear();
                goto gameStart;
            }
        }      
    }
}