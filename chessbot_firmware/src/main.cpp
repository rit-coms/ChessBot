#include <Arduino.h>
#include <Angles.h>

// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  using namespace Angles;

  int result = myFunction(2, 3);
  Vect2d vect = Vect2d(1,1);
  Armangles output = calculate(vect);
  Serial.println("Hello World!! :)");
  Serial.println(output.shoulder);
  Serial.println(output.elbow);
}

void loop() {
  // put your main code here, to run repeatedly:
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}
