using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace firstForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void muvelet()
        {
            if (radioButton1.Checked == true) { 
                Num3.Text = Convert.ToString(Convert.ToDouble(Num1Box.Text) - Convert.ToDouble(Num2Box.Text)) ;
            }
            else if (radioButton2.Checked == true) {
        }


        private void Form1_Load(object sender, EventArgs e)
        {

            btnExit.Text = "exit";

        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            muvelet();
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            muvelet();

        }

        private void Num1Box_TextChanged(object sender, EventArgs e)
        {
            muvelet();

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            muvelet();

        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            muvelet();

        }

        private void Num2Box_TextChanged(object sender, EventArgs e)
        {
            muvelet();

        }

        private void Num3_TextChanged(object sender, EventArgs e)
        {
            muvelet();

        }
    }

        private void label2_Click(object sender, EventArgs e)
        {

        }
    }
