import socket
import os
from faker import Faker

fake=Faker('ja_JP')

sock=socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address='udp_faker_socket'

try:
	os.unlink(server_address)
except FileNotFoundError:
	pass

print('starting up on {}'.format(server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, client_address = sock.recvfrom(4096)

    if not data:
        continue

    text = data.decode('utf-8').strip()
    print(f'received "{text}" from {client_address}')

    if text == 'quit':
        print('quit command received, shutting down server')
        break

    if text == 'name':
        reply = fake.name()
    elif text == 'address':
        reply = fake.address()
    elif text == 'email':
        reply = fake.email()
    else:
        reply = fake.sentence()

    print('sending back:', reply)
    sock.sendto(reply.encode('utf-8'), client_address)

sock.close()
os.unlink(server_address)
print('server closed')
