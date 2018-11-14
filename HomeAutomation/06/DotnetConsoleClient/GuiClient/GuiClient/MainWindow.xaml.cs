using Library;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace GuiClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private readonly LightService _service = new LightService();
        public ObservableCollection<LightViewModel> Lights { get; set; }

        public MainWindow()
        {
            var lights = _service.GetHouse().Lights;
            Lights = new ObservableCollection<LightViewModel>(lights.Select(l => new LightViewModel(_service, l)));
            DataContext = this;

            InitializeComponent();
        }
    }
}
