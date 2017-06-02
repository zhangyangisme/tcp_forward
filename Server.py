#!/usr/bin/env python
import os
import socket
import threading
from SocketServer import ThreadingTCPServer,BaseRequestHandler

ANYADDRESS = "0.0.0.0"
PORT_FOR_CLIENT = 9999
PORT_FOR_FORWARD = 8888

forward_socket_list = []

class client_handler(BaseRequestHandler):
    def __init__(self):
        super(self.__init__())
    def handle(self):
        if(len(forward_socket_list) == 0) :
            return
        else:
            conn = forward_socket_list[0]
            forward_socket_list.remove[0]
            self.request.settimeout(3)
            while True:
                data = self.request.read(1024)
                if(data == 0):
                    break;
                else:
                    conn.sendall(data)
        return

def forward_server():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
    sock.bind((ANYADDRESS,PORT_FOR_FORWARD))
    sock.listen(1000)
    while True:
        conn,address = sock.accept()
        forward_socket_list.append(conn)
    return


def main():
    forward_server_thread = threading.Thread(target=forward_server)
    forward_server_thread.start()
    client_server = ThreadingTCPServer((ANYADDRESS,PORT_FOR_CLIENT),client_handler)
    client_server.serve_forever()

if __name__ == "__main__":
    main()