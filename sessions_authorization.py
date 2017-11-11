import os
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
	
try:
    import tkMessageBox as tkBox
except ImportError:
    from tkinter import messagebox as tkBox
#from sessions import *

sessions_list = []
sessions_list_size = []

class Session_Authorization:
    def __init__(self):
        self.session_id = 0
        self.session_size = 4
    
    def setSession_id_size(self, session_id, session_size):
        self.session_id = session_id
	self.session_size = session_size

    def setSession_size(self, session_size):
        self.session_id = session_id
	self.session_size = session_size
        
    def getSession_id(self):
        return self.session_id

    def getSession_size(self):
        return self.session_size

# def sendPortHost(hostport_entry, window, hp):
#     hostport_data = hostport_entry.get().split(":")
#     if len(hostport_data) == 2 and hostport_data[1].isdigit():
#         tkBox.showinfo("Checking host and port", "Please, wait...")
#         hp.setHostPort(hostport_data)
#         window.destroy()
#     else:
#         tkBox.showinfo("Checking host and port", "Incorrect format of host:port")
#         window.destroy()


def send_data_sessions(listbox, sessions , window, sess): 
    current = listbox.curselection()
    if current:
        print 'Decide to join existing session'
        sessionsize = listbox.get(current[0])
        print("Session size is...", sessionsize)
	#return session_id
    else:
        sessionname = sessions.get()
        print("Connecting to...", sessionname)
	#return session_size
    if validate_session_size(sessionname):
        sess.passed = True
        sess.setNickname(sessionname)
        print("Welcome,", sessionname)
        tkBox.showinfo("Connected!", "Have fun!")
        window.destroy()
    else:
        print("CAN NOT CONNECT TO SESSION")
        tkBox.showinfo("Session already booked", "try another session")
        sessions.delete(0, len(sessionname))
        sessions.insert(0, "")


def validate_session_size(session_size):
    if len(session_size) == 0 or ' ' in nickname or len(session_size) > 2 or isinstance( session_size, ( int, long ) ):
        return False
    else:
        return True

    
def sessionsAuthorization(sessions, sess):
    window = tk.Tk()

    listbox_label_location_x = 10
    listbox_label_location_y = 10
    listbox_label_x = 10
    listbox_label_y = 30

    session_label_x = 200
    session_label_y = 30
    session_x = 200
    session_y = 60

    number_label_x = 200
    number_label_y = 35
    number_x = 200
    number_y = 40

    button_x = 200
    button_y = 150
    button_height = 3
    button_width = 15

    window.geometry('370x250')
    window.resizable(width=True, height=True)
    window.title('Authorization')
    listbox_text = tk.Label(text = "Join exesting session")
    listbox_text.place(x = listbox_label_location_x, y = listbox_label_location_y)
    listbox = tk.Listbox(window)

    sessions_counter = 0
    sessions_list = sorted(sessions_list) # Not neccessary
    for sessions in set(sessions_list):
        listbox.insert(sessions_counter, sessions)
        sessions_counter += 1
    listbox.place(x=listbox_label_x, y=listbox_label_y)
    session_text = tk.Label(text="Create new one. \n Enter session name:")
    session_text.place(x=session_label_x, y = session_label_y)

    session = tk.Entry()
    session.place(x=session_x, y=session_y)
    
    number_of_players = tk.Entry()
    number_of_players.place(x=number_x, y=number_y)

    a = tk.Button(window, text="Pick session", command=lambda: send_data_sessions(listbox, session, window, sess))
    a.config(height = button_height, width = button_width)
    a.place(x=button_x, y=button_y)
    window.mainloop()

def show_sessions():
    for id, sess in enumerate(sessions_list):
        print id, sess

def load_sessions(sessions_list, sessions_size): 
    content = (sessions_list, sessions_size)
    print content
        show_sessions()

    if len(sessions_list) > 0:
        for id, sess in enumerate(sessions_list):
        print id, sess
        return True
    else:
	print 'There are no sessions yet, please create new'
        return False

def sessionStart(sessions, load=True):
    #session_chosen = Session_Authorization()
    print 'session_chosen', sessions
    if load:
        load_sessions()
    sessionsAuthorization(sessions_list, sessions)
    return session_chosen.getSessionId()

