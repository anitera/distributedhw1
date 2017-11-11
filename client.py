from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser
import curses
import os
from login import *
from host_port_authorization import *
#from sessions_authorization import *
from Board_gui import *
buffer_length = 5024

from protocol import *
import pickle
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
                
    #sessionStart() # session start window

    print "Multiplayer Game"
    
    sessions  = pickle.loads(s.recv(buffer_length))
    print sessions
    # here we need to know id of our session and max number of clients
    flag_of_new_session = True
    current_session = ""
    if not sessions[0] == "None":
        print "Current session"
        for ss in sessions:
            print ss

        sess_name = raw_input("choose sess name or 0 to procceed: ")
        if sess_name == "0":
            print "create a new sesson"
        else:
            if sess_name in sessions:
                current_session = sess_name
            else:
                print "Session doesnt exist"
    else:
        flag_of_new_session = True

    #session_id = 0
   # session_size = 4

    if flag_of_new_session:
        sess_name = raw_input("input sess name ")
        sess_size = int (raw_input("input sess size") )
        s.send(DELIM.join(["0", sess_name, str(sess_size), nick]))
	# s.send(('3' + args.size).encode('utf-8') + '\n' + str(size).encode('utf-8'))
	#print '0' + nick + str(session_size)
	#s.send('0' + ' ' + nick + ' ' + str(session_size))
    else: 
        pass
	#s.send('1' + ' ' + nick + ' ' + str(session_id))
 

    '''getting session token, save it in client side and always send message with it
    because server should recognize for which session data incoming
    '''
    #IDK WATA FUCK IS GOING ON BUT BUFFER ALWAYS END ON '1'
    sess = s.recv(buffer_length)[:-1]

    print "Starting session ", sess, " token"

    # get current players and their score from session with dictionary table_score = { 'nickname': score}
    table_score = {'olha': 0, 'slava': 0, 'rita': 0, 'vasya': 0}

#    return_board(nick, host, port, session_id, session_size, table_score)



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
