import sys, json, requests

BASE_URL = 'http://raspberrypi/lights'

def printLightToConsole(light):
	print('Light {0} has house code of {1} and unit code of {2}'.format(light['lightId'], light['houseCode'], light['unitCode']))

def printAllLights():
	returnedJson = requests.get(BASE_URL).json()
	for light in returnedJson['lights']:
		printLightToConsole(light)

def printSingleLight(lightId):
	returnedJson = requests.get(BASE_URL + '/' + lightId).json()
	printLightToConsole(returnedJson)

def addLight(lightId, houseCode, unitCode):
	lightsJson = json.dumps({"lightId":lightId,"houseCode":houseCode,"unitCode":unitCode})
	requestHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	requests.post(BASE_URL, data=lightsJson, headers=requestHeaders)

def setLightState(lightId, command):
	requests.put(BASE_URL + '/{0}/{1}'.format(lightId, command))

def deleteLight(lightId):
	requests.delete(BASE_URL + '/' + lightId)

def process(argv):
	if(argv[0] == 'getall'):
		printAllLights()
	elif(argv[0] == 'get'):
		printSingleLight(argv[1])
	elif(argv[0] == 'add'):
		addLight(argv[1], argv[2], argv[3])
	elif(argv[0] == 'set'):
		setLightState(argv[1], argv[2])
	elif(argv[0] == 'delete'):
		deleteLight(argv[1])

if __name__ == '__main__':
	process(sys.argv[1:])