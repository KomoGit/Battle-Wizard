using System;
using System.Collections.Generic;
using System.Text;

namespace Battle_Wizard
{
    public class NumberGenerator
    {
        public static NumberGenerator generator = new NumberGenerator();
        Random rnd;
        public NumberGenerator() //This is the core of this game. Random generator. Courtesy of theupsidedown87
        {
            rnd = new Random();
        }

        // use seperate methods for each thing you want to generate

        public int generateEnemyRoll()
        {
            return rnd.Next(1, 10);
        }

        public int generatePlayerRoll()
        {
            return rnd.Next(1, 10);
        }

        public int generateLevel()
        {
            return rnd.Next(1, 9);
        }

        public string generateDeathMessage()
        {
            return Wizards.deathmessages[rnd.Next(0, Wizards.deathmessages.Length)]; //You can keep adding Wizard Death Messages
        }                                                                            //This generator and ones below does not have any limits.

        public string generatespells()
        {
            return Wizards.spells[rnd.Next(0, Wizards.spells.Length)]; //Spells, names, death messages and taunts are all in Wizards.cs
        }

        public string generateWizardName()
        {
            return Wizards.names[rnd.Next(0, Wizards.names.Length)];
        }

        public string generatetaunts()
        {
            return Wizards.taunts[rnd.Next(0, Wizards.taunts.Length)];
        }

        // etc for all the other things you need to generate.
    }
}
