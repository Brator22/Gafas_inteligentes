from machine import Pin, Timer
from time import sleep, ticks_ms
from menu import Menu
from machine import Pin, I2C
import ssd1306
import socket_bi
import _thread
import usocket as socket
import urequests

sock = socket_bi
sock.PararCamara()


# URL de la API
host = "https://timeapi.io"
path = "/api/Time/current/zone?timeZone=America/New_York"
path1 ="/api/Time/current/zone?timeZone=America/Bogota"


# ESP32 Pin assignment 
i2c = I2C(0, scl=Pin(14), sda=Pin(15))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# upp
boton1=Pin(2,Pin.IN,Pin.PULL_UP)
#down
boton2=Pin(12,Pin.IN,Pin.PULL_UP)
#enter
boton3=Pin(13,Pin.IN,Pin.PULL_UP)

sock.configNetwork()
sock.initCamera()

Inicio = 0
last_time = 0
opcion = 0
Hora = 0
Minutos = 0
Segundos = 0
bandera = 0
datetime = ''


tim0 = Timer(0)



def option0():
    global Inicio, Minutos, Segundos, opcion, datetime
    response = urequests.get(host+path)
    datetime = response.json()['time']
    date = response.json()['date']
    limpiar_pantalla()
    oled.text("New York", 10, 10)
    oled.text("Hora :",datetime, 10, 20)
    oled.text("Fecha: ",date, 10, 30)
    print(datetime)
    
    response = urequests.get(host+path1)
    datetime1= response.json()['time']
    date1 = response.json()['date']
    oled.text("Bogota DC", 10, 10)
    oled.text("Hora :",datetime1, 10, 20)
    oled.text("Fecha: ",date, 10, 30)
    
    opcion = 1
    Inicio = 0


def option1():
    
     

def option2():
    global Inicio, opcion
    limpiar_pantalla()
    oled.text("Di una ", 10, 10)
    oled.text("pregunta ", 10, 20)
            
    if Inicio == 1:
        sock.s.send('audio')
        opcion = 3
    if Inicio == 2:
        Inicio = 0



def changeLed1(t):
    global Hora, Minutos, Segundos, Inicio

    Segundos += 1
    if Segundos == 60:
        Minutos += 1
        Segundos = 0
    if Minutos == 60:
        Minutos == 0
        Segundos = 0

    if Segundos < 10 & Minutos < 9:
        Hora = "0" + str (Minutos) + ":" + "0" + str (Segundos)
    elif Segundos >= 10 & Minutos < 9:
        Hora = "0" + str (Minutos) + ":" + str (Segundos)
    else:
        Hora = str (Minutos) + ":" + str (Segundos)
    
def changeLed2(t):
    global Hora, Minutos, Segundos, Inicio

    Segundos += 1
    if Segundos == 60:
        Minutos += 1
        Segundos = 0
    if Minutos == 60:
        Minutos == 0
        Segundos = 0

    if Segundos < 10 & Minutos < 9:
        Hora = "0" + str (Minutos) + ":" + "0" + str (Segundos)
    elif Segundos >= 10 & Minutos < 9:
        Hora = "0" + str (Minutos) + ":" + str (Segundos)
    else:
        Hora = str (Minutos) + ":" + str (Segundos)

def changeLed3(t):
    global Hora, Segundos, bandera
    Segundos = 0
    bandera = 1
    Hora = "U Quindio"
    

menu = Menu(oled.print)

menu.addItem("Hora Colombia",option0)
menu.addItem("Hora Tokio",option1)
menu.addItem("chatgpt",option2)

def upp(pin):
    global last_time, Inicio
    if ticks_ms() - last_time > 500:
        if Inicio == 0:
            limpiar_pantalla()
            menu.up()
        last_time = ticks_ms()
        
def downn(pin):
    global last_time, Inicio
    if ticks_ms() - last_time > 500:
        if Inicio == 0:
            limpiar_pantalla()
            menu.down()
        last_time = ticks_ms()
        #limpiar_pantalla()

def enterr(pin):
    global last_time, Inicio
    if ticks_ms() - last_time > 500:
        Inicio += 1
        print(Inicio)
        menu.enter()        
        last_time = ticks_ms()
        

def limpiar_pantalla():
  oled.fill(0)  # Llena la pantalla de negro 
  oled.show()   # Actualiza la pantalla
  
def one():
    try:
        while True:        
            data = sock.s.recv(1024)
            print(data)
            if data == b'foto':
                print("FOTO ENVIADA")
                Foto = sock.takePhoto()
                size = len(Foto)
                sock.s.send(size.to_bytes(5, 'big'))
                sleep(0.1)
                sock.s.sendall(Foto)
    except:
        sock.PararCamara()

boton1.irq(upp, Pin.IRQ_FALLING)

boton2.irq(downn, Pin.IRQ_FALLING)

boton3.irq(enterr, Pin.IRQ_FALLING)

_thread.start_new_thread(one, ())

one = True

if _name_ == "_main_":
    while True:

        if one == True:
            oled.text("WELCOME..", 10, 10)
            oled.text("ENTER", 0, 25)
            oled.text("SUBIR", 0, 35)
            oled.text("BAJAR", 0, 45)
            one = False

        '''
        if opcion == 1:
            limpiar_pantalla()
            oled.text("Colombia ", 10, 10)
            oled.text(datetime, 10, 20)
            print("opcion 0")
            opcion = 0
        elif opcion == 2:
            limpiar_pantalla()
            oled.text("Tokio ", 10, 10)
            oled.text(datetime, 10, 20)
            print("opcion 1")
            opcion = 0
        elif opcion == 3:
            limpiar_pantalla()
            oled.text("Di una ", 10, 10)
            oled.text("pregunta ", 10, 20)
            print("opcion 2")
            opcion = 0
        '''

        if Segundos != bandera:
            limpiar_pantalla()
            oled.text(str(Hora), 10, 50)       
            bandera = Segundos
        oled.show()
        sleep(1)
               
