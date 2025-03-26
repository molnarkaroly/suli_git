using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace Feladat
{

    class Uzenet
    {
        public int nap;
        public string segito;
        public string szoveg;
        public Uzenet(string nap, string segito, string szoveg)
        {
            this.nap = Convert.ToInt32(nap);
            this.segito = segito;
            this.szoveg = szoveg;
        }
        public override string ToString()
        {
            return nap + ". nap " + segito + ". radioamator: " + szoveg;
        }

        class Program
        {
            static List<Uzenet> u = new List<Uzenet>();
            static void Main(string[] args)
            {
                using (StreamReader be = new StreamReader("veetel.txt"))
                {
                    string sor;
                    while ((sor = be.ReadLine()) != null)
                    {
                        string[] adatok = sor.Split(';');
                        u.Add(new Uzenet(adatok[0], adatok[1], adatok[2]));
                    }
                }
                int db = u.Count;
                // 1. feladat
                foreach (var item in u)
                {
                    Console.WriteLine(item);
                }
                // 2. feladat
                Console.WriteLine("Az elso uzenet rogzitoje: " + u[0].segito);
                Console.WriteLine("Az utolso uzenet rogzitoje: " + u[db - 1].segito);
                // 3. feladat
                foreach (var item in u)
                {
                    if (item.szoveg.Contains("farkas"))
                    {
                        Console.WriteLine(item.nap + ". nap " + item.segito + ". radioamator");
                    }
                }
                // 4. feladat

                int[] nap = new int[12];
                for (int i = 0; i < db; i++)
                {
                    nap[u[i].nap]++;
                }
                for (int n = 1; n <= 11; n++)
                {
                    Console.WriteLine(n + ". nap: " + " " + nap[n] + " radioamator");
                }
            }
        }
    }
}




