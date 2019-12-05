# Installation

## Conky Installation

```
sudo apt-get -y install conky kate terminator
```

Download the conkyrc file to home directory as .conkyrc

```
wget -O /home/pi/.conkyrc https://raw.githubusercontent.com/enriqueescobar-askida/Kinito.RaspberryPi/master/Setup/rpi3_conkyrc.txt
```

Create a refresh rate file

> sudo nano /usr/bin/conky.sh

```
#!/bin/sh
(sleep 10s && conky) &
exit 0
```

Create an auto launch file

> sudo nano /etc/xdg/autostart/conky.desktop

```
[Desktop Entry]
Name=conky
Type=Application
Exec=sh /usr/bin/conky.sh
Terminal=false
Comment=system monitoring tool.
Categories=Utility;
```
