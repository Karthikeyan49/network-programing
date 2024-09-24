import socket as sock
import sys
from threading import Thread

if len(sys.argv)==3:
    host=sys.argv[1]
    port=int(sys.argv[2])
else:
    print("usage: ./file.py host port")
    exit(-1)

class processoutputthread(Thread):
    def __init__(self,s):
        Thread.__init__(self)
        self.connection=s
    def run(self):
        while True:
            output=s.recv(1024)
            print(output.decode().rstrip())
            
s=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.setsockopt(sock.SOL_SOCKET,sock.SO_REUSEADDR,1)

try:
    s.connect((host,port))
    print("connected to server")
except Exception as e:
    print(e)
 
output=processoutputthread(s)
output.start()
   
while True:
    data=input()
    s.send(data.encode())
    print(s.recv(1024).decode())
    
# i/o blocking
    
