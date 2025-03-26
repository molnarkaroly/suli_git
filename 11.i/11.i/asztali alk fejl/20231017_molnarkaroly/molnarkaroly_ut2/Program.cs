using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace molnarkaroly_ut2
{
    class data
    {
        public byte hour;
        public byte minute;
        public byte second;
        public byte speed;
        public string irany;

        public data(string dLine)
        {
            string[] strings = dLine.Split(' ');
            try
            {
                this.hour = byte.Parse(strings[0]);
                this.minute = byte.Parse(strings[1]);
                this.second = byte.Parse(strings[2]);
                this.speed = byte.Parse(strings[3]);
                this.irany = strings[4];
            }
            catch (Exception)
            {
                this.hour = 99;
            }

         

        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            List<data> list = new List<data>();
            int hiba = 0;
            StreamReader reader = new StreamReader("forgalom.txt");
            string elsosor = reader.ReadLine(); //elso sor beolvavása
            while (!reader.EndOfStream)
            {
                data tmp = new data(reader.ReadLine());
                if (tmp.hour != 99)
                {
                    list.Add(tmp);
                }
                else
                {
                    hiba++;
                }
            }
            reader.Close();
            Console.Write("2. feldat \n\t adja meg a jármű sorszámát: ");

            int sorszam = 0;
            do
            {

                try
                {
                    sorszam = int.Parse(Console.ReadLine());
                }
                catch (Exception)
                {

                    sorszam = 0;
                }
            } while (sorszam < 1 || sorszam >  list.Count);

            Console.ReadKey();
        }
    }
}
