#include "Pantalla.h"

# define ANCHO_PANTALLA 128
# define ALTO_PANTALLA 64

void Pantalla::begin ()
{ 
  
display = new Adafruit_SSD1306(ANCHO_PANTALLA,ALTO_PANTALLA,&Wire);
display->begin(SSD1306_SWITCHCAPVCC,0x3C);// ALIMENTACION EXTERNA "SSD1306_EXTERNALVCC",0x3D para 128X64, 0X3C para 128x32
display->setTextColor(SSD1306_WHITE);

}
void Pantalla::limpieza(){//limpiar lo que se esta visulizando
   display->clearDisplay();
   
  }

void Pantalla::setTextSize(uint8_t size) {// tamaño de la letra
 if(size>3)
    size=3;
 if(size<1)
    size=1;
  display->setTextSize(size);// tamaño de la letra
}

void Pantalla::setCursor(uint8_t x, uint8_t y){ //donde se esta va a escribir 
   display->setCursor(x,y);
    }
  
size_t Pantalla::write(uint8_t c){// lo que se va a mostrar
   display->write(c);
return 1;
 }
  
void Pantalla::visualizar(){// imprimir
    display->display();
    }

int Pantalla::available(){}
int Pantalla::read(){}
int Pantalla::peek(){}
void Pantalla::flush(){}

