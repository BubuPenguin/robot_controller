#define enA 7
#define in1 6
#define in2 5
#define in3 4
#define in4 3
#define enB 2

int SPEED = 210;

void setup() {
  // Initialize motor control pins as outputs
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enB, OUTPUT);

  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
}

void loop() {
  analogWrite (enA, SPEED);
  analogWrite (enB, SPEED);

  if (Serial.available() > 0) {
    char command = Serial.read();

    // Move forward
    if (command == 'W') {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
    }

    // Move backward
    else if (command == 'S') {
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH);
    }

    // Turn left
    else if (command == 'A') {
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
    }

    // Turn right
    else if (command == 'D') {
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH);
    }

    // Stop
    else if (command == ' ') {
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
    }
  }
}

