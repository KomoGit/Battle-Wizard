using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Dynamic;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace Battle_Wizard
{
    public class Game
    {
        public void gameStart()
        {
            Console.WriteLine("Hello Wizard! What is your name: (Insert your name) ");
            PlayerClass Player01 = new PlayerClass();
            Player01.playerName();
        }
        public static string UserInput()
        {
            string input = Console.ReadLine();
            return input;
        }
        public static void WaitAndClear()
        {
            Console.WriteLine("Press any key to continue");
            Console.ReadKey();
            Console.Clear();
        }
    }
}
