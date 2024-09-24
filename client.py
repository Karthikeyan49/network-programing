import sys
import socket as soc
from threading import Thread
import os

class clientoutputthread(Thread):
    def __init__(self,conn):
        Thread.__init__(self)
        self.conn=conn
        
    def run(self):
        while s.fileno()>0:
            data=self.conn.recv(1024).decode()
            if(not data):
                self.conn.close()
                print("exit by foregin host")
                os._exit(-1) 
            else:
                print(data,end='')           
if len(sys.argv)<=3:
    host=sys.argv[1]
    port=sys.argv[2]

s=soc.socket(soc.AF_INET,soc.SOCK_STREAM)
# state="open"

try:
    s.connect((str(host),int(port)))
except Exception as e:
    print("cannot connect the {}:{}...".format(host,port))
    print(str(e))
    sys.exit(-1)
  
output=clientoutputthread(s)   
output.start()

while s.fileno()>0:
    try:
        msg=input()
        s.send(msg.encode())
    except:
        break

    