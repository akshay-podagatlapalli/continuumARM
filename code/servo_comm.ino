#include <Servo.h>  // Importing the mighty Servo library, because motors need love too.

// Declaring our loyal servo subjects.
Servo servoX;  
Servo servoY;  

void setup() {
  Serial.begin(9600);  // Starting serial communication: the modern-day telegraph.
  servoX.attach(9);  // ServoX, you're now in charge of pin 9. Don't let the power go to your head.
  servoY.attach(10);  // ServoY, pin 10 is now your kingdom. Rule wisely.
}

void loop() {
  // Read data from the serial port, because listening is a virtue.
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // Reading incoming data until newline, like reading a suspense novel.
    int commaIndex = data.indexOf(',');  // Finding the comma, because every sentence needs a pause.

    // Parse X and Y coordinates - like treasure coordinates, but less pirate-y.
    int xCoordinate = data.substring(0, commaIndex).toInt();  // Extracting X coordinate, no treasure map needed.
    int yCoordinate = data.substring(commaIndex + 1).toInt();  // And here comes the Y coordinate, equally important.

    // Map coordinates to servo angles. Servos can't read maps, but they understand angles.
    int xAngle = map(xCoordinate, -400, 400, 0, 180);  // Translating X coordinates to servo language.
    int yAngle = map(yCoordinate, -400, 400, 0, 180);  // Same for Y. It's all about equality.

    // Control your servos with xAngle and yAngle values, like a puppet master.
    servoX.write(xAngle);  // ServoX, turn to xAngle, and do it gracefully.
    servoY.write(yAngle);  // ServoY, follow suit. Keep up with your partner.
  }
  // This loop goes on and on, like a carousel, but with more servos and less horses.
}
