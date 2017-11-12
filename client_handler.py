from threading import Thread
from protocol import *
from socket import error as soc_err
from sessions import new_session, get_session
import time
import pickle

class ClientHandler(Thread):
    def __init__(self, client_socket, client_addr): #need to take as argument game_session_id
        Thread.__init__(self)
        self.__client_socket = client_socket
        self.__client_address = client_addr
        self.buffer_size = 1024
        self.sess_names = []
       # self.cv_sess = None
	#self.game_session_id = game_session_id

    def set_sessions(self, sess_names):
        for id, name in enumerate(sess_names):
            self.sess_names.append( (id,name ) )

    def run(self):
        self.__handle()


    def __handle(self):
        sess_token = None
        try:
            print "Client connected from %s:%d" % (self.__client_address)
            self.__client_socket.send(pickle.dumps(self.sess_names, -1))
                #self.__client_socket.send(DELIM.join([ x for x in self.sess_names]))
            

                
            initial_reply = self.__client_socket.recv(self.buffer_size) 
	    print initial_reply

            initial_reply = initial_reply.split(DELIM)
            nick = "" 
	    
            print initial_reply

            if initial_reply[0] == NEW_SESSION:
		nick = initial_reply[3]
                print 'Creating new session'
		print 'initial_reply[2] ', initial_reply[2]
                ''' creating new session using function
                !!! do not use class creation !!!!
                '''
		sess = new_session(self.__client_address, int(initial_reply[2]), initial_reply[1])
                #print "ebu4iy token ", t
               # self.cv_sess.notify()
                print "Session ", sess.get_name(), " created with token ", sess.get_token()
                
                
                sess.add_player(nick, self.__client_socket)
                
                #self.__client_socket.send(sess.get_token())
                
                #sess.add_player(nick, self.__client_socket)
                #self.__client_socket.send(sess.get_token())
                #self.cv_sess.notify()
                #save_session(self.cv_sess) 
            if initial_reply[0] == OLD_SESSION:
                name = initial_reply[1]
                print "find session by name ", name
                sess = get_session(name) #get_session(initilal_reply[1])
                nick = initial_reply[2]
                print "Player ", nick, " connected to session ", sess.get_token()
                sess.add_player(nick, self.__client_socket)
                
                #self.__client_socket.send(sess.get_token())
            
	    # if he created new session 0 - sess = Game_Session()

            # call function gamesession to add client name first time game_session new_player_in_current_session
            #print "Client's nickname=", nick
            self.__client_socket.send(sess.get_token())
            #print "send token ", sess_token
            #self.__client_socket.send(sess_token)
            while True:
                print "awaiting data"

                resp = self.__client_socket.recv(self.buffer_size)

                if resp == DISCONNECT:
                    break
                #receive answer from client: (i,j) 8
		#game_session solver(name, client_answer) - there check if it solved if yes return message
                time.sleep(10)
		#send table_score to client and/or message

        except soc_err as e:
            if e.errno == 107:
                print "Client left befor handle"
            else:
                print "error %s" % str(e)
        except:
            self.__client_socket.close()
        finally:
            self.__client_socket.close()
        if not sess == None:
            sess.remove_player(nick, self.__client_socket)
        print "client disconected"
