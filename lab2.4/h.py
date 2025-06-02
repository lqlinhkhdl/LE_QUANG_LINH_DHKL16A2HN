import network
import time 
import json
from machine import Pin
from umptt.simple import MQTTClient
import dht

sensor = dht.DHT22(Pin(2))  # Pin where the DHT22 is connected
sensor.measure()  # Initialize the sensor
time.sleep(2)  # Wait for the sensor to stabilize

