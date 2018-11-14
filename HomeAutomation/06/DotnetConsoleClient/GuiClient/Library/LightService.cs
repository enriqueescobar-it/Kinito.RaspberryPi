using RestSharp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Library
{
    public class LightService
    {
        private static readonly RestClient _restClient = new RestClient("http://raspberrypi");

        public House GetHouse()
        {
            var request = new RestRequest("lights", Method.GET) { RequestFormat = DataFormat.Json };
            return _restClient.Execute<House>(request).Data;
        }

        public void AddLight(string lightId, string houseCode, string unitCode)
        {
            var request = new RestRequest("lights", Method.POST) { RequestFormat = DataFormat.Json };
            request.AddBody(new { lightId = lightId, houseCode = houseCode, unitCode = unitCode });

            _restClient.Execute(request);
        }

        public void SetLightState(string lightId, string command)
        {
            var url = string.Format("lights/{0}/{1}", lightId, command);
            var request = new RestRequest(url, Method.PUT);
            _restClient.Execute(request);
        }

        public void DeleteLight(string lightId)
        {
            var url = string.Format("lights/{0}", lightId);
            var request = new RestRequest(url, Method.DELETE);
            _restClient.Execute(request);
        }

        public Light GetLight(string lightId)
        {
            var request = new RestRequest("lights/" + lightId, Method.GET) { RequestFormat = DataFormat.Json };
            var light = _restClient.Execute<Light>(request).Data;
            return light;
        }
    }
}
