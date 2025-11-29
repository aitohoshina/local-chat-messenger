import socket

server_address = '/tmp/socket_file'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

print('Connecting to', server_address)
sock.connect(server_address)

try:
    while True:
        message = input('You: ')
        if message == '':
            break

        sock.sendall(message.encode())

        data = sock.recv(1024)
        if not data:
            print('Server closed connection')
            break

        print('Server:', data.decode('utf-8'))

finally:
    print('Closing socket')
    sock.close()
