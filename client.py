from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser
import curses
import os
buffer_length = 1024

nicknames = []

def validate_nickname(nickname):
    if len(nickname) == 0 or ' ' in nickname or len(nickname) > 8:
        return False
    else:
        return True

if __name__ == '__main__':
    '''
    parser = ArgumentParser()
    parser.add_argument('-n','--nickname',\
                        help='nickname validation',\
                        required=False
                        )
    parser.add_argument('-p','--port',\
                        help='port',\
                        default=7777,\
                        required=False
                        )
    parser.add_argument('-H','--Host',\
                        help='host',\
                        required=False,\
                        default='127.0.0.1')
    args = parser.parse_args()
    '''

    if os.path.exists("client.ini"):
        with open("client.ini", "r+") as cli:
            for id, nick in enumerate(cli.readlines()):
                nicknames.append(nick)
                print id, nick
    nick = ""
    if len(nicknames) > 0:
        while True:
            id = raw_input("Choose id: ")
            id = int(id)
            if id >= 0 and id < len(nicknames):
                nick = nicknames[id]
                break
    else:
        while True:
            nick = raw_input("Enter nickname: ")
            if validate_nickname(nick):
                if nick not in nicknames:
                    nicknames.append(nick)
                else:
                    print "already exist!"
                break
                

        with open("client.ini", "w") as cli:
            for nick in nicknames:
                cli.write(nick+'\n')

    print "Your nickname: ", nick
    
    s = socket(AF_INET, SOCK_STREAM)

    while True:
        inpt = raw_input("Enter dedicated host address [ip:port]: ")
        host, port = inpt.split(":")
        port = int(port)

        if s.connect_ex( (host, port) ) != 0:
            print "Incorrect host address. Try again!"

        else:
            print "Connection established!"
            break
    
    print "Multiplayer Game"
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
