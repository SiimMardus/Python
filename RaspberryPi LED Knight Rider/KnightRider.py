# This program takes Raspberry Pi pin numbers to which LED's are connected to and displays K.I.T.T's front light on them

# GPIO and pins setup
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = [17,27,22,23,24,25,16,26,20,21]
GPIO.setup(pins,GPIO.OUT)

# Loops the lights back and forth
def knightRider():
    lightInfo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 0, 10: 0}
    lightMap = {1: 17, 2: 27, 3: 22, 4: 23, 5: 24, 6: 25, 7: 16, 8: 26, 9: 20, 10: 21}

    while True:
        head = 0
        right(lightInfo, lightMap, head)
        head = 10
        left(lightInfo, lightMap, head)

# Takes the trail right
def right(lightInfo, lightMap, head):

    litCheck = 1

	# Litcheck is the amount of LED's currently lit
	# If it is 0, the trail has reached the end and the function can end
    while litCheck > 0:
	time.sleep(0.1)
        litCheck = 0

		# Moves the head of the trail and switches the lights accordingly
        head += 1

        for i in range(head, head - 3, -1):
            if i in lightInfo:
                if lightInfo[i] == 0:
                    lightOn(lightMap[i])
                lightInfo[i] = 1
                litCheck += 1

        if (head - 3) in lightInfo:
            lightInfo[head - 3] = 0
            lightOff(lightMap[head - 3])


# Same as right() but goes left
def left(lightInfo, lightMap, head):
    litCheck = 1

    while litCheck > 0:
	
	time.sleep(0.1)

        litCheck = 0
        head -= 1

        for i in range(head, head + 3, 1):
            if i in lightInfo:
                if lightInfo[i] == 0:
                    lightOn(lightMap[i])
                lightInfo[i] = 1
                litCheck += 1

        if (head + 3) in lightInfo:
            lightInfo[head + 3] = 0
            lightOff(lightMap[head + 3])


# Turns on LED at lightNumber
def lightOn(lightNumber):
    GPIO.output(lightNumber, GPIO.HIGH)

# Turns off LED at lightNumber
def lightOff(lightNumber):
    GPIO.output(lightNumber, GPIO.LOW)

knightRider()
