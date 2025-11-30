Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from machine import Pin #pen define garna lai hami ley yo garey ko so hami ley pin use garna sakxam
... from time import sleep #sleep/delay like in Arduino programming ko lahi library import garey ko
... from dht import DHT22 #dht22 exrternal sensor ho , so yo use garna yesko library import garey ko
... 
... # Define the pin connected to the DHT22 data line
... # Change this according to your Wokwi diagram.json configuration
... DHT_PIN = 22 
... 
... # Create a DHT22 sensor object
... sensor = DHT22(Pin(DHT_PIN))
... 
... while True:  
...     try:
...         # Measure temperature and humidity
...         sensor.measure()  #sensor variable ma read garey ko data jun dht22 bata aauxa
...         temp = sensor.temperature() #temp variable ma  measure garey ko voltage lai word ko form ma rakhay ko , we are not using the formula library ma inbuild xa so , just voltage lai convert garyum 
...         humidity = sensor.humidity() #same temperature jastai humidity lai ni layum from voltage , jun measure ley read garey ko thiyo
... 
...         # Print the readings
...         print('Temperature: %2.2f C' % temp) # temperature varable ma vako value print garyum
...         print('Humidity: %2.2f %%' % humidity) # humidity variable ma vako value print garyum
... 
...     except OSError as e:
...         print('Failed to read sensor.') #exception message halyum in case if hamro sensor ley data read garna sakey na or sensor ma fault xa or nopt working
... 
...     # Wait for a few seconds before the next reading
...     # DHT22 typically needs at least 2 seconds between readings
