using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.ComponentModel;

//fáj a kezeem 

namespace statisztika
{
    class data
    {

        public bool playerId;
        public string[] types = new string[3];
        public int[] scores = new int[3];
        public data(string line)
        {
            string[] strings = line.Split(';');
            try
            {
                this.playerId = strings[0] == "1";
                for (int i = 0; i < 3; i++)
                {
                    if (strings[i + 1][0] == 'D' || strings[i + 1][0] == 'T')
                    {
                        this.types[i] = strings[i + 1][0].ToString();
                        this.scores[i] = int.Parse(strings[i + 1].Substring(1));
                    }
                    else
                    {
                        this.types[i] = "";
                        this.scores[i] = int.Parse(strings[i + 1]);
                    }
                }
            }
            catch (Exception)
            {

                this.types[0] = "error";
            }
        
        }

    }

    internal class Program
    {
        static void Main(string[] args)
        {
            #region variables
            data[] tomb = new data[300];
            List<data> lista = new List<data>();
            

            #endregion

            #region
            string filename = "dobasok.txt";



            StreamReader sr = new StreamReader(filename);
                int tombIndex = 0;
            while (!sr.EndOfStream) 
            {
                data tmp = new data(sr.ReadLine());
                if (tmp.types[0] != "error")
                {
                    lista.Add(tmp);
                    tomb[tombIndex++]= tmp;
                }
            }
           //int a = 0;
                sr.Close();
            //Console.WriteLine("1. f");
            #endregion


            #region
            Console.WriteLine("2. feladat");
            Console.WriteLine(tombIndex);
            #endregion


            #region
                Console.WriteLine("3. feladat");
                int bes = 0;
            foreach (var item in lista) 
            {
                if (item.scores[2] == 25 && item.types[2]=="D")
                {
                    bes++;
                }
            }
            Console.WriteLine("Bes (l):" + bes);
            bes = 0;
            foreach (var item in tomb)
            {
                if (item == null) continue;
                if (item.scores[2] == 25 && item.types[2] == "D")  bes++;
                
            }

            Console.WriteLine("Bes (t):" + bes);


            #endregion


            #region
            Console.WriteLine("4. feladat");
            Console.Write("adja meg a szektor erteket: ");
            string sector = Console.ReadLine();

            int secCount1 = 0;
            int secCount2 = 0;
            int _180_p1 = 0;
            int _180_p2 = 0;

            foreach (var item in lista) 
            {
                string akarmi = "";
                for (int i = 0; i < 3; i++) 
                {
                    if (sector == item.types[i] + item.scores[i].ToString() && item.playerId) secCount1++;
                    else if (sector == item.types[i] + item.scores[i].ToString() && !item.playerId) secCount2++;


                    akarmi += item.types[i] + item.scores[i].ToString();
                }


                if (item.playerId && akarmi == "T20T20T20")
                {
                    _180_p1++;
                }
                else if (!item.playerId && akarmi == "T20T20T20")
                {
                    _180_p2++;
                }

            }
            Console.WriteLine("az elso jatekos" +sector+"os dobasainak szama:" + secCount1);
            Console.WriteLine("az masodik jatekos" +sector+"os dobasainak szama:" + secCount2);
            #endregion


            #region
            Console.WriteLine("5. feladat");
            Console.WriteLine("1. jatekos: " + _180_p1);
            Console.WriteLine("2. jatekos: " + _180_p2);

            #endregion

            


            Console.ReadKey();
        }
    }
    
}
