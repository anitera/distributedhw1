from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser

# Constants
buffer_length = 1024

def validate_nickname(nickname):
    if len(nickname) == 0 or ' ' in nickname or len(nickname) > 8:
        return False
    else:
        return True

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-H','--Host',\
                        help='host',\
                        required=False,\
                        default='127.0.0.1')
    parser.add_argument('-p','--port',\
                        help='port',\
                        required=False,\
                        default=7777)
    args = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((args.Host, args.port))

    backlog = 0 # Waiting queue size, 0 means no queue
    s.listen(backlog)

    while True:
            try:
	        client_socket,client_addr = s.accept()
            except socket.error, exc:
                print 'Caught socket exceptopn', exc
            try:
	        nickname = client_socket.recv(buffer_length)
            except socket.error:
                print 'Socket error'
            if validate_nickname(nickname):
                client_socket.send('1')
            else:
                client_socket.send('0')
	    client_socket.close()
    s.close()
