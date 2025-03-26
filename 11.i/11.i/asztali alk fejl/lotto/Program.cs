using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace lotto
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> belotto = new List<int>();

            while (belotto.Count < 5) 
            {
                Console.WriteLine("Kérem adj meg egy számot:");
                int usernumber = 0;
                try
                {
                    usernumber = int.Parse(Console.ReadLine());

                }
                catch (Exception)
                {

                   usernumber = 0;
                }
                if (usernumber <= 90 && usernumber > 0 && !belotto.Contains(usernumber))
                {
                    belotto.Add(usernumber);
                    Console.Write("a lista:  ");
                    foreach (var item in belotto)
                    {
                        Console.WriteLine($" {item} ");
                    }
                }
            }

            Console.WriteLine(belotto[1]);
            
            Random rnd = new Random();
            List<string> tomb = new List<string>();

            for (int i = 0; i < 5; i++)
            {
                tomb.Add(rnd.Next(1, 90).ToString());
            }

            Console.WriteLine("A sorsolás elemei: " + string.Join(", ", tomb));

            List<string> lista = new List<string>();


            bool nyert = false;
            int db = 0;
            int kettesTalálat = 0;
            int harmasTalálat = 0;
            int negyesTalálat = 0;
            int ootoosTalálat = 0;
            /*
            while (nyert != true)
            {   
                for (int i = 0; i < 5; i++)
            {
                tomb.Add(rnd.Next(1, 90).ToString());
            }

                for (int i = 0; i < 5; i++)
                {
                    if (belotto.Contains(tomb[i]))
                    {
                        db ++;
                    }

                    lista.Add(tomb[1], tomb[2], tomb[3], tomb[4], tomb[5]);

                }
                if (db == 2)
                {
                    kettesTalálat ++;
                    Console.WriteLine($"Volt egy kettes találat {lista.Count} probalkozakor ami {lista.Count * 400} Ft-ba kerult");
                    continue;
                }
                if (db == 3)
                {
                    harmasTalálat++;
                    Console.WriteLine($"Volt egy hármas találat {lista.Count} probalkozakor ami {lista.Count * 400} Ft-ba kerult");
                                continue;

                }
                if (db == 4)
                {
                    negyesTalálat++;
                    Console.WriteLine($"Volt egy négyes találat {lista.Count} probalkozakor ami {lista.Count * 400} Ft-ba kerult");
                                continue;

                }
                if (db == 5)
                {
                    ootoosTalálat++;
                    Console.WriteLine($"Volt egy ötös találat {lista.Count} probalkozakor ami {lista.Count * 400} Ft-ba kerult";
                    break;
                }
            }
           */

            Console.ReadKey();
        }
    }
}
