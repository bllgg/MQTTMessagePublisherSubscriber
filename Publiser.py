# This shows a simple example of waiting for a message to be published.

# import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid, reason_code, properties):
    print("mid: " + str(mid))


def on_log(mqttc, obj, level, string):
    print(string)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
# Set the MQTT broker address and port
broker_address = "xxx.xxx.xxx.xxx"
broker_port = 0000
mqttc.username_pw_set("username", "password")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect(broker_address, broker_port, 60)

mqttc.loop_start()

print("tuple")
deviceSerial = "XXXXXXXX"
stringList = "Heeeeeeeey"
(rc, mid) = mqttc.publish("esppol/XXXXXXXX", "{\"deviceId\":" + deviceSerial + "\"message\":" + stringList + "}", qos=1)
print("class")
infot = mqttc.publish("esppol/XXXXXXXX", "{\"deviceId\":" + deviceSerial + "\"message\":" + stringList + "_test" + "}",qos=1)

infot.wait_for_publish()
