using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace sokdobas
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int elerendo = 0;
            while (true)
            {
                try
                {
                    if (elerendo < 1)
                    {
                        Console.Write("Elerendo szam: ");
                        elerendo = int.Parse(Console.ReadLine());
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

            bool True = true;
            int jatekos1pont = 0;
            int jatekos1elozo = 0;
            int jatekos2pont = 0;
            int jatekos2elozo = 0;

            Random rnd = new Random();

            int db = 0;
            int dobas1 = 0;
            int dobas2 = 0;

            while (True)
            {

                dobas1 = rnd.Next(1, 7);
                jatekos1pont += dobas1;

                dobas2 = rnd.Next(1, 7);
                jatekos2pont += dobas2;

                if (dobas1 == 1 && jatekos1elozo == 1)
                {
                    jatekos1pont = 0;
                }

                if (dobas2 == 1 && jatekos2elozo == 1)
                {
                    jatekos2pont = 0;
                }

                if (dobas1 == 6 && jatekos1elozo == 6)
                {
                    jatekos2pont = 0;
                }

                if (dobas2 == 6 && jatekos2elozo == 6)
                {
                    jatekos1pont = 0;
                }

                jatekos1elozo = dobas1;
                jatekos2elozo = dobas2;

                db++;





                Console.WriteLine($"{dobas1} {dobas2} {jatekos1pont} {jatekos2pont}");
                
                
                if(jatekos1pont > elerendo || jatekos2pont > elerendo)
                {
                    if (jatekos1pont == jatekos2pont)
                    {
                        Console.WriteLine($"döntetlen");
                    }
                    else if ( jatekos1pont > jatekos2pont)
                    {
                        Console.WriteLine($"jatekos1");

                    }
                    else
                    {
                        Console.WriteLine($"jatekos2");
                    }
                    Console.WriteLine($"{db} kör volt");
                    True = false;
                }

            }
            Console.ReadKey();
        }
    }
}
