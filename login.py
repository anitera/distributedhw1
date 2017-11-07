import os

nicknames =[]

def validate_nickname(nickname):
    if len(nickname) == 0 or ' ' in nickname or len(nickname) > 8:
        return False
    else:
        return True
def show_nicknames():
    for id, nick in enumerate(nicknames):
        print id, nick

def load_nicknames(): 
    if os.path.exists("client.ini"):
        with open("client.ini", "r+") as cli:
            for id, nick in enumerate(cli.readlines()):
                nick = nick[:-1]
                nicknames.append(nick)
        
        show_nicknames()

    if len(nicknames) > 0:
       return True
    else:
        return False

def enter_nickname():
    while True:
        nick = raw_input("Enter nickname: ")
        nick = nick
        if validate_nickname(nick):
            if nick not in nicknames:
                nicknames.append(nick)
                with open("client.ini", "w") as cli:
                    for nick in nicknames:
                        cli.write(nick+'\n')
                return nick
            else:
                print "already exist!"
                show_nicknames()
        else:
            print "Doesnt match requirements"

def load_nickname():
    while True:
        id = raw_input("Choose id: ")
        try:
            id = int(id)
        except:
            print "Not digit!"
            continue
        if id >= 0 and id < len(nicknames):
            return nicknames[id]
        else:
            print "wrong id!"
            show_nicknames()



