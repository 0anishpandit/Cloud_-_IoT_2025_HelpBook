from machine import Pin # pin define garna lai hami ley yo garey ko so hami ley pin use garna sakxam
from time import sleep # sleep/delay like in Arduino programming ko lahi library import garey ko
from dht import DHT22 # dht22 exrternal sensor ho , so yo use garna yesko library import garey ko

# Define the pin connected to the DHT22 data line
# Change this according to your Wokwi diagram.json configuration. We use pin 22 here.
DHT_PIN = 22 

# Define the pins for the output indicators (LEDs/Buzzer)
ALARM_PIN = 19
WARNING_PIN = 18
COOL_PIN = 17

# Create a DHT22 sensor object
sensor = DHT22(Pin(DHT_PIN)) # Create a DHT object to use the library functions

# Setup the output pins (pinMode in Arduino terminology is handled during Pin object creation in MicroPython)
pin_alarm = Pin(ALARM_PIN, Pin.OUT) # pin lai OUTPUT mode ma set garey ko
pin_warning = Pin(WARNING_PIN, Pin.OUT) # pin lai OUTPUT mode ma set garey ko
pin_cool = Pin(COOL_PIN, Pin.OUT) # pin lai OUTPUT mode ma set garey ko

# Ensure all pins start LOW (OFF)
pin_alarm.value(0)
pin_warning.value(0)
pin_cool.value(0)

while True:  # The main loop, equivalent to Arduino's loop()
    # Wait for a few seconds between measurements.
    # DHT22 typically needs at least 2 seconds between readings
    # Note: We place this delay at the start, as the internal if-block delays will handle timing otherwise.
    
    # Measure temperature and humidity
    try:
        sensor.measure()  # sensor variable ma read garey ko data jun dht22 bata aauxa
        humidity = sensor.humidity() # humidity variable ma vako value layum from sensor, jun readHumidity() ley read garey ko thiyo
        temp = sensor.temperature() # temp variable ma measure garey ko reading lai float word ko form ma rakhay ko

        # Print the readings first
        print('Temperature: %2.2f C' % temp) # temperature varable ma vako value print garyum
        print('Humidity: %2.2f %%' % humidity) # humidity variable ma vako value print garyum
        
        # Check conditions (if/elif is like if/else if in Arduino)
        if temp > 40 and humidity < 50: # condition check garey ko
            pin_alarm.value(1) # digitalWrite(19, HIGH)
            print("ALARMMMMMMMMMMMMMMMMMMMMMMM")
            sleep(2) # delay(2000) - keep LED on for 2 seconds
            pin_alarm.value(0) # digitalWrite(19, LOW)

        elif temp > 35 and humidity < 40: # condition check garey ko
            pin_warning.value(1) # digitalWrite(18, HIGH)
            print("WARNINGGGGGGGGGGGGGGGGGGG")
            sleep(2) # delay(2000) - keep LED on for 2 seconds
            pin_warning.value(0) # digitalWrite(18, LOW)

        elif temp < 35 and humidity > 40: # condition check garey ko
            pin_cool.value(1) # digitalWrite(17, HIGH)
            print("COOLLLLLLLLLLLLLLLLLLLLLLL")
            sleep(2) # delay(2000) - keep LED on for 2 seconds
            pin_cool.value(0) # digitalWrite(17, LOW)
        
        else:
            # If no conditions were met, wait for 2 seconds before looping again
            sleep(2) # every reading ma 2 second ko gap liyum

    except OSError as e:
        print('Failed to read sensor.') # exception message halyum in case if hamro sensor ley data read garna sakey na or sensor ma fault xa or nopt working
        sleep(2) # Wait 2 seconds before trying again after a failure
