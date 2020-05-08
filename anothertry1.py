#!/usr/bin/python

import socket
import os

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usrtarg = input("Please Enter Target: ")
target = f'{usrtarg}'
print("Your Target Is: ",target)

usrport1 = input("Please Enter Starting Port: ")
targport1 = f'{usrport1}'

usrport2 = input("Please Enter Ending Port: ")
targport2 = f'{usrport2}'

print("Port Range Selected: ", usrport1, "-", usrport2)


def ban(target, xport):
    bannergrabber = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
    bannergrabber.settimeout(3)     
    try:
        bannergrabber.connect((target, xport))
        bannergrabber.send(b"GET / \r\n")
        banner = str(bannergrabber.recv(4096), 'ascii')
        bannergrabber.close()
        print (ascii(banner), "\n")
    except: #Exception:
        print ("Cannot connect to port ", xport)
   
def portscan(port):
    try:
        print(target, "Port: ", port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))
        if result == 0:
            s.close()
            return True
        s.close()
    except:
        return False


for xport in range(int(usrport1), int(int(usrport2) + 1)):    
    if portscan(xport):
        print("Port", xport, "is Open!")
        ban(target, xport)
    else:
        print("Port", xport, "Closed")
        continue



