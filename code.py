#include <MeMegaPi.h>

// Define motor objects for each motor connected to the MegaPi board
MeMegaPiDCMotor motor1(PORT1B);
MeMegaPiDCMotor motor2(PORT2B);
MeMegaPiDCMotor armMotor3(PORT3B);
MeMegaPiDCMotor motor4(PORT1A);

// Define the ultrasonic sensor object
MeUltrasonicSensor ultrasonic(PORT_7);

// Define the speeds for each motor (adjust as needed)
int motorSpeed1 = 200;
int motorSpeed2 = 200;
int armMotor = 100;
int gripperMotor = 150;
int distanceThreshold = 20;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Read the distance from the ultrasonic sensor
  int distance = ultrasonic.distanceCm();
  Serial.print("Distance: ");
  Serial.println(distance);

  // If the object is farther than the threshold, move motors
  if (distance > distanceThreshold) {
    // Move both motors forward for 2 seconds
    motor1.run(motorSpeed1);
    motor2.run(motorSpeed2);
    delay(2000);
    
    // Move the arm up
    armMotor3.run(-armMotor);
    delay(100); 

    //move the erm down
    armMotor3.run(-armMotor);
    delay(1000);

    // Open the gripper
    motor4.run(-gripperMotor);
    delay(2000);
    //open the grippper
    motor4.run(-gripperMotor);
    delay(2000); 
  } else {
    
    // If the object is within threshold, stop motors and close gripper
    motor1.run(0);
    motor2.run(0);
    
    // Stop the arm
    armMotor3.run(0);

    // Close the gripper
    motor4.run(gripperMotor);
    delay(2000);
  }

  // Stop the gripper motor after operation
  motor4.run(0);
}
