#include <Wire.h>

const int MAX_LEVEL = 100;
int sequence[MAX_LEVEL];
int your_sequence[MAX_LEVEL];
int level = 1;
int velocity = 1000;

bool myTurn = false;
bool myReady = false;
bool gameOver = false;

void setup() {
  Wire.begin(8);
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);

  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}

void loop() {
  if (gameOver)
    return;

  if (!myTurn)
    return;

  if (level == 1)
    generate_sequence();

  show_sequence();
  get_sequence();
}

void generate_sequence() {
  randomSeed(millis());
  for (int i = 0; i < MAX_LEVEL; i++) {
    sequence[i] = random(2, 6);
  }
}

void show_sequence() {
  for (int i = 0; i < level; i++) {
    digitalWrite(sequence[i], HIGH);
    delay(velocity);
    digitalWrite(sequence[i], LOW);
    delay(200);
  }
}

void get_sequence() {
  int flag = 0;
  for (int i = 0; i < level; i++) {
    flag = 0;
    while (flag == 0) {
      if (digitalRead(A0) == LOW) {
        digitalWrite(5, HIGH);
        your_sequence[i] = 5;
        flag = 1;
        delay(200);
        if (your_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(5, LOW);
      }
      if (digitalRead(A1) == LOW) {
        digitalWrite(4, HIGH);
        your_sequence[i] = 4;
        flag = 1;
        delay(200);
        if (your_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(4, LOW);
      }
      if (digitalRead(A2) == LOW) {
        digitalWrite(3, HIGH);
        your_sequence[i] = 3;
        flag = 1;
        delay(200);
        if (your_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(3, LOW);
      }
      if (digitalRead(A3) == LOW) {
        digitalWrite(2, HIGH);
        your_sequence[i] = 2;
        flag = 1;
        delay(200);
        if (your_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(2, LOW);
      }
    }
  }
  right_sequence();
}

void wrong_sequence() {
  blink_all_leds();
  gameOver = true;
}

void right_sequence() {
  blink_all_leds();
  if (level < MAX_LEVEL)
    level++;
  velocity -= 50;

  myReady = true; 
  myTurn = false;
}

void receiveEvent(int howMany) {
  int x = Wire.read();
  if (x == 1) {
    digitalWrite(2, HIGH);
    delay(300);
    digitalWrite(2, LOW);
    myTurn = true;
    level = 1;
    velocity = 1000;
  }
}

void requestEvent() {
  if (myReady) {
    Wire.write(1);
    myReady = false;
  }
}

void blink_all_leds() {
  for (int i = 0; i < 2; i++) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
    digitalWrite(5, HIGH);
    delay(200);
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    delay(200);
  }
}