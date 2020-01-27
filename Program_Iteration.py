from time import sleep
import serial
from tello import Tello

import tellopy
#help(tellopy)

tello = Tello()

#tello.send_command("takeoff")

# MAKE SURE THE BAUDRATE MATCHES WITH THE ARDUINO (Serial.begin(115200);)
# ser = serial.Serial("/dev/ttyACM0",115200) #Linux
ser = serial.Serial("COM5", 9600)  # Windows

drone = tellopy.Tello()

import tellopy
from time import sleep



while True:
    line = ser.readline().decode("utf-8")  # read until newline
    #print(line)
    lineSplit = line.split(",")  # split the line into a list

    # Parse integer values and assign variables from the list:

    x1 = int(lineSplit[0])
    y1 = int(lineSplit[1])
    x2 = int(lineSplit[2])
    y2 = int(lineSplit[3])

    #print(y1)
    #rc 0 0 0 0
    #tello.send_command("rc " + str(x1) + " " +str(y1) + " " + str(x2) + " " + str(y2))



    if y2 > 600:
        print("com")
        drone.connect()
        drone.wait_for_connection(60.0)
    elif y2 < 400:
        print("LAND")
        drone.land()
    elif x2 > 600:
        print("TAKEOFF")
        drone.takeoff()
    elif x2 < 500:
        print("left")

    if y1 == 511 or y1 == 512:
        drone.set_pitch(0)



    if y1 > 514:
        print("forward")
        drone.set_pitch(1)

    elif y1 < 509:
        print("backward")
        drone.set_pitch(-1)
    elif x1 > 513:
        print("hell")
        drone.right(x1/5)
    elif x1 < 507:
        print("ii")
        drone.left(x1/5)

    if x1 == 510 or x1 == 512:
        drone.right(0)
        drone.left(0)
