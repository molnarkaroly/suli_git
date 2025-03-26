using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace kocka_poker
{



    internal class Program
    {
        static void Main(string[] args)
        {

            int jatekosSzam = 0;
            while (true)
            {
                try
                {
                    if (jatekosSzam < 2)
                    {
                        Console.Write("Hány darab játékos?: ");
                        jatekosSzam = int.Parse(Console.ReadLine());
                        continue;
                    }
                    else
                    {
                        break;
                    }
                }
                catch (Exception)
                {

                    continue;
                }
                
            }
            var tomb = new int[jatekosSzam, 5];
            Random rnd = new Random();
            bool True = true;
            while (True)
            {
                for (int i = 0; i < jatekosSzam; i++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        int dobas = rnd.Next(1, 7);
                        tomb[i, j] = dobas;
                    }
                }


                for (int i = 0; i < jatekosSzam; i++)
                {
                    for (int j = 0; j < 5; j++)
                    {
                        Console.Write(tomb[i, j]);
                    }
                    Console.WriteLine(" ");
                }

                
                var jatekosok = new string[jatekosSzam];
                for (int ii = 0; ii < jatekosSzam; ii++)
                {
                    var darab = new int[jatekosSzam, 6];
                    for (int j = 0; j < 6; j++)
                    {
                        darab[ii, j]++;
                    }
                }

                for (int ii = 0; ii < jatekosSzam; ii++)
                {
                    var darab = new byte[jatekosSzam, 6];
                    for (int j = 0; j < 6; j++)
                    {
                       Console.Write(darab[ii, j]);
                    }
                    Console.WriteLine(" ");
                }

                break;

            }
        
            
        Console.ReadKey();
        }
    }
}
