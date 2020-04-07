#!/usr/bin/python3

#   import pcap library
import pcopy

#   find and print devices 
devices = pcapy.findolldevs
print(devices)

# device, # of byes to capture per packet, promiscuous mode, timeout (ms)
capture = pcapy.open_live("en0", 65536, 1 ,0)

count = 1
while count:
    # print count of packets
    (header, payload) = capture.next()
    print(count)
    count = count + 1