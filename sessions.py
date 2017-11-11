
from Generation import * 

# Constants -------------------------------------------------------------------
___NAME = 'Sessions Protocol'
___VER = '0.0.0.1'
___DESC = 'Simple Sessions protocol (server-side)'
___BUILT = '2016-08-23'
___VENDOR = 'Copyright (c) 2016 DSLab'
# Private variables -----------------------------------------------------------
__M = [] # Received messages (array of tuples like ( ( ip, port), data)
__S = {} # Sessions
__OUTBOX = {}
__INBOX = {}
__sess_id_counter = 0
g_c = 0


#return_question_and_answer question (blank),answer (filled)
#



class Game_Session():


    def __init__(self, session_size):
	'''Creating new session with specified size'''
	global __sess_id_counter
        global __S
	global g_c
        for i in range(10):
            g_c += 1
            print g_c
	self.session_size = session_size
	self.session_id = __sess_id_counter
	
	# call function from Generation.py
	question, answer = return_question_and_answer()
	self.sudoku_full = answer
	self.sudoku_current = question

	# Update global variables
	__sess_id_counter += 1
	__S[source+(uuid,)] = {}

    def return_session_id(self):
	return self.session_id

    def return_session_size(self):
	return self.session_size

    def return_sudoku_current(self):
	return self.sudoku_current

    def return_sudoku_full(self):
	return self.sudoku_full
        



def new_session(source):
    '''Create new session, give it unique iD
    @param source: tuple ( ip, port ), socket address of the session originator
    @returns int, new session iD
    '''
    global __sess_id_counter
    global __S
    uuid = __sess_id_counter
    __sess_id_counter += 1
    __S[source+(uuid,)] = {}
    return uuid

