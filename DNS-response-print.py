# How many DNS responses contain "string" domain name
from scapy.all import *
counter = 0
for packet in PcapReader('sample.pcap'):
    if packet.haslayer(DNSRR):
        if isinstance(packet.an, DNSRR):
            counter = counter +1
            print(counter, packet.an.rrname)