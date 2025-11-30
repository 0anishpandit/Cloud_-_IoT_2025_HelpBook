//Separately install this library from library manger
#include "DHT.h" // dht22 exrternal sensor ho , so yo use garna yesko library include garey ko

// Define the pin connected to the DHT22 data line
// Change this according to your physical wiring. We use pin 22 here.
#define DHT_PIN 22 // pin define garna lai hami ley yo garey ko so hami ley pin use garna sakxam

// Specify the sensor type as DHT22
#define DHT_TYPE DHT22

// Create a DHT sensor object
DHT sensor(DHT_PIN, DHT_TYPE); // Create a DHT object to use the library functions

void setup() {
  pinMode(19, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(17, OUTPUT);
  Serial.begin(9600); // Start serial communication for printing output
  sensor.begin(); // Initialize the sensor
  // sleep/delay like in Arduino programming ko lahi library by default include hunxa
}

void loop() {
  // Wait for a few seconds between measurements.
  // DHT22 typically needs at least 2 seconds between readings
  delay(2000); // every reading ma 2 second ko gap liyum (2000 milliseconds)

  // Measure temperature and humidity
  // Reading temperature or humidity takes about 250 milliseconds!
  float humidity = sensor.readHumidity(); // humidity variable ma vako value layum from sensor, jun readHumidity() ley read garey ko thiyo
  float temp = sensor.readTemperature(); // temp variable ma measure garey ko reading lai float word ko form ma rakhay ko

  // Check if any reads failed and handle the error
  if (isnan(humidity) || isnan(temp)) { // Check if the values are "Not a Number" (NaN)
    Serial.println("Failed to read sensor."); // exception message halyum in case if hamro sensor ley data read garna sakey na or sensor ma fault xa or nopt working
    return; // Skip the rest of the loop and try again
  }


  if (temp > 40 && humidity <50){
    digitalWrite(19, HIGH);
    delay(2000);
    digitalWrite(19, LOW);
    Serial.println("ALARMMMMMMMMMMMMMMMMMMMMMMM");
    Serial.print("Temperature: "); // temperature varable ma vako value print garyum
    Serial.print(temp);
    Serial.println(" C");

    Serial.print("Humidity: "); // humidity variable ma vako value print garyum
    Serial.print(humidity);
    Serial.println(" %%");
  }else if(temp > 35 && humidity<40) {
    digitalWrite(18, HIGH);
    delay(2000);
    digitalWrite(18, LOW);
    Serial.println("WARNINGGGGGGGGGGGGGGGGGGG");
    Serial.print("Temperature: "); // temperature varable ma vako value print garyum
    Serial.print(temp);
    Serial.println(" C");

    Serial.print("Humidity: "); // humidity variable ma vako value print garyum
    Serial.print(humidity);
    Serial.println(" %%");
  }else if(temp < 35 && humidity>40) {
    digitalWrite(17, HIGH);
    delay(2000);
    digitalWrite(17, LOW);
    Serial.println("COOLLLLLLLLLLLLLLLLLLLLLLL");
    Serial.print("Temperature: "); // temperature varable ma vako value print garyum
    Serial.print(temp);
    Serial.println(" C");

    Serial.print("Humidity: "); // humidity variable ma vako value print garyum
    Serial.print(humidity);
    Serial.println(" %%");
  }
  delay(2000);
}
