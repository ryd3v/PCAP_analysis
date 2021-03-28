from scapy.all import *

# Read the packets from the pcap file
packets = rdpcap('sample.pcap')

for packet in packets:
    packet_amount = len(packets)
    
print(len (packets))    
