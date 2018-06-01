void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  char x,y;
  if(Serial.available()>0)
     x=Serial.read();
  if(x==97){
  while(1)
  {
     Serial.print(analogRead(A0));
     Serial.print(" ");
     Serial.print(analogRead(A1));
     Serial.print(" ");
     Serial.print(analogRead(A2));
     Serial.print(" ");
     Serial.print(analogRead(A3));
     Serial.print(" ");
     Serial.print(analogRead(A4)); 
     Serial.print("\n");
     if(Serial.available()>0)
        y=Serial.read();
     if(y==98)
     {
        for(int i=1;i<=7;i++)
          Serial.print("\n");
        break;
     }
  }
}
}
