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

## Mount external disk

Add power to USB port Add the following to the end

```
sudo echo -e "max_usb_current=1" >> /boot/config.txt
```

Install NTFS support

```
sudo apt-get install ntfs-3g ntfs-config ntfsprogs gdisk
```

Use parted to check USB  and print devices

```
sudo parted
print all
select /dev/sda
print
```

Create new GUID partition table and verify

```
mklabel gpt
print
```

Create 16G 'os' partition

```
mkpart
# Provide the following information when prompted
# Partition name: os
# File system type: ext4
# Start: 0gb
# End: 16gb
```

Create 6G 'data-ext4' partition

```
mkpart data-ext4 ext4 16gb 75%
```

Create 2G data-ntfs partition

```
mkpart data-ntfs ntfs 22gb 100%
print
q
```



