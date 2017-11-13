from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser
import curses
import os
from login import *
from host_port_authorization import *
from sessions_authorization import *
from Board_gui import *
import time
buffer_length = 5024

from protocol import *
import pickle
import random
from threading import Thread, Lock
import signal

class GamePlaying():

    def __init__(self, socket, nick):
        self.s = socket
        self.nick = nick
        self.buffer_size = 1024
        self.game = True
        self.l_game = Lock()

    def get_state(self):
        with self.l_game:
            status = self.game
        return status

    def run(self):
        self.playing = Thread(target=self.playing_game)
        self.listeting = Thread(target=self.listeting_server)
        self.playing.start()
        self.listeting.start()

    
    def close(self):
        with self.l_game:
            self.game = False
        self.playing.join()
        print "play thread done"
        s.send(DELIM.join([DISCONNECT]))
        self.s.close()
        self.listeting.join(1)
        print "listen thread done"
            

    def playing_game(self):
        while True:
            with self.l_game:
                status = self.game
            if status == True:
                print "playing.."
                time.sleep(10)
                cell = list([random.randint(1,9), random.randint(1,9)])
                value = random.randint(1,9)
                data = DELIM.join([PLAY_TURN,str(cell[0]), str(cell[1]), str(value)] )
                s.send(data)
            else:
                print "game over"
                break
    

    def listeting_server(self):
        while True:
            with self.l_game:
                status = self.game
            if status == True:
                msg = self.s.recv(self.buffer_size).split(DELIM)
                if msg[0] == GAME_END:
                    with self.l_game:
                        self.game = False
                    print "game ended from server!"
                    break
            else:
                break



def stop_execution(signum, taskfrm, game):
    print('You pressed Ctrl+C!')
    game.close()


from functools import partial

def sigint_handler(signum, frame, obj):
    obj.close()

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
    #s_ret = sessionStart(sessions)
    #print 'We return value yiiiii', s_ret[0]
    #print 'name ', s_ret[1]
    # here we need to know id of our session and max number of clients
    flag_of_new_session = False
    current_session = ""
    if len(sessions) > 0:
        print "Current session"
        for ss in sessions:
            print ss

        sess_name = raw_input("choose sess name or 0 to procceed: ")
        if sess_name == "0":
            print "create a new sesson"
            flag_of_new_session = True
        else:
            snames = [x[1] for x in sessions ] 
            if sess_name in snames:
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
        s.send(DELIM.join([NEW_SESSION, sess_name, str(sess_size), nick]))
	# s.send(('3' + args.size).encode('utf-8') + '\n' + str(size).encode('utf-8'))
	#print '0' + nick + str(session_size)
	#s.send('0' + ' ' + nick + ' ' + str(session_size))
    else: 
        print "Session=", current_session, " Nick=", nick
        s.send(DELIM.join([OLD_SESSION, current_session, nick]))
	#s.send('1' + ' ' + nick + ' ' + str(session_id))
 

    '''getting session token, save it in client side and always send message with it
    because server should recognize for which session data incoming
    '''
    try:
        sess = s.recv(buffer_length)
        print "Session token ", sess
    except:
        print "socket errot"


    rspn = s.recv(buffer_length)
    
    if rspn == GAME_START:
        print "session started"
    else:
        print "session error"
    
    
    
    game = GamePlaying(s, nick)

    game.run()

    while True:
        exit = int(raw_input("exit?"))
        if exit == 1:
            game.close()
            break
        elif game.get_state() == False:
            game.close()
            break
    print "Thank you for playing!" 
    '''
    try:
        while True:
            print "playing.."
            time.sleep(10)
            cell = list([random.randint(1,9), random.randint(1,9)])
            value = random.randint(1,9)
            data = DELIM.join([PLAY_TURN,str(cell[0]), str(cell[1]), str(value)] )
            s.send(data)
    except KeyboardInterrupt:
        s.send(DELIM.join([DISCONNECT]))
        s.close()
    '''
    # get current players and their score from session with dictionary table_score = { 'nickname': score}
  #  table_score = {'olha': 0, 'slava': 0, 'rita': 0, 'vasya': 0}

#    return_board(nick, host, port, session_id, session_size, table_score)



    '''
    s = socket(AF_INET, SOCK_STREAM)

    server_address = (args.Host, int(args.port))

    s.connect(server_address)
    try:
        s.send(args.nickname)
    except socket.error:
        #print 'Socket error'
    try:
        message = s.recv(buffer_length) 
    except socket.error:
        print 'Socket error'
    print message

    if message == "1":
        print ""
    '''
    #s.close()
