using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MolnarKaroly_ut
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
            if (strings.Length > 1 )
            { 
            this.hour = byte.Parse(strings[0]);
            this.minute = byte.Parse(strings[1]);
            this.second = byte.Parse(strings[2]);
            this.speed = byte.Parse(strings[3]);
            this.irany = strings[4];
            }

        }
    }

    internal class Program
    {
        static int szamolA(byte ora, string irany,int ii)
        {
            int db = 0;

            if (ora == ii && irany == "A")
            {
                db++;
            }

            return db;
        }

        static int szamolF(byte ora, string irany, int ii)
        {
            int db = 0;

            if (ora == ii && irany == "F")
            {
                db++;
            }

            return db;
        }


        static void Main(string[] args)
        {
            List<data> list = new List<data>();
            StreamReader reader = new StreamReader("forgalom.txt") ;
            while (!reader.EndOfStream)
            {
                list.Add(new data(reader.ReadLine()));
            }

            int lenght = list.Count;

            Console.WriteLine("2.feladat");

            Console.Write("Kérem az n értékét: ");
            
            int n = int.Parse(Console.ReadLine());

            Console.WriteLine($"Az n-edik kocsi {list[n].irany} fele  haladt");

            reader.Close();
            /*  
              byte fmp = 0;
              for (int i = lenght; i > lenght; i--)
              {
                  int elso = 0;
                  int masodik = 0;

                  if (elso == 0 && list[i].irany == "A")
                  {
                      elso = list[i].speed;
                  }

                  if (elso != 0 && list[i].irany == "A")
                  {
                      masodik = list[i].speed;  
                  }

                  if (elso != 0 && masodik != 0)
                  {
                   if (elso > masodik)
                   {
                        fmp = elso - masodik;
                      }
                      else
                      {
                        fmp = elso - masodik;

                      }
                  }
              }


              Console.WriteLine($"a Felső város irányába tartó utolsó két jármű {fmp} másodperc \r\nkülönbséggel érte el az útszakasz kezdetét");
              */
            /*
            Console.WriteLine("4.feladat");

            for (int i = 0; i < lenght; i++)
            {
                Console.WriteLine($"{list[i].hour} órakor A írányba {szamolA(list[i].hour, "A", i)}db F irányba {szamolA(list[i].hour, "F", i)} db");
            }
            */
            Console.ReadKey();
        }
    }
}
