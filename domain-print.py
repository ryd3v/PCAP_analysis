from scapy.all import *

response_counter = 0

for packet in PcapReader('sample.pcap'):
    if packet.haslayer(DNSRR):
        response_counter = response_counter + 1
        

print("Total DNS Response packets: "+str(response_counter))