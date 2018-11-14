using Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace GuiClient
{
    public class LightCommand : ICommand
    {
        public event EventHandler CanExecuteChanged;

        private readonly string _command;
        private readonly string _lightId;
        private readonly LightService _service;

        public LightCommand(string command, string lightId, LightService service)
        {
            _command = command;
            _service = service;
            _lightId = lightId;
        }

        public bool CanExecute(object parameter)
        {
            return true;
        }

        public void Execute(object parameter)
        {
            _service.SetLightState(_lightId, _command);
        }
    }
}
