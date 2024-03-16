#include "menu.h"
#include "Pantalla.h"

#define LED0 2
//#define LED1 18
//#define LED2 15
volatile int conteo;
volatile int bandera=0;

hw_timer_t *timer=NULL;// puntero

Menu menu; //donde se quiere imprimir, tiene que ser de la clase Stream
Pantalla pantalla;

volatile unsigned long lastTime=0;
volatile boolean bUp, bDown, bEnter = false; 
volatile boolean Boption0, Boption1, Boption2 = true;
volatile boolean desconteo=100;

void setup() {


  Serial.begin(115200);
  menu.begin(pantalla);
  pantalla.begin();

  menu.addItem("option 0",option0);
  menu.addItem("option 1",option1);
  menu.addItem("option 2",option2);

  timer=timerBegin(0,80,true);//timer 0, division de reloj 80
timerAttachInterrupt(timer,&timerInterrupcion,true);
timerAlarmWrite(timer,1000000,true);//interrupcion cada 1 segundo 
timerAlarmEnable(timer); // habilitar la alarma

// declaramos pines de los led
  pinMode (LED0,OUTPUT);
  //pinMode (LED1,OUTPUT);
  //pinMode (LED2,OUTPUT);
  
//declaramos los pines pulsadores
  pinMode (12,INPUT_PULLUP);
  pinMode (14,INPUT_PULLUP);
  pinMode (27,INPUT_PULLUP);
  
// pull up
  attachInterrupt(14,enter,FALLING);// enter
  attachInterrupt(27,up,FALLING);//bajar 
  attachInterrupt(12,down,FALLING);//subir
  
  bUp = bDown = bEnter = false;

  timer=timerBegin(0,80,true);// timer,preescalar

timerAttachInterrupt(timer,timerInterrupcion, true);
timerAlarmWrite(timer,1000000,true);
timerAlarmEnable(timer);

timerStop (timer);
timerRestart(timer);


pantalla.setTextSize(2);
pantalla.limpieza();
}

void loop() {

if(bUp==true){

  menu.up();
  bUp=false; 
  }
  if(bDown==true){
    
  menu.down();
  bDown=false; 
  }
  if(bEnter==true){
  menu.enter();
  bEnter=false; 
  }


pantalla.visualizar();

}
void ARDUINO_ISR_ATTR timerInterrupcion() 
{
    if(bandera==0)
    conteo++;
    else{
    conteo=0;
    timerRestart(timer);
    }
  }

void ARDUINO_ISR_ATTR enter() // anti-rebote
{
  if ( (millis()-lastTime)>200){
   bEnter= true;
   lastTime=millis();
  }
}

void ARDUINO_ISR_ATTR up() // anti-rebote
{
  if ( (millis()-lastTime)>200){
   bUp= true;
   lastTime=millis();
  }
}

void ARDUINO_ISR_ATTR down() // anti-rebote
{
  if ( (millis()-lastTime)>200){
   bDown= true;
   lastTime=millis();
  }
}

void option0 ()
{
  if(bandera==0){
     bandera=1;
     timerRestart(timer);
     pantalla.limpieza();
     pantalla.setTextSize(3);
     pantalla.setCursor(64,32);
     pantalla.write(conteo);
     pantalla.visualizar();
     bandera=0;
  }

}

void option1 ()
{
 
  if(bandera==0){
    bandera=1;
    timerRestart(timer);
    digitalWrite(LED0,!digitalRead(LED0));
    bandera=0;
  }
}

void option2 ()
{
  if( bandera==0){
     desconteo=100;
     bandera=1;
     pantalla.limpieza();
     timerRestart(timer);
     desconteo=desconteo-conteo;
     pantalla.setTextSize(3);
     pantalla.setCursor(64,32);
     pantalla.write(desconteo);
     pantalla.visualizar();
     bandera=0;
  }
}



  



 
