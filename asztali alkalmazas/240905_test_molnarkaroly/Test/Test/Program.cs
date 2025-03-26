using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int dbszam = 0;
            while (!(dbszam > 10 && dbszam < 1000))
            {
                Console.WriteLine("Adja meg a darabszámot: (10-1000)");
                dbszam = int.Parse(Console.ReadLine());
            }

            Random random = new Random();

            int szamok = random.Next(10, 1000);

            String str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

            
            

        

        Console.WriteLine("");
            Console.ReadKey();
        }
    }
}
