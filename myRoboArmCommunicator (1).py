# Nour Ahmed and Moaaz ABC
# Matrikal-Nr.: 5200991 and 123456789

#========================================================================
# @file  myRoboArmCommunicator.py
# @brief The entry point of the application.
#
# Manages serial communication between a computer (running python) and Arduino
# for the purpose of controlling the a 3R Robot Arm
#
# @author    Nour Ahmed and Moaaz ABC
# @email     nahmed@stud.hs-bremen.de and Moaaz.ABC@stud.hs-bremen.de
# @repo      https:#github.com/nouremara/myPong
# @createdOn 12.01.2023
# @version   1.0.0
 #========================================================================

import serial
import time

PORT="COM3"         # you can get the serial ports available in a terminal with this command: python -m serial.tools.list_ports
BAUD_RATE=9600      # you may change this to match the one used in Arduino

# Open serial port
serialPort = serial.Serial(PORT, BAUD_RATE)
#-------------------------------------------------------------------------

servo1value = 0     # Initialposition des ersten Servos
servo2value = 180   # Initialposition des zweiten Servos
servo3value = 90    # Initialposition des dritten Servos
servo4value = 135   # Initialposition des dritten Servos
delay_between_commands=15
#-------------------------------------------------------------------------

#==============================================================================
# recvFromArduino
#==============================================================================
def recvFromArduino():
    """
    --Description--
    Recieve a message from the Arduino. The message is interpreted as a string being
    between the start character '<' and end character '>'

    --Parameters--
    None

    --Returns--
    msg -> The received message as a string

    """
    msg = ""
    x = "z"  # any value that is not an end or startMarker
    byteCount = -1  # to allow for the fact that the last increment will be one too many
    
    startMarker = 60  # unicode character '<'
    endMarker = 62  # unicode character '>'
    
    # wait for the start character
    while ord(x) != startMarker:  # ord returns the unicode number for the character
        x = serialPort.read()

    # save data until the end marker is found
    while ord(x) != endMarker:
        if ord(x) != startMarker:
            msg = msg + x.decode("utf-8")  # decode from unicode
            byteCount += 1
        x = serialPort.read()

    return(msg)
#==============================================================================

#==============================================================================
# Main 
#==============================================================================
print("Serial port " + PORT + " opened  Baudrate " + str(BAUD_RATE))


# print first message received from Arduino
print(recvFromArduino())

# convert values to a string of comma separated values
data = str(servo1value) + ","  + str(servo2value) + ","  + str(servo3value) + "," + str(servo4value) + "\n"

# write to the serial port
serialPort.write(data.encode('utf-8'))  # encode as unicode

# print reply message received from Arduino
print(recvFromArduino())

# wait for the given time
time.sleep(delay_between_commands)

# close serial port
serialPort.close()