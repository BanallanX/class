#!/usr/bin/python

import os
import re
from datetime import datetime
import socket
import time
import threading
from queue import Queue



print_lock = threading.Lock() 

usrtarg = input("Please Enter Target: ")
target = f'{usrtarg}'
print("Your Target Is: ",target)

usrport1 = input("Please Enter Starting Port: ")
targport1 = f'{usrport1}'

usrport2 = input("Please Enter Ending Port: ")
targport2 = f'{usrport2}'

print("Port Range Selected: ", usrport1, "-", usrport2)


def portscan(port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn = soc.connect((target, port))

        with print_lock:
            print('Port', port, 'is open!')
        conn.close()    
    except:
        pass

        # print("Port", port, "closed")
        # return False
#
#for x in range(1,26):
#    if portscan(x):
#        print("Port", x, "is open")
#    else:
#        print("Port", x, "closed")    
start = time.time()
def threader():
    while True:
        pnum = q.get()
        portscan(pnum)
        q.task_done()
q = Queue()
for x in range(10000):
    thr = threading.Thread(target=threader)
    thr.daemon = True
    thr.start()
for pnum in range(int(targport1), int(int(targport2) + 1)):
    q.put(pnum)
q.join()
print("Completed In: ", time.time()-start, "Seconds")

#print(portscan(port))

# def bannergrabbing(target, port):
# #    '''Connect to process and return application banner'''
#     print ("Gettig service information for port: ", port)
#     bgs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     socket.setdefaulttimeout(2)
#     try:
#         bgs.connect((target, port))
#         bgs.send('WhoAreYou\r\n')
#         banner = bgs.recv(1024)
#         bgs.close()
#         print (banner, "\n")
#     except:
#         print ("Cannot connect to port ", port)

# def portscanner(address, start, end):
#     open_ports = []
#     # scan port range for host
#     for port in range(start_port, end_port):
#         open_port = scanport(target, port)
#         if open_port is None:
#             continue
#         else:
#             open_ports.append(open_port)
#     return open_ports

# def get_service_banners_for_host(address, portlist):
#     for port in portlist:
#         bannergrabbing(target, port)



# open_ports = portscanner(target, targport1, targport2)

# get_service_banners_for_host(target, open_ports)



