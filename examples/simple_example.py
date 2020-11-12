from GSVDevice import GSVDeviceSerial
import time

port = 1

device = GSVDeviceSerial(port)

device.set_transmission_rate(20)

try:
    while True:
        print(device.read_data())
        time.sleep(0.025)
except KeyboardInterrupt:
    del device