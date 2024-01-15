const int ledPin = 2;  // Pin connected to the LED

void setup() {
  Serial.begin(9600);  // Set the baud rate to match the one used in Python code
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Check if data is available to read from the Serial port
  while (Serial.available() > 0) {
    // Read the incoming data
    int numFingers = Serial.parseInt();

    // Control the LED based on the number of fingers
    if (numFingers == 0) {
      digitalWrite(ledPin, LOW);  // Turn off the LED when no finger is shown
    } else {
      // Blink the LED the corresponding number of times
      for (int i = 0; i < numFingers; i++) {
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
      }
    }
  }
}
