

import urequests
import machine
i2c = machine.I2C('X')
machine.Pin.board.EN_3V3.value(1)
packages = {}

# main.py -- put your code here!

def connect_wifi():
    from wifi.wifi_connect import *
    myWifi = Wifi_manager()
    myWifi.retries(8)
    myWifi.connect('Kinkerl', 'testtest')


print("connect to new wifi")
connect_wifi()

print("get bus")

for i2c_bus_id in i2c.scan():
    print("trying to get something for: "+str(i2c_bus_id))
    #TODO: only do that if it does not yet exist
    #TODO: check for updates?!
    response = urequests.get('https://micropython-sensor-registry.eu.aldryn.io/sensor/?identifier='+str(i2c_bus_id))
    response_data = response.json()
    if response_data:
        package = response_data[0]["package"]
        code = response_data[0]["code"]
        if code:
            code
            f = open(package+'.py', 'w')
            f.write(code)
            f.close()
        else:
            print("installing "+package)
            upip.install(package)
        
        packages[i2c_bus_id] = package

for i2c_bus_id in packages:

    p = __import__(packages[i2c_bus_id])
    data = p.read_data(i2c, i2c_bus_id)
    data = p.read_data(i2c, i2c_bus_id)
    print(data)
