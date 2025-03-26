using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
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
                NUM.Text = Convert.ToString(Convert.ToDouble))
            }

        private void Form1_Load(object sender, EventArgs e)
        {
                muvelet();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
                muvelet();
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
                muvelet();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
                muvelet();
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
                muvelet();
        }
    }
}
