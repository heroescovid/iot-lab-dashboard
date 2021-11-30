import paho.mqtt.client as mqtt
#Connection success callback
def on_connect(client, userdata, flags, rc):
    client.subscribe("testtopic/#")
    client.publish("testtopic/said",payload = "hola mundo",qos = 0)
    print('Connected with result code '+str(rc))
# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
client_mqtt = mqtt.Client()
# Specify callback function
client_mqtt.on_connect = on_connect
client_mqtt.on_message = on_message
# Establish a connection
client_mqtt.connect("broker.emqx.io",1883,60)
client_mqtt.subscribe("dashboard/#")
# Publish a message
client_mqtt.publish("dashboard/temperatura",payload = "hola",qos = 0)
client_mqtt.publish("dashboard/temperatura",payload = "hola",qos = 0)
client_mqtt.loop_forever()