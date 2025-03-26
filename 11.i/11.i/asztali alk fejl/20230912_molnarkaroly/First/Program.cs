using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace First
{
    internal class Program
    {    
        static void wait(string text)
            {
                Console.WriteLine(text);
                Console.ReadKey();
            }

        static void Main(string[] args)
        {

            #region feladat1
            //  kérjen be egy nevet
            string yourname = null;
            do
            {           
                Console.Write("Kérem a nevét: ");
                yourname = Console.ReadLine();

            } while (yourname == "");
            Console.WriteLine("Hello, "+ yourname);

            #endregion

            wait("Billentyűre tovább....");


            #region feladat2
            //kérjen be egy kort
            int yourage = 0;
            do
            {
                Console.Write("Kérem a korát: ");
                yourage = Convert.ToInt32(Console.ReadLine());

            } while (yourage == 0);
            Console.WriteLine("te korod: {0} év", yourage.ToString());

            Console.WriteLine("hello {0} a te korod {1}", yourname, yourage.ToString());
            #endregion


            wait("Billentyűre kilépés....");
        }
    }
}
