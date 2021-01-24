import socket


def handler(sock, name):
    sock.sendall(name)
    while True:
        msg = 1
        while msg == 1:
            message = input('Send to server > ').encode().strip()
            if message or message != b'':
                msg = 0
            else:
                print('Message was empty')

        if message.decode().lower() == 'slut':
            sock.sendall(message)
            sock.close()
            print('Connection closed')
            break

        send(sock, message)

        data = receive(sock)

        if data.lower() == 'slut':
            sock.close()
            print('Connection closed by host')
            break


def send(sock, message):
    try:
        sock.sendall(message)
    except Exception as e:
        print(e)
        return 'No message could be sent'


def receive(sock):
    try:
        data = sock.recv(4096)
    except socket.error as e:
        print(e)
        return 'Issue receiving data'

    print('Server > ', data.decode())
    return data.decode()


def connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 65432))
    return sock


def main():
    name = input('Set your client name: ')
    print(f'Server now know you as {name}')
    name = f'!#?{name}'.encode()
    handler(connection(), name)


if __name__ == '__main__':
    main()
