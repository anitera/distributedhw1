
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
