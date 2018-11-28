# HomeServer
Home Server Description

## Original configuration

[Original config](/HomeServer/01_demos.txt)

## Network configuration and administration

```
ifoncfig
```

Edit network configuration

```
sudo nano /etc/network/interfaces
```

Reboot the system

```
sudo reboot
```

## Webmin installation

Create webmin.sources.list

```
sudo touch /etc/apt/sources.list.d/webmin.list
```

Add the following lines

'deb http://download.webmin.com/download/repository sarge contrib'

'deb http://webmin.mirror.somersettechsolutions.co.uk/repository sarge contrib'

```
sudo nano /etc/apt/sources.list.d/webmin.list
```

Install Webmin signing key

```
sudo su
cd /root
wget http://www.webmin.com/jcameron-key.asc
apt-key add jcameron-key.asc
exit
```

```
sudo apt-get update
sudo apt-get upgrade
```

Install Webmin and x11VNC

```
sudo apt-get -y install webmin x11vnc
```

Show the desktop

```
startx
```

Create x11VNC password

```
x11vnc -storepasswd
```

Create desktop configuration file

```
mkdir /home/pi/.config/autostart
nano /home/pi/.config/autostart/x11vnc.desktop
# Add the following lines[Desktop Entry]
# Encoding=UTF-8
# Type=Application
# Name=X11VNC
# Exec=x11vnc -forever -usepw -display :0 -ultrafilexfer
# StartupNotify=false
# Terminal=false
# Hidden=false
```

Reboot again show desktop

```
startx
```

