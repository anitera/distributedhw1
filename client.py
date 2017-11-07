from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser
import curses
import os
from login import *
buffer_length = 1024



if __name__ == '__main__':
    '''
    parser = ArgumentParser()
    parser.add_argument('-n','--nickname',\
                        help='nickname validation',\
                        required=False
                        )
    parser.add_argument('-p','--port',\
                        help='port',\
                        default=7777,\
                        required=False
                        )
    parser.add_argument('-H','--Host',\
                        help='host',\
                        required=False,\
                        default='127.0.0.1')
    args = parser.parse_args()
    '''
    nick = ""
    if (load_nicknames()):
        while True:
            opt = raw_input("Load nick? y/n ")
            if opt == "y":
                nick = load_nickname()
                break
            if opt == "n":
                nick = enter_nickname()
                break
            print "Wrong input! Enter \"y\" for Yes and \"n\" for No"
    else:
        nick = enter_nickname()
                       

    print "Your nickname: ", nick
    
    s = socket(AF_INET, SOCK_STREAM)

    while True:
        inpt = raw_input("Enter dedicated host address [ip:port]: ")
        host, port = inpt.split(":")
        port = int(port)

        if s.connect_ex( (host, port) ) != 0:
            print "Incorrect host address. Try again!"

        else:
            print "Connection established!"
            break
    
    print "Multiplayer Game"
    '''
    s = socket(AF_INET, SOCK_STREAM)

    server_address = (args.Host, int(args.port))

    s.connect(server_address)
    try:
        s.send(args.nickname)
    except socket.error:
        print 'Socket error'
    try:
        message = s.recv(buffer_length) 
    except socket.error:
        print 'Socket error'
    print message

    if message == "1":
        print ""
    '''
    s.close()
