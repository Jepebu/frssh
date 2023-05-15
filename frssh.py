#!/usr/bin/python3


try:
    import paramiko
    import getpass3
    import threading
except ImportError:
    print("Missing one or more libraries: paramiko, getpass3, threading\n")
    exit()

hostList = open("hosts.txt","r")
hostList = hostList.readlines()


cmd = input("Enter the command you want to run:\n")
password = getpass3.getpass("Please enter your password:\n")

class createThread():
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name
        self.client = paramiko.client.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    def run(self):
        self.ran = (hostGroupN * (self.ID - 1)),(hostGroupN * self.ID)
        for n in range(int(self.ran[0]),int(self.ran[1])):
            try:
                print(hostList[n],flush=True)
                self.client.connect(hostList[n], username="root", password=password,timeout=5)
                _stdin, _stdout,_stderr = client.exec_command(cmd)
                print(_stdout.read().decode(),flush=True)
                if _stderr:
                    print(_stderr.read().decode(),flush=True)
                except:
                    print("Error on host",host[n],flush=True)
        self.client.close()

def main():
    threadA = createThread(1,"A")
    threadB = createThread(2,"B")
    
    if len(hostList) < 500:
        hostGroupN = (round(len(hostList)) / 2)
    else:
        print("Using 4 threads due to increased list size\n")
        hostGroupN = (round(len(hostList)) / 4)
        threadC = createThread(3,"C")
        threadD = createThread(4,"D")
        threadC.start()
        threadD.start()
        threadC.join()
        threadD.join()
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()    
        
if name == "__main__":
    main()

    