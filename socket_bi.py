import network
import _thread
import config
import socket
from time import sleep


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("wifi connected")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.43.159', 65432))

def one():
    while True:
        s.send(b'hello')
        sleep(5)


_thread.start_new_thread(one, ())


while True:
    data = s.recv(1024)
    print(data)

    