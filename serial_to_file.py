##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial
import time
import os

serial_port = '/dev/cu.usbmodem1431';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt";

if os.path.isfile(write_to_file_path) :
    print "output.txt already exists!"
    exit()

output_file = open(write_to_file_path, "w+");
ser = serial.Serial(serial_port, baud_rate)

start_time = time.time()

while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    line = str(time.time() - start_time) + ", " + line
    print(line);
    output_file.write(line);
    output_file.flush();
