# Top 10 thing to do

## Install `Git`

## Configure bash aliases

## Install a Terminal Multiplexer (tilix, tmux, screen)

> apt-get -y install tilix tmux

## Install Your Favorite Hacking Tools (Aircrack-Ng, BeEF, Burp Suite, Hydra, Nikto, Maltego, Nmap, Wireshark)

> apt-get -y install maltego metasploit-framework burpsuite wireshark aircrack-ng hydra nmap beef-xss nikto

## Install the Latest Version of Tor

```
echo 'deb https://deb.torproject.org/torproject.org stretch main
deb-src https://deb.torproject.org/torproject.org stretch main' > /etc/apt/sources.list.d/tor.list
```

> wget -O- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | sudo apt-key add -

```
apt-get update
apt-get install tor deb.torproject.org-keyring
```

## Configure File Sharing with Syncthing

## Install a Code Editor

> apt-get install gvfs gvfs-common gvfs-daemons gvfs-libs gconf-service gconf2 gconf2-common gvfs-bin psmisc

> dpkg -i ~/Downloads/atom-amd64.deb

## Clone Rubber Ducky Encoder

## Change SSH Keys & Default Password
