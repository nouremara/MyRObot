#include <Servo.h>

Servo up_down;
Servo forward_backward;
Servo grab;

int pos1 = 0;    // Initialposition des ersten Servos
int pos2 = 180;  // Initialposition des zweiten Servos
int pos3 = 90;  // Initialposition des dritten Servos

void setup() {
  up_down.attach(10);  // Verbindung des ersten Servos mit Pin 9
  forward_backward.attach(11); // Verbindung des zweiten Servos mit Pin 10
  grab.attach(5); // Verbindung des dritten Servos mit Pin 11
  Serial.begin(9600);  // Initialisierung der seriellen Schnittstelle
}

void loop() {
  // Bewegung des ersten Servos nach rechts
  for (pos1 = 90; pos1 <= 180; pos1 += 1) {
    up_down.write(pos1);
    
    delay(15);
  }
  // Bewegung des zweiten Servos nach links
  for (pos2 = 90; pos2 >= 0; pos2 -= 1) {
    forward_backward.write(pos2);
    Serial.println(forward_backward.read());
    delay(15);
  }
  // Bewegung des dritten Servos nach oben
  for (pos3 = 0; pos3 <= 180; pos3 += 1) {
    grab.write(pos3);
    delay(15);
  }
  // Bewegung des ersten Servos nach links
  for (pos1 = 180; pos1 >= 90; pos1 -= 1) {
    up_down.write(pos1);
    delay(15);
  }
  // Bewegung des zweiten Servos nach rechts
  for (pos2 = 0; pos2 <= 90; pos2 += 1) {
    forward_backward.write(pos2);
    delay(15);
  }
  // Bewegung des dritten Servos nach unten
  for (pos3 = 180; pos3 >= 0; pos3 -= 1) {
    grab.write(pos3);
    delay(15);
  }

}
