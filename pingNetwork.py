import os

FirstIP = input("input the first ip of a network ") 
IPbase = FirstIP.rsplit('.', 1)[0]
ENDip = FirstIP.split(".")[-1]
FirstMachine = int(ENDip)

for x in range(FirstMachine, 254):
    machine = str(x)
    PingIP = IPbase + "." + machine
    response = os.system(f"ping -c 1 {PingIP} > /dev/null")
    if response == 0:
        print(f"{PingIP} is up!")
    else:
        print(f"{PingIP} is down!")