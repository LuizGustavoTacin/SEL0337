#include <Wire.h>

const int ledPin =  LED_BUILTIN;
int pot = 0;
byte buf[2];

void setup(){

  Serial.begin(9600);
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,LOW);
}
  void receiveEvent(int number){
    while (Wire.available()){
      char c = Wire.read();
      digitalWrite(ledPin,c);
    }
  }
  void requestEvent(){
    Serial.println(F("Valor recebido: "));
    Serial.print(F("Valor enviado: "));
    pot = analogRead(A0);
    Serial.println(pot);
    Wire.write(highByte(pot));
    Wire.write(lowByte(pot));
  }
void loop(){
  delay(100);
}
