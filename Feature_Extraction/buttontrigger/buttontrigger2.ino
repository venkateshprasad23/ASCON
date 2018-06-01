#include<avr/io.h>
//int analogPin = 14;     // potentiometer wiper (middle terminal) connected to analog pin 3

                       // outside leads to ground and +5V

int val=0;           // variable to store the value read
int pushButton = 2;
void setup()

{
  Serial.begin(9600);          //  setup serial
  pinMode(pushButton, INPUT);
  DDRD&=0x00;
}

void loop()

{
  int buttonState = digitalRead(pushButton);
  if ( buttonState == 1)
  {
    for(int i=14;i<19;i++)
    {
      val = analogRead(i);    // read the input pin
      delay(10);
      Serial.print(val);
      Serial.print(" ");
    }
    Serial.print("\n");
  } 
  
  delay(10);
}
