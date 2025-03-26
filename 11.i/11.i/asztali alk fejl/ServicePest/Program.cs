using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ServicePest
{
    class Data
    {
        public string azon;
        public List<string> gepKod = new List<string>();
        public List<string> munkabeosztas = new List<string>();
        public float ertekeles;
        public Data(string sor)
        {
            string[] strings = sor.Split(',');
            this.ertekeles = float.Parse(strings[strings.Length - 1]);
            for (int i = strings.Length - 8; i < strings.Length - 1; i++)
            {
                this.munkabeosztas.Add(strings[i]);
            }
            for (int ii = strings.Length - 9; ii > 0; ii--)
            {
                this.gepKod.Add(strings[ii]);
            }
            this.azon = strings[0];
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {

            try
            {
                StreamReader rf = new StreamReader("Pest.csv");
                List<Data> list = new List<Data>();
                while (!rf.EndOfStream)
                {
                    list.Add(new Data(rf.ReadLine()));
                }
                rf.Close();

                Console.WriteLine($"1. feladat:\nA 21 pesti szerelő adatának beolvasása megtörté");

                int lgt = 0;
                foreach (var item in list)
                {
                    if(item.gepKod.Count > lgt) 
                    {
                        lgt = item.gepKod.Count;
                    }
                }

                Console.Write($"2.feladat\nA legtöbb({lgt}db) különböző típusú berendezéshez értő szerelők azonosítója: ");

                foreach (var item in list)
                {
                    if (item.gepKod.Count == lgt)
                    {
                        Console.Write(item.azon + ", ");
                    }
                }

                int szombat = 0;
                int vasarnap = 0;


                foreach (var item in list)
                {
                    if (item.munkabeosztas[5] == "X")
                    {
                        szombat++;
                    }
                    if (item.munkabeosztas[6] == "X")
                    {
                        vasarnap++;
                    }
                }
                

                Console.WriteLine($"3. feladat:\nSzombatonként {szombat} szerelő, vasárnaponként {vasarnap} szerelő áll rendelkezésre.");


                float atlagPont = 0;
                float osszPont = 0;
                foreach (var item in list) 
                {
                    osszPont += item.ertekeles;
                }

                atlagPont = osszPont / list.Count;

                string formattedFloat = atlagPont.ToString("0.0");

                float felettszazalekcount = 0;

                foreach(var item in list)
                {
                    if (item.ertekeles > atlagPont)
                    {
                        felettszazalekcount++;
                    }
                }

                float felettszazalek = (felettszazalekcount / list.Count)*100 ;
                string formattedszazalek = felettszazalek.ToString("0.");


                Console.WriteLine($"4. feladat:\nA szerelők átlagosan {formattedFloat} pontot kaptak. A szerelők {formattedszazalek}%-a az átlagnál magasabb pontszámot kapott. \n");



                Console.Write($"5. feladat:\nMindhárom gázzal működő berendezéshez értő szerelők: ");
                foreach (var item in list) 
                {
                    if (item.gepKod.Contains("C") && item.gepKod.Contains("G") && item.gepKod.Contains("K"))
                    {
                        Console.Write(item.azon + ", ");
                    }
                }


                Console.Write("6. feladat:\r\nAdja meg a keresendő háztartási eszköz nevének rövidítését: ");
                string kereskod = Console.ReadLine();
                Console.WriteLine("A keresett típushoz a következő napokon nem áll rendelkezésre szerelő:");



            }
            catch (Exception)
            {
                Console.WriteLine("„A Pest.csv nevű fájl beolvasása sikertelen");
            }
               


            Console.ReadKey();
        }
    }
}
