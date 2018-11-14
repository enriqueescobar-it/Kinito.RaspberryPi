using Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace GuiClient
{
    public class LightViewModel
    {
        private readonly LightService _service;
        private readonly Light _light;

        public Light Light { get { return _light; } }

        public ICommand TurnOn { get; private set; }

        public ICommand TurnOff { get; private set; }

        public LightViewModel(LightService service, Light light)
        {
            _service = service;
            _light = light;
            TurnOn = new LightCommand("on", light.LightId, _service);
            TurnOff = new LightCommand("off", light.LightId, _service);
        }
    }
}
