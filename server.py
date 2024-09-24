import socket as s 
from threading  import Thread
from subprocess import PIPE,Popen,STDOUT
   
def start_new_math(conn,addr,st):
    t=mathservercommunicationthread(addr,conn,st)
    t.start()
       
class processoutputthread(Thread):
    def __init__(self,proc,conn,st):
        Thread.__init__(self)
        self.proc=proc
        self.conn=conn
        self.st=st
    def run(self):
        while not self.proc.stdout.closed and self.st=="open":
            send=self.proc.stdout.readline()
            self.conn.sendall(send)
   
class mathservercommunicationthread(Thread):   
    def __init__(self, addr,conn,st):
        Thread.__init__(self)
        self.addr=addr
        self.conn=conn
        self.st=st
              
    def run(self):
        p=Popen(['bc','-i'],stdout=PIPE,stdin=PIPE,stderr=STDOUT,shell=True)
        output=processoutputthread(p,self.conn,self.st)
        output.start()
        while not p.stdout.closed:
            data=self.conn.recv(1024)
            if not data:
                break
            else:
                data=data.decode()
                data=data.rstrip()
                if data =='quit' or data =='exit':
                    p.communicate(data.encode(),timeout=1)
                    self.st="close"
                    self.conn.close()
                    p.kill()
                    if p.poll()is not None:
                        break
                p.stdin.write((data+'\n').encode())
                p.stdin.flush()
            
host=""
port=5555

sock=s.socket(s.AF_INET,s.SOCK_STREAM)

sock.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)

socket_status="open" 
sock.bind((host,port))
sock.listen()
while True:
    conn,addr=sock.accept()
    start_new_math(conn,addr,socket_status)
    
s.close()
    


    
    
