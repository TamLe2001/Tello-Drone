from time import sleep
import serial
from tello import Tello

import tellopy
#help(tellopy)

turn = 0

tello = Tello()

#tello.send_command("takeoff")

# MAKE SURE THE BAUDRATE MATCHES WITH THE ARDUINO (Serial.begin(115200);)
# ser = serial.Serial("/dev/ttyACM0",115200) #Linux
ser = serial.Serial("COM5", 9600)  # Windows

drone = tellopy.Tello()

import tellopy
from time import sleep

drone.connect()
drone.wait_for_connection(60.0)


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
        print("up")
        drone.up(60)
    elif y2 < 400:
        print("down")
        drone.down(60)
    else:
        drone.up(0)
        drone.down(0)

    if x2 > 600:
        print("clock")
        drone.clockwise(70)
    elif x2 < 400:
        print("CC")
        drone.counter_clockwise(70)
    else:
        drone.clockwise(0)
        drone.counter_clockwise(0)




    if (y1 == 511) or (y1 == 512):
        drone.set_pitch(0)



    if y1 > 550:
        print("forward")
        drone.set_pitch(1)

    elif y1 < 500:
        print("backward")
        drone.set_pitch(-1)
    elif x1 > 550:
        print("right")
        drone.right(60)
    elif x1 < 500:
        print("left")
        drone.left(60)
    else:
        drone.right(0)
        drone.left(0)

    if x1 > 1000:
        if turn == 0:
            drone.takeoff()
            print("takeoff")
            turn = 1
        elif turn == 1:
            drone.land()
            print("land")
            turn = 0