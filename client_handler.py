from threading import Thread
from protocol import *
from socket import error as soc_err
from sessions import *
import time
import pickle

class ClientHandler(Thread):
    def __init__(self, client_socket, client_addr): #need to take as argument game_session_id
        Thread.__init__(self)
        self.__client_socket = client_socket
        self.__client_address = client_addr
        self.buffer_size = 1024
        self.sess_names = []
	#self.game_session_id = game_session_id

    def set_sessions(self, sess_names):
        for id, name in enumerate(sess_names):
            self.sess_names.append( (id,name ) )

    def run(self):
        self.__handle()


    def __handle(self):
        try:
            print "Client connected from %s:%d" % (self.__client_address)
            if len(self.sess_names) > 0:
                self.__client_socket.send(pickle.dumps(self.sess_names, -1))
                #self.__client_socket.send(DELIM.join([ x for x in self.sess_names]))
            else:
                self.__client_socket.send("None")

                
            initial_reply = self.__client_socket.recv(self.buffer_size) 
	    print initial_reply

            initial_reply = initial_reply.split(DELIM)

	    if initial_reply[0] == '0':
		print 'Creating new session'
		print 'initial_reply[2] ', initial_reply[2]
                ''' creating new session using function
                !!! do not use class creation !!!!
                '''
		sess = new_session(self.__client_address, int(initial_reply[2]), initial_reply[1])
                print "Session ", sess.name, " created with token ", sess.token

                self.__client_socket.send(sess.token)
                save_sessions() 
            
	    # if he created new session 0 - sess = Game_Session()

            # call function gamesession to add client name first time game_session new_player_in_current_session
            #print "Client's nickname=", nick

            self.__client_socket.send(OK)
            while True:
                print "awaiting data"
                #receive answer from client: (i,j) 8

		#game_session solver(name, client_answer) - there check if it solved if yes return message
                time.sleep(10)
		#send table_score to client and/or message

        except soc_err as e:
            if e.errno == 107:
                print "Client left befor handle"
            else:
                print "error %s" % str(e)

        finally:
            self.__client_socket.close()

        print "client disconected"
