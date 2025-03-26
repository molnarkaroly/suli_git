using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace tarsalgo
{
    class data
    {
        public byte hour;
        public byte min;
        public byte id;
        public bool entry = true;
        public data(string dLine) {
            string[] strings = dLine.Split(' ');
            this.hour = byte.Parse(strings[0]);
            this.min = byte.Parse(strings[1]);
            this.id = byte.Parse(strings[2]);
            if( strings[3] == "ki") this.entry = false;
        }

    }

    internal class Program
    {
        static void Main(string[] args)
        {
            #region 1.feladat
            List<data> list = new List<data>();
            StreamReader reader = new StreamReader("ajto.txt");
            while (!reader.EndOfStream)
            {
                list.Add(new data(reader.ReadLine()));
            }
            reader.Close();
            int length = list.Count;

            #endregion

            #region 2.feladat

            int ii = 0;

            while (!list[ii].entry)
            {
                ii++;
            }
            Console.WriteLine($"2. feladat \n \t Az első belépő kódja:{list[ii].id}");

            ii = length -1;

            while (list[ii].entry)
            {
                ii--;
            }
            Console.WriteLine($"\t Az utolso kilépő kódja:{list[ii].id}");


            #endregion

            #region feladat 3
            HashSet<byte> set = new HashSet<byte>();
            for (ii = 0; ii < length; ii++) set.Add(list[ii].id);
            
            int[] counter = new int[100];
            foreach (var item in list)
            {
                counter[item.id-1]++;
            }

            StreamWriter writer = new StreamWriter("athaladat.txt");
            for (ii = 0; ii < 100; ++ii)
            {
                if (counter[ii] != 0)
                {
                    writer.WriteLine($"{ii+1} {counter[ii]}");
                }
            }

            writer.Close();

            #endregion

            #region

            #endregion

            Console.ReadKey();
        }
    }
}
