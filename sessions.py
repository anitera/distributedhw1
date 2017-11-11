import binascii
from Generation import * 
import os
# Constants -------------------------------------------------------------------
___NAME = 'Sessions Protocol'
___VER = '0.0.0.1'
___DESC = 'Simple Sessions protocol (server-side)'
___BUILT = '2016-08-23'
___VENDOR = 'Copyright (c) 2016 DSLab'
# Private variables -----------------------------------------------------------
M = [] # Received messages (array of tuples like ( ( ip, port), data)
S = {} # Sessions
OUTBOX = {}
INBOX = {}
sess_id_counter = 0



#return_question_and_answer question (blank),answer (filled)
#



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

        #current players
        self.players = {}

    def get_token(self):
        return self.token

    def get_size(self):
        return self.size

    def get_state(self):
        return self.state

    def get_total(self):
        return self.sudoku_full

    def add_player(self, source):
        self.players[source] = 0

        

def new_session(source, session_size):
    '''Create new session, give it unique iD
    @param source: tuple ( ip, port ), socket address of the session originator
    @param session_size: max number of players in session
    @returns hex, session token
    '''
    global S
    sess = GameSession(session_size)
    token = sess.get_token()
    sess.add_player(source)
    S[token] = sess
    return token
 
