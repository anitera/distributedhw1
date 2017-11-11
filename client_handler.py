from threading import Thread
from protocol import *
from socket import error as soc_err
from sessions import *
import time

class ClientHandler(Thread):
    def __init__(self, client_socket, client_addr): #need to take as argument game_session_id
        Thread.__init__(self)
        self.__client_socket = client_socket
        self.__client_address = client_addr
        self.buffer_size = 1024
	#self.game_session_id = game_session_id

    def run(self):
        self.__handle()


    def __handle(self):
        try:
            print "Client connected from %s:%d" % (self.__client_address)

            initial_reply = self.__client_socket.recv(self.buffer_size) 
	    print initial_reply

            initial_reply = initial_reply.split()

	    if initial_reply[0] == '0':
		print 'Creating new session'
		print 'initial_reply[2] ', initial_reply[2]
                ''' creating new session using function
                !!! do not use class creation !!!!
                '''
		sess = new_session(self.__client_address, int(initial_reply[2]))
                print "Session created with token ", sess

                self.__client_socket.send(sess)
                

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
