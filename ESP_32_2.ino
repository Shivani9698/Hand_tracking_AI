const int ledPins[] = {2, 4, 5, 12, 13};  // Pins connected to the LEDs
const int numLeds = sizeof(ledPins) / sizeof(ledPins[0]);

void setup() {
  Serial.begin(9600);  // Set the baud rate to match the one used in Python code

  // Set the LED pins as OUTPUT
  for (int i = 0; i < numLeds; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  // Check if data is available to read from the Serial port
  while (Serial.available() > 0) {
    // Read the incoming data
    int numFingers = Serial.parseInt();

    // Control the LEDs based on the number of fingers
    for (int i = 0; i < numLeds; i++) {
      // Turn on/off each LED based on the number of fingers
      digitalWrite(ledPins[i], i < numFingers ? HIGH : LOW);
    }
  }
}
