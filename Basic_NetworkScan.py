#!/usr/bin/python3
import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])   #script name is considered arg 0 
    #gethostbyname > you can specify domain, it will convert to ip
else:
    print("missing argument")   
    print("scanner.py ip")   

print("-"*50)     #long linge to make it beautiful 
print("scanning target: "+target)
print("starting time"+str(datetime.now()))
print("-"*50)

try:
    for port in range(53,54):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
                print("port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
        print("Keyboard interupt")
        SystemExit

except socket.gaierror:
     print("Impossible to resolve hostname")

except socket.error:
     print("error while connecting")
