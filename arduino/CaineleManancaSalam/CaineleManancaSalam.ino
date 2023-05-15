#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

Servo servo;
int cereal_type = 0;
int pos = 0;

ISR(PCINT2_vect) {
  if (digitalRead(PD2) == HIGH) {
    if (cereal_type == 0) {
      // handle vanilla cereal
      servo.write(0);
    } else if (cereal_type == 1) {
      // handle cacao cereal
      servo.write(180);
    }
  }
}

void setup_interrupts() {
  cli();

  // set PD2 as output PIN
  pinMode(PD2, OUTPUT);
  // because PD2 is equivalent to PCINT18
  PCICR |= (1 << PCIE2);
  PCMSK2 |= (1 << PCINT18);

  sei();
}

void setup()
{
  setup_interrupts();
  Serial.begin(9600);
  Serial.setTimeout(1);
  servo.attach(9);
}

void loop()
{
  while(!Serial.available());
  cereal_type = Serial.readString().toInt();

  if (cereal_type == 0) {
    // vanilla cereal
    digitalWrite(PD2, HIGH);
    digitalWrite(PD2, LOW);
    delay(1000);
  } else if (cereal_type == 1) {
    // cacao cereal
    digitalWrite(PD2, HIGH);
    digitalWrite(PD2, LOW);
    delay(1000);
  } else {
    servo.write(90);
    // shaking state
    // for (pos = 75; pos <= 105; pos++) {
    //     servo.write(pos);
    //     delay(3);
    // }
    // for (pos = 105; pos >= 75; pos--) {
    //     servo.write(pos);
    //     delay(3);
    // }
    // for (pos = 75; pos <= 90; pos++) {
    //     servo.write(pos);
    //     delay(3);
    // }
    delay(100);
  }
}
