using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using ArtificialNature;

namespace AppNeonWinform
{
    public partial class FormMain : Form
    {
        public FormMain()
        {
            InitializeComponent();
        }

        private void FormMain_Load(object sender, EventArgs e)
        {
            var neon = new UserControl_NeonCLR();
            this.panelOpenGL.Controls.Add(neon);
        }

        private void Neon_OnFrame(int timeDelta)
        {
            Console.Write(timeDelta);
        }
    }
}
