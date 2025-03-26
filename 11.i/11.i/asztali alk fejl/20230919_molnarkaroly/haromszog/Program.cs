/*Kérje be egy háromszög három oldalának hosszát, és végezze el a következő feladatokat vele:
- állapítsa meg, hogy létezhet-e ilyen háromszög,
- állapítsa meg, hogy a háromszög egyenlő oldalú-e,
- állapítsa meg, hogy a háromszög egyenlő szárú-e,
- állapítsa meg, hogy a háromszög derékszögű-e,
- írja ki, a háromszög kerületét,
- írja ki, a háromszög területét,
- írja ki, a háromszög belső szögeinek összegét!
*/


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace haromszog
{
    internal class Program
    {


        static double sideInput(string text)
        {

            double TMP = 0;

            do
            {

                try
                {

                    Console.Write(text);
                    TMP = double.Parse(Console.ReadLine());
                }
                catch (Exception)
                {
                    TMP = 0;
                }

            }
            while (TMP <= 0);
            return TMP;
        }

        static void Main(string[] args)
        {

            double triangleSide1 = sideInput("kérem az elso oldal hosszát: ");
            double triangleSide2 = sideInput("kérem az masoodik oldal hosszát: ");
            double triangleSide3 = sideInput("kérem az harmadik oldal hosszát: ");

            #region Feladat 1
            bool triangle = false;
            if    (triangleSide1 + triangleSide2 > triangleSide3 
                && triangleSide2 + triangleSide3 > triangleSide1 
                && triangleSide1 + triangleSide3 > triangleSide2)
            {
                triangle = true;
            }

            #endregion

            #region Feladat 2
            bool sameSideTriangle = triangleSide1 == triangleSide2 &&
                                    triangleSide2 == triangleSide3 &&
                                    triangle;

            #endregion

            #region Feladat 3
            bool isoscelesTriangle = sameSideTriangle|| ((triangleSide1 == triangleSide2  ||
                                      triangleSide1 == triangleSide3  ||
                                      triangleSide2 == triangleSide3) &&
                                      triangle);
            #endregion

            #region Feladat 4

            bool rightTriangle = Math.Pow(triangleSide1, 2) + Math.Pow(triangleSide2, 2) == Math.Pow(triangleSide3, 2) ||
                                 Math.Pow(triangleSide2, 2) + Math.Pow(triangleSide3, 2) == Math.Pow(triangleSide1, 2) ||
                                 Math.Pow(triangleSide1, 2) + Math.Pow(triangleSide3, 2) == Math.Pow(triangleSide2, 2);
            #endregion

            if (triangle
            { 

            #region Feladat 5
            Console.WriteLine("a haromszög kerülete: {0}",(triangleSide1 + triangleSide2 +triangleSide3).ToString());


            #endregion

            #region Feladat 6
            #endregion

            #region Feladat 7
            Console.WriteLine("a háromszög belsőszögeinek összege 180°");
                #endregion

            }
            else  Console.WriteLine("azadatoknem egy háromszög  oldalait adják meg");
 


            Console.ReadKey();
        }
    }
}
