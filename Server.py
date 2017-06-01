#!/usr/bin/env python

import os
import socket
from SocketServer import TCPServer,BaseRequestHandler


SERVER  = "127.0.0.1"
PORT = 9999



class tcphandler(BaseRequestHandler):
    """
    """
    def __init__(self,queue_to_put,queue_to_get):
        super(self.__init__())
        self.queue_to_get = queue_to_get
        self.queue_to_put = queue_to_put

    def handle(self):
        self.data = self.request.recv(1024)
        self.queue_to_put.put(self.data)
        data = self.queue_to_get.get()
        self.request.sendall(data)

def main():
    queue_to_get = None
    queue_to_put = None

    server = TCPServer((SERVER,PORT),tcphandler(queue_to_get,queue_to_put))
    server.serve_forever()
    return

if __name__ == "__main__":
    main()