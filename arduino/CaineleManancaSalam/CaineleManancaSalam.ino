#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

// Set the LCD address to 0x27 for a 16 chars and 2 line display
Servo servo;
int pos = 0;
int a;
int state = 0;

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(1);
  servo.attach(9);
  // servo.write(0);
  // delay(1000);
  // servo.write(45);
  // delay(1000);
  // servo.write(90);
  // delay(1000);
  // servo.write(135);
  // delay(1000);
  // servo.write(180);
  // delay(1000);
  // servo.write(90);
}

void loop()
{
  while(!Serial.available());
  a = Serial.readString().toInt();

  if (a == 0) {
    servo.write(0);
    delay(3);
  } else {
    servo.write(180);
    delay(3);
  }

	// for (pos = 75; pos <= 105; pos++) {
  //   servo.write(pos);
  //   delay(3);
  // }
  // for (pos = 105; pos >= 75; pos--) {
  //   servo.write(pos);
  //   delay(3);
  // }
}
