from flask import Flask, request
from flask import render_template

import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 65431))
s.listen()

client = None

def wait_for_client():
    global client
    client, address = s.accept()
    print('Client connected')

t1 = Thread(target=wait_for_client)
t1.start()



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.post('/update_esp')
def ESP32Foto():
     if client is not None:
        client.send(b'imagen')
        data = ''
        size = client.recv(5)
        size = int.from_bytes(size, 'big')
        print(size) 
        while True:
            esp = client.recv(65536)
            data += esp.decode()
            size -= len(esp)
            if size <= 0:
                break

        data = 'data:image/jpeg;base64,' + data

        return {'response': data}
     else:
         return{'response': '', 'error': 'client not connected'}




if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0')


