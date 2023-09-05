# pip3 install scapy
# download winpcap

import scapy.all as scapy
import socket


request = scapy.ARP()
request.pdst = '192.168.1.1/24'

broadcast = scapy.Ether() 
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
request_broadcast = broadcast / request

clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]

for element in clients:
    ip = element[1].psrc
    mac = element[1].hwsrc
    print(ip + "  :  " + mac)

try:
    a = socket.gethostbyaddr(ip)
    print("hostname: " + a[0])
except:
    print("Hostname: DESCONHECIDO")
