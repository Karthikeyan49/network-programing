import socket as sock
from threading import Thread

host=""
port=5555

# thread class
# constructor(self)

class muilthreadclienthandle(Thread):
    def __init__(self,conn,s):
        Thread.__init__(self)
        self.connection=conn
        self.s=s
    def run(self):
        output=processoutputthread(self.connection,self.s)
        output.start()
        
        while True:
            inpt=input()
            for i in clients:
                i.sendall(inpt.encode())
            
            
class processoutputthread(Thread):
    def __init__(self,conn,s):
        Thread.__init__(self)
        self.connection=conn
        self.s=s
    def run(self):
        while True:
            data=self.connection.recv(1024)
            data=data.decode().rstrip()
            if data=='quit':
                self.s.close()
                self.connection.close()
                break
            self.connection.send(data.encode())
            
s=sock.socket(sock.AF_INET,sock.SOCK_STREAM)
s.setsockopt(sock.SOL_SOCKET,sock.SO_REUSEADDR,1)
       
s.bind((host,port))
s.listen()
print("listening.....")
clients=[]

while True:
    conn,addr=s.accept()
    clients.append(conn)
    client=muilthreadclienthandle(conn,s)
    client.start()






    
# step :1 socket config: address family,tcp/udp
#step 2: options: level,optname,buffer reable
# server ip many port(gateway) 
# table clinet ip 
# tcp-relaible protocol -packets
# udp-faster-datagrams

# -clinet ip mnay port

# step 3:ip port bind
# step 4:listen()
# step 5:accept()

# ipv4 -32 255.255.255.255
# ipv6 -128 
# full duplex and half duplex

# io blocking
# create new process/thread

# process
# task varibales,function,disk space

# thread -inside the 
# memory