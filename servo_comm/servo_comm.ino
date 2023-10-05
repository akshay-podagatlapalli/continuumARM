#include<Servo.h>
Servo s1;
Servo s2;

int pos = 0; // inital servo position 

void setup() {
  s1.attach(9); // attaches the servo to pin 9
  Serial.begin(9600); // setup serial communication
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int coordX = data.substring(0, data.indexOf(',')).toInt();

    // Map the x-coordinate value to servo position
    pos = map(coordX, -0.4, 0.4, 0, 180);

    // Move the servo
    s1.write(pos);
  }  
}