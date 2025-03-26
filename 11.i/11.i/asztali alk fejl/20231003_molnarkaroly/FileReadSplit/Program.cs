using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace FileReadSplit
{
    internal class data
    {
        public byte hour;
        public byte min;
        public byte sec;
        public bool In;
        public data(string line ) //konstructor
        {
            string[] stings = line.Split(' ');
            this.hour = Byte.Parse(stings[0]);
            this.min = Byte.Parse(stings[1]);
            this.sec = Byte.Parse(stings[2]);
            this.In = true;
            if (stings[3] == "ki" ) this.In = false; 

        }
    }


    internal class Program
    {
        static void Main(string[] args)
        {
            string[] sorok = System.IO.File.ReadAllLines("ajto.txt");
            int length = sorok.Length;

            data[] datas = new data[length];

            for (int i = 0; i < length; i++)
            {
                datas[i] = new data(sorok[i]);
            }


            Console.ReadKey();
        }
    }
}
