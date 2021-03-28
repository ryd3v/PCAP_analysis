from scapy.all import *

packets = rdpcap('sample.pcap')
# iterate through every packet
for packet in packets[0:5]:
    print(packet)
    print("\n")