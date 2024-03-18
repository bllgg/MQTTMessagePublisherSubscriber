#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import the MQTT client library
import paho.mqtt.client as mqtt


# Callback function to handle connection established event
def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code " + str(rc))
    # Subscribe to the topic upon successful connection
    client.subscribe("esppol/XXXXXXXX")


# Callback function to handle message reception
def on_message(client, userdata, msg):
    print("Received message on topic " + msg.topic + ": " + str(msg.payload))


# Create an MQTT client instance
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set the MQTT broker address and port
broker_address = "xxx.xxx.xxx.xxx"
broker_port = 0000

# Set username and password if authentication is required
client.username_pw_set(username="username", password="password")

# Connect to the broker
client.connect(broker_address, broker_port, 60)

# Start the loop to process incoming messages
client.loop_forever()
