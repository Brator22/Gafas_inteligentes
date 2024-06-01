from time import sleep
import threading
import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6543))
s.listen()

client, address = s.accept()
print('Client connected')

def one():
    while True:
        try:

            #data = client.recv(1024)
            #print(data)
            client.send(b'RECIBIDO')
            sleep(3)

        except KeyboardInterrupt:
            break

class two(Thread):
    def run(self):
        while True:
            try:
                data = client.recv(1024)
                print(data)
                #client.send(b'ON')

            except KeyboardInterrupt:
                break

t1 = threading.Thread(target=one)
t2 = two()

t1.start()
t2.start()