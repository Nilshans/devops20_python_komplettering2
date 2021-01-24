import socket
import json
import random


class HandleName:

    def __init__(self):
        self.visitors = {}

    def selName(self, addr):
        return self.visitors[addr]

    def setName(self, addr, aname):
        self.visitors[addr] = aname

    def writeFile(self):

        with open('visitors.json', 'w') as f:
            json.dump(self.visitors, f)

    def readFile(self):

        with open('visitors.json', 'r') as f:
            data = json.load(f)
        return data


class Response:

    def __init__(self, conn, addr):
        self.rain = True
        self.luck_num = 0
        self.conn = conn
        self.addr = addr

    def getRain(self):
        rand_bit = random.getrandbits(1)
        self.rain = bool(rand_bit)
        if self.rain == True:
            message = 'There will be rain tomorrow'
        else:
            self.rain = False
            message = 'You wont need an umbrella tomorrow'
        return message

    def getLuckyNum(self):
        self.lucky_num = random.randint(1, 100)
        return str(self.lucky_num)

    def setMessage(self):
        new_name = HandleName()
        new_name.__init__()
        while True:
            command = receive(self.conn)
            if command == "slut":
                print('Connection Closed')
                new_name.writeFile()
                break

            if command.startswith('!#?'):
                new_name.setName(self.addr, command[3:])
                print(f'Name set to: {new_name.selName(self.addr)}')

            if command == 'regn':
                msg = self.getRain()

            elif command == 'turnummer':
                msg = self.getLuckyNum()

            elif command == 'hej medium':
                msg = f'hej {new_name.selName(self.addr)}'

            elif command == 'whoami':
                msg = new_name.selName(self.addr)

            elif command == 'hjälp':
                msg = '"hej medium", "regn", "whoami", "turnummer", "hjälp", "slut"'

            else:
                msg = 'Command invalid. Type "hjälp" for options'

            if not command.startswith('!#?'):
                send(self.conn, msg)


def send(conn, msg):
    try:
        conn.sendall(msg.encode())
    except Exception as e:
        print('Message not sent')
        print(e)


def receive(conn):
    try:
        message = conn.recv(4096).decode().lower()
        print('Data received: ', message)
    except socket.error as e:
        print(e)
        return 'Cannot receive data'
    return message


def connection():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 65432))
    sock.listen()
    return sock


def handler(sock):
    while True:
        conn, addr = sock.accept()
        print(f'Connection from: {addr[0]}')

        response = Response(conn, addr[0])
        response.setMessage()
        conn.close()


def main():
    print('Välkommen till ditt medium')
    handler(connection())


if __name__ == '__main__':
    main()
