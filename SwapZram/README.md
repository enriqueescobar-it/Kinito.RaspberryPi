# SWAP & RAM Setup

## RAM Setup

https://www.bitpi.co/2015/02/11/how-to-change-raspberry-pis-swapfile-size-on-rasbian/

https://www.framboise314.fr/et-si-on-se-passait-du-swap/

http://blog.nunosenica.com/reduce-write-operations-to-sd-card-with-raspbian/

http://duinorasp.hansotten.com/sd-card-lifetime-how-to-extend/

https://www.zdnet.com/article/raspberry-pi-extending-the-life-of-the-sd-card/

## SWAP setup

> sudo apt-get -y install dphys-config dphys-swapfile

> sudo apt-get install zram-config zram-tools udisks2-zram

```
sudo su
service dphys-swapfile stop
nano /etc/dphys-swapfile
	# The default value of CONF_SWAPSIZE in Raspbian is 100.
	# We will need to change this to: (empty) ,1024, and so on.
	# After installing RStudio, it would be better to restore
	# the value of CONF_SWAPSIZE to the initial value in order
	# to stand a micro SD card long use.
service dphys-swapfile start
```

### zRAM Setup

If you use heavy memory aplications and little cpu, you will probably see a increase in performance with ZRAM. On the other side, a CPU bound application with little memory usage will see a possible DECREASE in performance (as RAM usage might trigger the ZRAM and steal some cpu cycles that would otherwise would go to the app)

you need to monitor your machine for cpu and ram/swap usage to view it's the long term usage.

* If free RAM, no swap, ZRAM is useless.
* If free RAM, some swap usage, but less than the free RAM, ZRAM is useless, just tune the swappiness so the swap is less used
* If free RAM, some swap usage, but a lot more than free RAM, try first to tune the swappiness and the apps, to decrease the ram usage. If no change, try ZRAM is our cpu is free most of the time
* If no free RAM, swap usage high, ZRAM might be a good idea, even if CPU is used, as IO operation might be blocking the CPU more than what you would lose with ZRAM
again, all depends of what you use and how you use the RaspberryPI (or any computer)

Script to dynamically enable ZRAM on a Raspberry Pi or other Linux system.

Automatically detects the number of CPU cores to allocate to ZRAM computation, disables existing swap and enables ZRAM swap.

Download the script and copy to /usr/bin/ folder

> sudo wget -O /usr/bin/zram.sh https://raw.githubusercontent.com/enriqueescobar-askida/Kinito.RaspberryPi/master/SwapZram/zram.sh

Make file executable

> sudo chmod +x /usr/bin/zram.sh

Edit /etc/rc.local file to run script on boot

> sudo nano /etc/rc.local

Add line before exit 0

> /usr/bin/zram.sh &

However, I'm running system with 32 GiB of RAM, zero real swap and I've installed zram-config but modified `/etc/init/zram-config.conf` to use only 5% of RAM for zram (instead of default 50%).
This allows kernel to see some swap but that swap is hugely faster than any `SDD`.
As a result, all swap-related codepaths inside kernel can be used and I think this has fixed some issues that I had when I didn't have swap at all.
(Namely, it seems to me that when RAM is fragmented and the system does not have any swap, the kernel is not clever enough to workaround the problem. However, with zRam or swap on ramdisk, the kernel is able to move pages to swap and relocate during swapin.
That's only my theory, though.)
