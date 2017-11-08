from threading import Thread
from protocol import *
from socket import error as soc_err
from sessions import *
import time

class ClientHandler(Thread):
    def __init__(self, client_socket, client_addr):
        Thread.__init__(self)
        self.__client_socket = client_socket
        self.__client_address = client_addr
        self.buffer_size = 1024

    def run(self):
        self.__handle()


    def __handle(self):
        try:
            print "Client connected from %s:%d" % (self.__client_address)
            self.__session = new_session(self.__client_address)
            print "Session ", self.__session, " created"

            nick = self.__client_socket.recv(self.buffer_size)

            print "Client's nickname=", nick

            self.__client_socket.send(OK)
            while True:
                print "awaiting data"
                time.sleep(10)
        except soc_err as e:
            if e.errno == 107:
                print "Client left befor handle"
            else:
                print "error %s" % str(e)

        finally:
            self.__client_socket.close()

        print "client disconected"
