Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import time #important for the adding delays 
import network  #module used for managing the wifi connectivity
from umqtt.simple import MQTTClient #making the MQTT Communication Library

#1 : Creating Object for the Wifi in "Station Mode"(phone lai router sanga connecting garey jasto)
#2 : Station Mode(STA Mode)--> it is a mode where device act like a client that connects to a wifi router or access point 
#3 : Connecting to router
wifi = network.WLAN(network.STA_IF)

#4 : Turning the Wifi ON
wifi.active(True)

#5 : Connecting with the proper network (SSID + Password)
wifi.connect("Wokwi-GUEST" , "")

#6 : Waiting till connection or checking for the connection 
print("Connecting...", end= "")
while not wifi.isconnected():
  print(".", end="") #shows progress of connecting with dot 
  time.sleep(0.5) #small delay

#7 : Once Connected Shows Success
print("Connected! ")
... print("Network Details: " , wifi.ifconfig())  #jsut shows IP address
... 
... 
... ## Install Node-Red Locally 
... #1. Install Node.js from official site
... #2. Install Node-Red
...     #-->Open CMD
...     #-->npm install -g --unsafe-perm node-red
...     #--> Start Node red(node-red)
...     #--> npm install node-red-dashbaord(optional)
... 
... 
... ###MQTT Server Configuration
... MQTT_CLIENT_ID = "value_send"
... MQTT_BROKER = "broker.mqttdashboard.com"   # corrected spelling
... MQTT_USER = ""
... MQTT_PASSWORD = ""
... MQTT_TOPIC = "value"
... 
... 
... ## Connecting to the broker
... client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
... client.connect()
... print("Connected to MQTT Broker")
... 
... i = 0
... import ujson   # add this at the top
... 
... i = 0
... while True:
...     # create JSON message
...     message = ujson.dumps({
...         "count": i,
...         "status": "running"
...     })
...     print(message)
...     client.publish(MQTT_TOPIC, message)   # publish JSON string
...     i += 1
