from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser
import curses
import os
from login import *
from host_port_authorization import *
from Board_gui import *
buffer_length = 1024


if __name__ == '__main__':

    nick = enter_nickname()

    print "Your nickname: ", nick
    
    s = socket(AF_INET, SOCK_STREAM)

    while True:
        #inpt = raw_input("Enter dedicated host address [ip:port]: ")
        HP = HostPort()
        hostPortAuthorization(HP)
        host, port = HP.getHostPort()
        if port.isdigit():
            port = int(port)
            if s.connect_ex( (host, port) ) != 0:
                print "Incorrect host address. Try again!"
            else:
                print "Connection established!"
                break
    
    print "Multiplayer Game"

    # here we need to know id of our session and max number of clients
    session_id = 0
    session_size = 4
    
    # get current players and their score from session with dictionary table_score = { 'nickname': score}
    table_score = {'olha': 0, 'slava': 0, 'rita': 0, 'vasya': 0}

    return_board(nick, host, port, session_id, session_size, table_score)



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
