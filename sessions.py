import binascii
from Generation import * 
import os
import pickle
from threading import Thread, Lock, Condition
import time
# Constants -------------------------------------------------------------------
___NAME = 'Sessions Protocol'
___VER = '0.0.0.1'
___DESC = 'Simple Sessions protocol (server-side)'
___BUILT = '2016-08-23'
___VENDOR = 'Copyright (c) 2016 DSLab'
# Private variables -----------------------------------------------------------
M = [] # Received messages (array of tuples like ( ( ip, port), data)
S = {} # Sessions
GH = {}
OUTBOX = {}
INBOX = {}
sess_id_counter = 0
cv_session = Condition()
#from server import cv_session

#return_question_and_answer question (blank),answer (filled)
#
def get_name(token):
   
    print "get name by token ", token
    return GH[token].get_name()

def add_player(token, nick, socket):
    GH[token].add_player(nick, socket)

def remove_player(token, nick, socket):
    GH[token].remove_player(nick, socket)

class Player():
    def __init__(self, name, socket):
        self.name = name
        self.socket = socket

    def get_name(self):
        return self.name

    def get_socket(self):
        return self.socket

    def send(self, data):
        try:
            self.socket.send(data)
            return True
        except:
            print "cannot send data to player ", self.name
            return False


class GameHandler(Thread):

    def __init__(self, GameSession):
        Thread.__init__(self)
        self.session = GameSession
        self.players = {}
        #self.lock_layers = Lock()
        self.cv_players = Condition()
        self.cv_turn = Condition()
        #self.lock = Lock()
        print "Game Session ", self.session.name, " started!"

    def add_player(self, name, socket):
        with self.cv_players:
            self.players[name] =  socket
            self.cv_players.notify()


    def remove_player(self, name, socket):
        with self.cv_players:
            del self.players[name]
            self.cv_players.notify()

    def play_turn(self, point, value, player):
        # TO DO 
        self.cv_turn.notify()

    def get_token(self):
        return self.session.get_token()
     
    def get_name(self):
        return self.session.get_name()

    def run(self):
        
        with self.cv_players:
            while True:    
                if not len(self.players) == self.session.size:
                    print "waiting players ", len(self.players), "/", self.session.size 
                else:
                    print "Enough players! Staring game..."
                    break
                self.cv_players.wait()
        

        self.cv_turn.acquire()
        while len(self.players) > 0:
           # check game state
           print "Someone play turn"
           self.cv_turn.wait()
        print "No players left. Game session ", self.get_name()," closed!"
        self.cv_turn.release()

class GameSession():

    def __init__(self, session_size):
	'''Creating new session with specified size
        @param session_size: max number of players in session
        '''
	global sess_id_counter
	self.size = session_size
        #generate session token
	self.token = binascii.hexlify(os.urandom(16))
	sess_id_counter += 1
	self.id = sess_id_counter
        # call function from Generation.py
	question, answer = return_question_and_answer()

        #board
	self.sudoku_full = answer

        #current state
	self.state = question

        #session name
        self.name = {}

    def get_token(self):
        return self.token

    def get_size(self):
        return self.size

    def get_state(self):
        return self.state

    def get_total(self):
        return self.sudoku_full

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

def new_session(source, session_size, name):
    '''Create new session, give it unique iD
    @param source: tuple ( ip, port ), socket address of the session originator
    @param session_size: max number of players in session
    @returns hex, session token
    '''
    global S, GH, cv_session
    with cv_session:
        sess = GameSession(session_size)
        token = sess.get_token()
        sess.set_name(name)
        S[token] = sess
        GH[token] = GameHandler(sess)
        GH[token].start()
        cv_session.notify()

    
    #print "Sess token ", token
    return GH[token]

def get_session(name):
   
    print "get session ", name
    for k, v in GH.items():
        if v.get_name() == name:
            return GH[k]
    
def save_sessions(cv):
    with cv:
        global S
        with open("sessions.bin", 'wb') as f:
            pickle.dump(S, f, pickle.HIGHEST_PROTOCOL)
    
    cv.notify()


def current_sessions():
    sess_names = [ x.get_name() for x in GH.values() ] 
    return sess_names

def load_sessions():
    global S
    try:
        with open('sessions.bin', 'rb') as handle:
            S = pickle.load(handle)
        if len(S) > 0:
            print len(S), " session loaded!"
            print S
            sess_names = [ x.name for x in S.values() ]
            return sess_names
        else:
            return []
            print "No loaded sessions!"
    except:
        print "No session dump!"
        return []
