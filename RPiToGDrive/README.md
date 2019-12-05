# RPi To GDrive

## Create GDrive folder and GSheets file

Rpi/GSheetsAPI.gsheet

## Console Cloud from Google

https://console.cloud.google.com

### Create new project

Project Name: GSheetsAPI
Project ID: sheets-api-256717
Project Number: 701043255328

### Add APIs & Services for your project (sheets-api-256717)

Dashboard for project 
https://console.developers.google.com/apis/dashboard?project=sheets-api-256717

Credentials for project 
https://console.developers.google.com/apis/credentials?project=sheets-api-256717

Library for project 
https://console.developers.google.com/apis/library?project=sheets-api-256717

#### GDrive Choose & Enable & Credentials

https://console.developers.google.com/apis/library/drive.googleapis.com?id=e44a1596-da14-427c-9b36-5eb6acce3775&project=sheets-api-256717

https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=sheets-api-256717

Create credentials 
https://console.developers.google.com/apis/api/drive.googleapis.com/credentials?project=sheets-api-256717

Help me choose
> Which API are you using?
Google Drive API
> Where will you be calling the API from?
WebServer (NodeJS or TomCat)
> What data will you be accessing?
Application Data
> Are you planning to use this API with App Engine or Compute Engine?
No

Service Account Name: GDriveWebServerAppDataNoProjEd
Service Account Role: Project Editor
Service Account Id: gdrivewebserverappdatanoprojed
Service Account JSON: GSheetsAPI-73b82ffff956.json

#### GSheets Choose & Enable & Credentials

https://console.developers.google.com/apis/library/sheets.googleapis.com?id=739c20c5-5641-41e8-a938-e55ddc082ad1&project=sheets-api-256717

https://console.developers.google.com/apis/api/sheets.googleapis.com/overview?project=sheets-api-256717

Create credentials
https://console.developers.google.com/apis/api/sheets.googleapis.com/credentials?project=sheets-api-256717

## Processor

vcgencmd measure_temp

vcgencmd get_mem arm && vcgencmd get_mem gpu

sysbench --test=cpu --cpu-max-prime=20000 --num-threads=4 run


```
#!/bin/bash
# Script: my-pi-temp.sh
# Purpose: Display the ARM CPU and GPU  temperature of Raspberry Pi 2/3 
# Author: Vivek Gite <www.cyberciti.biz> under GPL v2.x+
# -------------------------------------------------------
cpu=$(</sys/class/thermal/thermal_zone0/temp)
echo "$(date) @ $(hostname)"
echo "-------------------------------------------"
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)"
echo "CPU => $((cpu/1000))'C"
```
## FitBit

### Create Fitbit Application

| Key                        | Value                            |
| -------------------------- | -------------------------------- |
| ApplicationName            | RPiFit                           |
| Description                | Raspberry Pi 3 Fitbit            |
| Application WebSite        | http://google.com                |
| Organization               | Mine                             |
| Organization WebSite       | http://google.com                |
| Terms Of Service Url       | http://google.com                |
| Privacy Policy Url         | http://google.com                |
| OAuth 2.0 Application Type | personal                         |
| Callback URL               | http://127.0.0.1:8080/           |
| Default Access Type        | Read-Only                        |
| OAuth 2.0 Client ID        | 22BDC9                           |
| Client Secret              | cc41ea02e5519cbcd457c357cec3d24c |

### Manage Fitbit Application

https://dev.fitbit.com/apps

### Unofficial API

https://github.com/orcasgit/python-fitbit

```
git clone https://github.com/orcasgit/python-fitbit.git
cd python-fitbit
sudo pip install -r requirements/base.txt
sudo pip install -r requirements/dev.txt
sudo pip install -r requirements/test.txt
```