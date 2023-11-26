#include <Servo.h>
Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(9600);  // Make sure the baud rate matches the Python script
  servoX.attach(9);
  servoY.attach(10);
  }

void loop() {
  // Read data from the serial port
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int commaIndex = data.indexOf(',');

    // Parse X and Y coordinates
    int xCoordinate = data.substring(0, commaIndex).toInt();
    int yCoordinate = data.substring(commaIndex + 1).toInt();

    // Map coordinates to servo angles (assuming servoMin and servoMax are your servo limits)
    int xAngle = map(xCoordinate, -400, 400, 0, 180);
    int yAngle = map(yCoordinate, -400, 400, 0, 180);

    // Control your servos with xAngle and yAngle values
    servoX.write(xAngle);
    servoY.write(yAngle);
  }
}
