using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kinevetAvegen
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int kek   = 0;
            int kekDobas = 0;
            int zold  = 0;
            int zoldDobas = 0;
            int piros = 0;
            int pirosDobas = 0;
            int sarga = 0;
            int sargaDobas = 0;

            int kezd = 0;
            while(true) 
            {
                try
                {
                    if (kezd == 0 || kezd > 4)
                    {
                        Console.Write("ki kezdjen? 1:kek 2: zöld: 3:piros 4:sarga ");
                        kezd = int.Parse(Console.ReadLine());
                        continue;
                    }
                    else
                    {
                        break;
                    }
                }
                catch (Exception)
                {

                    continue;
                }

            }

            if (kezd == 1) 
            {
                Console.WriteLine("\n kék kezd");
            }
            if (kezd == 2){
                Console.WriteLine("\n Zöld kezd");

            }
            if (kezd == 3){
                Console.WriteLine("\n Piros kezd");

            }
            if (kezd == 4)
            {
                Console.WriteLine("\n Sárga kezd");
            }

            if (kezd == 4)
            {
                
            }

            Console.ReadKey();
        }
    }
}
