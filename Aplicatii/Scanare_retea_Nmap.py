#!/usr/bin/python3

import nmap3, nmap, os

### PART 0 ### Alocarea variabilelor

obiect = nmap.PortScanner()
ports = '20-80'
devices = ''
# print(dir(nmap))
### PART 1 ### Obtinerea device-urilor din retea

print("Getting devices from network...")

devices = os.popen('arp -n | cut -f1 -d \' \' | grep [0-9]').read()

### PART 2 ### Formatarea datelor pentru procesare

devices = devices.split('\n')
devices = devices [:-1]
print(devices)

### PART 3 ### Scanarea adreselor IP

print("Waiting to scan...")

nr = 1
for ip in devices:
    print("Scanning device..." + str(nr))
    res = obiect.scan(ip, ports)
    print(res)
    nr = nr + 1

print("Scan is done.")