import network          # wifi library ho 
import time             # sleep ani delay ko lagi
from machine import Pin # hardware pin haru ko access esp32 ko board ko
from umqtt.simple import MQTTClient  # Lightweight MQTT client library for ESP32

#wifi ko configuration garey ko hami ley 
WIFI_SSID = "Wokwi-GUEST"        
WIFI_PASSWORD = ""              

MQTT_BROKER = "broker.hivemq.com"   # Public MQTT broker address 
MQTT_CLIENT_ID = "esp32_wokwi_01"   # Unique client ID for this ESP32 device
MQTT_TOPIC = b"wokwi/led/control"   # Topic  subscribe ko lagi  (binary string required by MQTT)

LED_PIN = 2  #led connect garey ko pin 
led = Pin(LED_PIN, Pin.OUT)  # led ma output ho vaney ra

#wifi ko connectivity create garney
def connect_wifi():
    print("Connecting to WiFi...")
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object in Station mode (STA_IF = client mode)
    wlan.active(True)                    # Activate the WiFi interface
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)  # Connect to the specified WiFi network

    # Wait until the connection is established
    while not wlan.isconnected():
        time.sleep(0.5)  # Pause for half a second before checking again

    # Once connected,ip address dekhauxa
    print("WiFi connected!")
    print("IP:", wlan.ifconfig()[0]) 


def mqtt_callback(topic, msg):
    # function is automatically called when message is received on the subscribed topic
    print("Message received:", msg)

    # If the message is "ON"
    if msg == b"ON":
        led.value(1) #led on harnu
        print("LED ON")

    # If the message is "OFF"
    elif msg == b"OFF":
        led.value(0)  # led off garnu
        print("LED OFF")


connect_wifi()  # First, connect the ESP32 to WiFi

#broker lai connect gariyo with function and protocol
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)


#mqtt callback , msg receive garna lai
client.set_callback(mqtt_callback)

# Connect to the MQTT broker
client.connect()

# Subscribe to the chosen topic so we can receive LED control messages
client.subscribe(MQTT_TOPIC)

print("Subscribed to:", MQTT_TOPIC)

# Infinite loop  new MQTT messages ko lagi to check the instuction
while True:
    client.check_msg()    #msg check garey ko 
    time.sleep(0.1)    