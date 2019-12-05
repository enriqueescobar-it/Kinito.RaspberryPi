# Installation

## Raspbian Installation

```
sudo apt-get install pijuice-base pijuice-gui
```

## Kali Linux Installation

https://github.com/PiSupply/PiJuice/tree/master/Software

https://github.com/PiSupply/PiJuice/issues/405

```
apt-get -y install python3-urwid
apt-get -y install python3-tk
apt-get -y install i2c-tools
apt-get -y install lua5.3
dpkg -i ./pijuice-base_1.5_all.deb
dpkg -i ./pijuice-gui_1.5_all.deb
```

Add user root to group pijuice run sudo visudo add root ALL=(pijuice) ALL save and exit.

```
git clone https://github.com/PiSupply/PiJuice.git
cd PiJuice/Software/Install
dpkg -i pijuice-base_1.5_all.deb
apt --fix-broken install
dpkg -i pijuice-gui_1.5_all.deb
apt --fix-broken install
```
