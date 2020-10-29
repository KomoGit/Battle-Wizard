using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace Battle_Wizard
{
    class PlayerClass
    {
        //public int playerRoll;
        public string Player = Console.ReadLine();
        public void playerName()
        {
            switch (this.Player) //These are the names for player. Only serve easter egg purposes, nothing else.
            {  //This class will also hold level system, experience, and play exclusive spells.
                case "Elnur":
                    Console.WriteLine("Welcome God! " + "\nPress any button to begin.");
                    Console.ReadKey();
                    break;
                case "Snake":
                    Console.WriteLine("Kept you waiting huh? " + "\nPress any button to begin.");
                    Console.ReadKey();
                    break;
                case "Raiden":
                    Console.WriteLine("It's time for Jack, to let er' rip! " + "\nPress any button to begin.");
                    Console.ReadKey();
                    break;
                case "Developer":
                    Console.WriteLine("Developer Mode On.");
                    Console.ReadKey();
                    break;
                default:
                    Console.WriteLine("Your name is? " + Player + " What a stupid name." + "\nPress any button to begin.");
                    Console.ReadKey();
                    break;
            }
        }       
    }
}
