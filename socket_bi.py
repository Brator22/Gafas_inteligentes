import network
import _thread
import config
import socket
from time import sleep
import camera
import ubinascii

#data = 0
s = None


def initCamera():
    camera.init(0, format=camera.JPEG)
    #Establece el brillo
    camera.brightness(-1)
    #Orientacion normal
    camera.flip(0)
    #Orientación normal
    camera.mirror (0)
    #Resolución
    camera.framesize(camera.FRAME_QVGA)
    #contraste
    camera.contrast(2)
    #saturacion
    camera.saturation (-2)
    #calidad
    camera.quality(20)
    # special effects
    camera.speffect(camera.EFFECT_NONE)
    # white balance
    camera.whitebalance(camera.WB_NONE)
    
def takePhoto():
    #Captura la imagen
    img = camera.capture()
    
   # Codifica la imagen en Base64
    base64_img = ubinascii.b2a_base64(img).decode().strip()
    print ("Tamaño=",len(base64_img))
    
    return base64_img

def configNetwork():
    global s
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("wifi connected")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.43.159', 65432))

if __name__ == "__main__":
    
     
    initCamera()
    configNetwork()

    while True:
        
        data = s.recv(1024)
        print(data)
        if data == b'imagen':
                   
            Foto = takePhoto()
            tamano = len(Foto)
            s.send(tamano.to_bytes(5, 'big'))
            sleep(0.1)
            s.sendall(Foto)