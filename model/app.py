import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    arduino.flush()
    time.sleep(0.1)
    data = arduino.readline()
    return data

idx = 0
for i in range(1000):
    val = ""
    if idx % 2 == 0:
        val = write_read(str(0))
    else:
        val = write_read(str(1))

    idx += 1
    print ('am primit', val)

