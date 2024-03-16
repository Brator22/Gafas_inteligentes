#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


class Pantalla: public Stream{

  public:
 virtual int available();
 virtual int read();
 virtual int peek();
 virtual void flush();
 void setTextSize(uint8_t);
 void setCursor(uint8_t, uint8_t);
 void visualizar();
 void limpieza();
 void begin();
 size_t write(uint8_t c);
  private:
   
   Adafruit_SSD1306 *display;  
   uint8_t sizeText;
  };
