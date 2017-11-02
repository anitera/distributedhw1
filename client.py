from socket import AF_INET, SOCK_STREAM, socket
from argparse import ArgumentParser

buffer_length = 1024

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n','--nickname',\
                        help='nickname validation',\
                        required=True
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
    s.close()
