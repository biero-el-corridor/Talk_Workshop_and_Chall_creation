

#include <ModbusRTUSlave.h>
#include <Servo.h>
#include <LiquidCrystal_I2C.h>

// Pin Definitions
#define DE_RE_PIN 2      // MAX485 DE/RE pins (tied together)
#define SERVO_PIN 3      // Servo control pin
#define STATUS_LED 13    // Built-in LED for status indication
#define ON_LED 4 
// Modbus Configuration
#define SLAVE_ID 1       // Modbus slave ID
#define BAUD_RATE 9600   // Must match master's baud rate
#define REG_COUNT 1     // Number of holding registers
#define COIL_COUNT 10    // Number of coils
//const uint8_t coilPins[2] = {4};
// Debug mode (set to true to enable Serial debug messages)
#define DEBUG_MODE false

// Create objects
Servo myServo;
uint16_t registers[REG_COUNT];
bool coils[COIL_COUNT];
ModbusRTUSlave modbus(Serial, DE_RE_PIN);
LiquidCrystal_I2C lcd(0x27,16,2); // found the address via exemple => wire => i2c scanner 
// Variables to track state
uint16_t lastServoPos = 0;  // Default servo position
unsigned long lastComm = 0;  // Timestamp of last communication
bool ledState = false;       // LED state for blinking


void setup() {
  // Initialize serial for Modbus communication
  Serial.begin(BAUD_RATE);
  
  // Initialize pins
  pinMode(STATUS_LED, OUTPUT);
  pinMode(ON_LED, OUTPUT);
  pinMode(DE_RE_PIN, OUTPUT);
  digitalWrite(DE_RE_PIN, LOW);  // Start in receive mode
  // Initialize servo
  myServo.attach(SERVO_PIN);
  myServo.write(lastServoPos);
  
  // Initialize holding registers with default values
  for (int i = 0; i < REG_COUNT; i++) {
    registers[i] = 0;
  }
  registers[0] = lastServoPos;  // Set register 0 to default servo position

  // Configure and start Modbus slave
  modbus.configureHoldingRegisters(registers, REG_COUNT);
  modbus.configureCoils(coils, COIL_COUNT); 
  modbus.begin(SLAVE_ID, BAUD_RATE);
  
  // Indicate we're ready
  for (int i = 0; i < 3; i++) {
    digitalWrite(STATUS_LED, HIGH);
    delay(100);
    digitalWrite(STATUS_LED, LOW);
    delay(100);
  }
  // sections for init the lcd screen.  
  lcd.init();
  lcd.clear();         
  lcd.backlight();      // Make sure backlight is on
  
  // Print a message on both lines of the LCD.
  lcd.setCursor(2,0);   //Set cursor to character 2 on line 0
  lcd.print("Door open      ");
  
  lcd.setCursor(2,1);   //Move cursor to character 2 on line 1
  lcd.print("You Can pass   ");
}

void loop() {
  // Process Modbus messages
  bool activity = modbus.poll();
  modbus.poll();
  digitalWrite(ON_LED, coils[0]);

if (registers[0] >= 70) {
  coils[0] = 1;
  //digitalWrite(ON_LED, HIGH);
  // Print a message on both lines of the LCD.
  lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
  lcd.print("HZV{PhYc4l_4cC3s");
  
  lcd.setCursor(0,1);   //Move cursor to character 2 on line 1
  lcd.print("s_Fr0m_tHe_WiR3}");
} else if (registers[0] >= 50) {
  coils[0] = 1;
  //digitalWrite(ON_LED, HIGH);
  // Print a message on both lines of the LCD.
  lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
  lcd.print("Door open");
  
  lcd.setCursor(0,1);   //Move cursor to character 2 on line 1
  lcd.print("You Can pass");
} else {
  coils[0] = 0;
  // Print a message on both lines of the LCD.
  lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
  lcd.print("Door closed: You");
  
  lcd.setCursor(0,1);   //Move cursor to character 2 on line 1
  lcd.print("shall not pass");
}

  // Check if servo position needs to be updated
  if (registers[0] != lastServoPos) {
    // Constrain value to valid servo range
    uint16_t newPos = constrain(registers[0], 0, 180);
    
    // Update servo
    myServo.write(newPos);
    lastServoPos = newPos;
    
    // Rapid blink to indicate servo movement
    for (int i = 0; i < 3; i++) {
      digitalWrite(STATUS_LED, LOW);
      delay(50);
      digitalWrite(STATUS_LED, HIGH);
      delay(50);
    }
  }
}