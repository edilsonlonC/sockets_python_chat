import socket
import threading
import sys
import pickle

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients = []

def send_broadcast (data,conn):
    for c in clients:
        try:
            
            if c != conn:
                print (clients)
                c.send(data)
        except:
            clients.remove(c)

def accept_connection():
    print ('Acepted connection')
    while True:
        try:
            conn , addr = server.accept()
            conn.setblocking(False)
            clients.append(conn)
            
        except:
            pass

def process_connection():
    print('connection is processed')
    while True:
        if len(clients) > 0: 
            for c in clients:
                try:
                    data = c.recv(1024)
                    
                    if data: 
                       
                        send_broadcast(data,c)
                except:
                    pass


    
if __name__ == "__main__":

    server.bind((HOST,PORT))
    server.listen(10)
    server.setblocking(False)
    accept = threading.Thread(target=accept_connection)
    process = threading.Thread(target=process_connection)
    accept.daemon = True
    accept.start()
    process.daemon = True
    process.start()
    while True:
        data = input('->')
        if data == 'salir':
            server.close()
            sys.exit()
        