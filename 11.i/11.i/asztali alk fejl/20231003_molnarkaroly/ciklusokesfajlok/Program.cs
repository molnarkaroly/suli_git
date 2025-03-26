using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace ciklusokesfajlok
{
    class data
    {
        public int x;
        public string y;
        public data(int i, string sor) 
        {
            this.x = i;
            this.y = sor;
        }
    }

    class Program
    {



        static void Main(string[] args)
        {
            List<string> datas = new List<string>(); //lista létrehozása

            /*  string[] tombNev = new string[2]; //tömb létrehozása csak adott számú elemet tárolhat el
                int[] tombNevint = new int[2]; 
                bool[] tombNevbool = new bool[2]; 

                HashSet <string> halmaz = new HashSet<string>(); // ez egy halmazt hoz létre
            */

            string[] sorok = File.ReadAllLines("ajto.txt");

            StreamReader fromfile = new StreamReader("ajto.txt");
            StreamWriter tofile = new StreamWriter("ajtoKi.txt");


            while (!fromfile.EndOfStream)
            {
             datas.Add(fromfile.ReadLine());

            }

            fromfile.Close();
            tofile.Close();


            //számláló ciklus

            for (int i = 0; i < sorok.Length; i++)
            {
                Console.WriteLine(sorok[i]);

            }

            Console.WriteLine();
            //bejaro ciklus - halmazok
            foreach (string item in sorok) 
            {
                Console.WriteLine(item);
            }

            data[]neve = new data[sorok.Length];
            for (int i = 0; i < sorok.Length; i++)
            {
                nneve[i] =  new data(i, sorok[i]);

            }


            Console.ReadKey();
            //a fájlt a bin debug mappába kell rakni 
           // a
        }
    }
}
