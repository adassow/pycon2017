import network
from umqttsimple import MQTTClient

wifi = network.WLAN(network.STA_IF)

wifi.active(True)
wifi.connect("dl", "dl")
while not wifi.isconnected():
	pass

c = MQTTClient("my_esp", "mymqtt.com")
c.connect()
c.publish(c"foo_topic", "Hello World!!!")
c.disconnect()
