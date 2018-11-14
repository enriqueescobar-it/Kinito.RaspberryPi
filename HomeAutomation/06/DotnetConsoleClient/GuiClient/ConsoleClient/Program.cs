using Library;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleClient
{
    class Program
    {
        private readonly static LightService _service = new LightService();

        static void Main(string[] args)
        {
            if (!args.Any())
                Console.WriteLine("You must supply an action.");
            else if (args[0] == "getall")
                PrintListOfAllLights();
            else if (args[0] == "get")
                PrintSingleLight(args[1]);
            else if (args[0] == "add")
                _service.AddLight(args[1], args[2], args[3]);
            else if (args[0] == "set")
                _service.SetLightState(args[1], args[2]);
            else if (args[0] == "delete")
                _service.DeleteLight(args[1]);
        }

        private static void PrintListOfAllLights()
        {
            var house = _service.GetHouse();
            foreach (var light in house.Lights)
                Console.WriteLine(string.Format("Light {0} has house code of {1} and unit code of {2}", light.LightId, light.HouseCode, light.UnitCode));
        }

        private static void PrintSingleLight(string lightId)
        {
            var light = _service.GetLight(lightId);
            Console.WriteLine(string.Format("Light {0} has house code of {1} and unit code of {2}", light.LightId, light.HouseCode, light.UnitCode));
        }
    }
}
