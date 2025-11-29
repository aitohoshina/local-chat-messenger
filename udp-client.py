import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = 'udp_faker_socket'
client_address = 'udp_faker_client'

try:
    os.unlink(client_address)
except FileNotFoundError:
    pass

sock.bind(client_address)

try:
    while True:
        msg = input('command (name/address/email/other, quitで終了): ')
        if msg == '':
            continue

        sock.sendto(msg.encode('utf-8'), server_address)

        if msg == 'quit':
            print('bye')
            break

        data, _ = sock.recvfrom(4096)
        print('SERVER:', data.decode('utf-8'))

finally:
    sock.close()
    os.unlink(client_address)
