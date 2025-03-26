using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Security.Cryptography;


namespace reklam
{

    class data
    {
        public byte nap;
        public string varos;
        public byte db;
        public data(string dLine)
        {
            string[] strings = dLine.Split(' ');
            this.nap = byte.Parse(strings[0]);
            this.varos = strings[1];
            this.db = byte.Parse(strings[2]);

        }
    }
    internal class Program
    {
        static public List<data> list = new List<data>();

        static int osszes(string varos, byte nap)
        {
            int osszeg = 0;
            foreach (var item in list)
            {
                if (item.nap == nap) {
                osszeg+= (int)item.db;
                }
               
            }
            return osszeg;

        }


        static void Main(string[] args)
        {
            StreamReader reader = new StreamReader("rendel.txt");
            /*string[] strings = File.ReadAllLines("rendel.txt");*/

            while (!reader.EndOfStream)
            {
                list.Add(new data(reader.ReadLine()));
            }
            int length = list.Count;
            reader.Close();


           
            /*
             * list.Clear();
             * foreach(var item in strings)
             * {
             * list.Add(new data(item));
             * }
            */
            Console.WriteLine($"2. feladat \n \t Összesen {length} rendelés érkezett");

            Console.Write("3. feladat \n \tKérem a nap számát: ");
            byte napszam = byte.Parse(Console.ReadLine());

            int count = 0;
            for (int i = 0; i < length; i++)
            {
                if (list[i].nap == napszam) count++;
            }

            Console.WriteLine($"A {napszam}. nap {count} rendelés történt");


            HashSet<byte> rendelesiNapok = new HashSet<byte>();
            HashSet<byte> napok = new HashSet<byte>();
            
            foreach (var item in list)
            {
                napok.Add(item.nap);

                if (item.varos =="NR")
                {
                    rendelesiNapok.Add(item.nap);
                }
            }

            if (rendelesiNapok.Count == napok.Count)
            {
                Console.WriteLine($"4. feladat \n \t mindennap volt rendelés az érintett városból");
            }
            else 
            {
                Console.WriteLine($"4. feladat \n \t {napok.Count - rendelesiNapok.Count} nap nem volt rendelés a reklámban nem érintett városban");

            }
            int maxIndex = 0;

            for (int i = 1; i < length; i++)
            {
                if (list[i].db > list[maxIndex].db)
                {
                    maxIndex = i;
                }
            }

            Console.WriteLine($"5. Feladat \n\t {list[maxIndex].nap} nap rendelték a legtöbbet {list[maxIndex].db}db-ot");

            Console.ReadKey();
        }
    }
}
