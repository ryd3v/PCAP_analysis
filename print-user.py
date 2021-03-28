import pyshark

count = 0

capture = pyshark.FileCapture('sample.pcap', display_filter='http contains user')

for packet in capture:
    count = count + 1

print(count)