import socket
import threading
import queue
import json 
import os
import os.path
import sys


IP = '127.0.0.1'
PORT = 8080     
messages = queue.Queue()
users = []   
lock = threading.Lock()

def onlines():    
    online = []
    for i in range(len(users)):
        online.append(users[i][0])
    return online

class ChatServer(threading.Thread):
    global users, que, lock


    def __init__(self):        
        threading.Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.chdir(sys.path[0])



    def receive(self, conn, addr):            
        user = conn.recv(1024)        
        user = user.decode()
        print('||||')
        users.append((user, conn))
        USERS = onlines()
        self.Load(USERS,addr)
        try:
            while True:
                print(1)
                message = conn.recv(1024)           
                message = message.decode()
                message = user + ':' + message
                # self.Load(message,addr)
                print('|||',message,addr)
            conn.close()


        except:   
            j = 0          
            for man in users:
                if man[0] == user:
                    users.pop(j)      
                    break
                j = j+1

            USERS = onlines()
            self.Load(USERS,addr)
            conn.close()



    def Load(self, data, addr):
        lock.acquire()
        try:
            messages.put((addr, data))
        finally:
            lock.release()        



    def sendData(self): 
        while  True:
            if not messages.empty():
                message = messages.get()
                if isinstance(message[1], str):
                    for i in range(len(users)):
                        data = ' ' + message[1]
                        users[i][1].send(data.encode())
                        print(data)
                        print('\n')

                if isinstance(message[1], list):
                    data = json.dumps(message[1])
                    for i in range(len(users)):
                        try:
                            users[i][1].send(data.encode())
                        except:
                            pass

    def run(self):
        try:
            print('|||', IP, PORT)
            self.s.bind((IP, PORT))
            self.s.listen(5)
            q = threading.Thread(target=self.sendData)
            q.start()
            print(1111)
            while True:
                print(11)
                conn, addr = self.s.accept()
                t = threading.Thread(target=self.receive, args=(conn, addr))
                t.start()
        finally:
            self.close()


if __name__ == '__main__':
    cserver = ChatServer()
    cserver.start()

