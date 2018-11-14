using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleClient
{
    class Program
    {
        private static readonly RestClient _restClient = new RestClient("http://raspberrypi");

        static void Main(string[] args)
        {
            if (!args.Any())
                Console.WriteLine("You must supply an action.");
            else if (args[0] == "getall")
                PrintListOfAllLights();
            else if (args[0] == "get")
                PrintSingleLight(args[1]);
            else if (args[0] == "add")
                AddLight(args[1], args[2], args[3]);
            else if (args[0] == "set")
                SetLightState(args[1], args[2]);
            else if (args[0] == "delete")
                DeleteLight(args[1]);
        }

        private static void PrintListOfAllLights()
        {
            var house = GetHouse();
            foreach (var light in house.Lights)
                Console.WriteLine(string.Format("Light {0} has house code of {1} and unit code of {2}", light.LightId, light.HouseCode, light.UnitCode));
        }

        private static void PrintSingleLight(string lightId)
        {
            var light = GetLight(lightId);
            Console.WriteLine(string.Format("Light {0} has house code of {1} and unit code of {2}", light.LightId, light.HouseCode, light.UnitCode));
        }

        private static House GetHouse()
        {
            var request = new RestRequest("lights", Method.GET) { RequestFormat = DataFormat.Json };
            return _restClient.Execute<House>(request).Data;
        }

        private static void AddLight(string lightId, string houseCode, string unitCode)
        {
            var request = new RestRequest("lights", Method.POST) { RequestFormat = DataFormat.Json };
            request.AddBody(new { lightId = lightId, houseCode = houseCode, unitCode = unitCode });

            _restClient.Execute(request);
        }

        private static void SetLightState(string lightId, string command)
        {
            var url = string.Format("lights/{0}/{1}", lightId, command);
            var request = new RestRequest(url, Method.PUT);
            _restClient.Execute(request);
        }

        private static void DeleteLight(string lightId)
        {
            var url = string.Format("lights/{0}", lightId);
            var request = new RestRequest(url, Method.DELETE);
            _restClient.Execute(request);
        }

        private static Light GetLight(string lightId)
        {
            var request = new RestRequest("lights/" + lightId, Method.GET) { RequestFormat = DataFormat.Json };
            var light = _restClient.Execute<Light>(request).Data;
            return light;
        }
    }
}
