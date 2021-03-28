from scapy.all import *

counter = 0

for packet in PcapReader('sample.pcap'):
    if packet.haslayer(DNS):
        counter = counter + 1

print("Total DNS packets: "+str(counter))