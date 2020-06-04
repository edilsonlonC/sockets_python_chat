import socket
import threading
import sys
import pickle

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '127.0.0.1'
PORT = 8000


def recv_message():
    print('message here ')
    while True:
        try:
            
            data = server.recv(1024)
            if (data):
                print('\n',pickle.loads(data))
        except:
            pass

def send_messagge(msg):
    server.send(pickle.dumps(msg))



if __name__ == "__main__":
    
    server.connect((HOST,PORT))
    msg_recv = threading.Thread(target=recv_message)
    msg_recv.daemon = True
    msg_recv.start()
    mesg_server = ''

    #send nick name
    while mesg_server != 'True':
        nick_name = input('username')
        send_messagge(nick_name)
        mesg_server =  pickle.loads(server.recv(1024))
        if !mesg_server:
            PRINT('CHECK NICKNAME')

    while True:
        data = input('->')
        if data != 'salir':
            print('yo : ' , data)
            send_messagge(data)
        else:
            server.close()
            sys.exit()