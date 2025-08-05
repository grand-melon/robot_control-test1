#include <Servo.h>

Servo servo;

int motor = 2; //32
int angle = 90;

void setup() {
  // put your setup code here, to run once:
  servo.attach(motor);
  Serial.begin(9600);

  Serial.println("Enter the u or d");
  Serial.println("u = angle + 15");
  Serial.println("d = angle - 15\n");

}

void loop() {
  // put your main code here, to run repeatedly:

  if(Serial.available())
  {
    char input = Serial.read();

    if(input == 'u')
    {
      Serial.print("+15");
      for(int i=0;i<15;i++){
        angle = angle + 1;
        if(angle >=180){angle = 180;}
        servo.write(angle);
        delay(10);
      }
      Serial.print("\t\t");
      Serial.println(angle);
    }
    else if(input == 'd')
    {
      Serial.print("\t-15\t");
      for(int i=0;i<15;i++){
        angle = angle - 1;
        if(angle <=0){angle = 0;}
        servo.write(angle);
        delay(10);
      }
      Serial.print("\t\t");
      Serial.println(angle);
    }
    else{
      Serial.println("wrong character");
    }

  }

}
