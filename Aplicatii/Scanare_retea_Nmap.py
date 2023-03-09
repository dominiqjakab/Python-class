#!/usr/bin/python3

### Algorith used to scan the network ###
### apt-get python3-nmap python-nmap
import nmap3, nmap, os

### PART 0 ### Variable allocation

object = nmap.PortScanner()
ports = '20-80'
devices = ''
# print(dir(nmap))

### PART 1 ### Obtaining the devices in the network ###

print("Getting devices from network...")

devices = os.popen('arp -n | cut -f1 -d \' \' | grep [0-9]').read()

### PART 2 ### Formatting the data for processing

devices = devices.split('\n')
devices = devices [:-1]
print(devices)

### PART 3 ### Scanning the IP addresses

print("Waiting to scan...")

nr = 1
for ip in devices:
    print("Scanning device..." + str(nr))
    res = object.scan(ip, ports)
    print(res)
    nr = nr + 1

print("Scan is done.")