# Azure Raspberry Pi

## Pre requisites

1. Azure https://portal.azure.com
2. Azure IoT Hub https://docs.microsoft.com/en-us/azure/iot-hub/about-iot-hub
2. PowerBI https://app.powerbi.com/home
3. AzureDevOps https://dev.azure.com
4. Microsoft AI Platform https://www.microsoft.com/en-us/ai/ai-platform
5. Raspberry Pi online simulator to Azure IoT Hub (Node.js) https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-raspberry-pi-web-simulator-get-started

## Raspberry Pi web simulator https://azure-samples.github.io/raspberry-pi-web-simulator/#GetStarted

1. Assembly area (right pane)
2. Coding area (left upper pane)
3. Integrated console window RUN - RESET - FOLD / EXPAND (left lower pane)

## Create IoT Hub resource https://docs.microsoft.com/en-us/azure/azure-resource-manager/manage-resource-groups-portal

1. Create resource [IoTHubResourceGroup | WebRPiIoTHub] https://portal.azure.com/#create/Microsoft.IotHub
2. Size & Scale F1 : Free tier
3. Hub https://portal.azure.com/#blade/HubsExtension/DeploymentDetailsBlade/overview/id/%2Fsubscriptions%2F72391b61-4b5a-4f6a-b161-eda9ba8fb5d1%2FresourceGroups%2FIoTHubResourceGroup%2Fproviders%2FMicrosoft.Resources%2Fdeployments%2FMicrosoft.IotHub-9615939/packageId/Microsoft.IotHub/packageIconUri/https%3A%2F%2F106c4.wpc.azureedge.net%2F80106C4%2FGallery-Prod%2Fcdn%2F2015-02-24%2Fprod20161101-microsoft-windowsazure-gallery%2FMicrosoft.IotHub.1.0.7%2FIcons%2FMedium.png/primaryResourceId/%2Fsubscriptions%2F72391b61-4b5a-4f6a-b161-eda9ba8fb5d1%2Fresourcegroups%2FIoTHubResourceGroup%2Fproviders%2FMicrosoft.Devices%2FIotHubs%2FWebRPiIoTHub

## Register a new RPi device onto IoT Hub resource https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-identity-registry#identity-registry-operations

1. IoT Devices https://portal.azure.com/#blade/HubsExtension/BrowseAll
2. IoT Devices Provisioning WebRPiIoTHubDevicePRovisioningService https://portal.azure.com/#create/Microsoft.IoTDeviceProvisioning
3. Add IoT Devices https://portal.azure.com/#@ce57ebe3-a63d-4708-b5cf-c274b48bd26c/resource/subscriptions/72391b61-4b5a-4f6a-b161-eda9ba8fb5d1/resourceGroups/IoTHubResourceGroup/providers/Microsoft.Devices/IotHubs/WebRPiIoTHub/DeviceExplorer




