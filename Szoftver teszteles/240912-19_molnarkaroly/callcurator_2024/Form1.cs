using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace callcurator_2024
{
    public partial class calculator24 : Form
    {
        public calculator24()
        {
            InitializeComponent();
        }

        static int intColorIndex = 0;
        static List<Color> ListColors = new List<Color>();
        static int sign = 0;
        static int dot = 0;
        static double result = 0;


        private void calculator24_Load(object sender, EventArgs e)
        {
            txbDisplay.Text = "0";
            ListColors.Add(Color.White);
            ListColors.Add(Color.Red);
            ListColors.Add(Color.Green);
            ListColors.Add(Color.Blue);
            ListColors.Add(Color.Purple);
            txbDisplay.BackColor = ListColors[intColorIndex];

        }

        private void off_Btn_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void txbDisplay_TextChanged(object sender, EventArgs e)
        {

        }

        private void btn_Color_Click(object sender, EventArgs e)
        {
            intColorIndex++;
            if (intColorIndex >= ListColors.Count)
            {
                intColorIndex = 0;
            }
            txbDisplay.BackColor = ListColors[intColorIndex];

        }

        private void btn0_Click(object sender, EventArgs e)
        {
            Display("+-");
        }

        private void Display(string btn) 
        {
            string textDisplay = txbDisplay.Text;
            int maxlength = length(textDisplay);

            if (btn == "+-")
            {
                txbDisplay.Text = (double.Parse(txbDisplay.Text) * -1).ToString();
                return;
            }

            if (btn == "C")
            {
                txbDisplay.Text = "0";
                return;
            }

            if (btn == "AC")
            {
                txbDisplay.Text = "0";
                result = 0;
                return;
            }


            if (textDisplay.Length == maxlength)
            {
                return;
            }
            else 
            {
                if (btn == "," && dot == 0)
                {
                    txbDisplay.Text += ",";
                    return;
                }
                else if(btn == "," && dot == 1)
                {
                    return;
                }

                






               else
                {
                    if (txbDisplay.Text == "0") txbDisplay.Text = btn;
                    else txbDisplay.Text += btn;
                }
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btn3_Click(object sender, EventArgs e)
        {
            Display("1");
        }


        static int length(string displayText)
        {
            if (displayText.Contains(","))
            {
                dot = 1;
            }
            else 
            {
                dot = 0;
            
            }

            if (displayText.Contains("-"))
            {
                sign = 1;
            }
            else
            {
                sign = 0;
            }

            return 14+ sign + dot;
        }

        private void btn2_Click(object sender, EventArgs e)
        {
            Display(",");
        }

        private void btn1_Click(object sender, EventArgs e)
        {
            Display("0");

        }

        private void btn4_Click(object sender, EventArgs e)
        {
            Display("2");

        }

        private void btn5_Click(object sender, EventArgs e)
        {
            Display("3");

        }

        private void btn6_Click(object sender, EventArgs e)
        {
            Display("4");

        }

        private void btn7_Click(object sender, EventArgs e)
        {
            Display("5");

        }

        private void btn8_Click(object sender, EventArgs e)
        {
            Display("6");

        }

        private void btn9_Click(object sender, EventArgs e)
        {
            Display("7");

        }

        private void btn10_Click(object sender, EventArgs e)
        {
            Display("8");

        }

        private void btn11_Click(object sender, EventArgs e)
        {
            Display("9");

        }

        private void btn17_Click(object sender, EventArgs e)
        {
            Display("C");
        }

        private void btn18_Click(object sender, EventArgs e)
        {
            Display("AC");
        }





    }
}
