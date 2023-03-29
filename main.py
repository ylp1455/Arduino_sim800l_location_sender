import serial
import time

port = "/dev/ttyS0"  # replace with your serial port
phone_number = "+947812345678"  # replace with your recipient's number

ser = serial.Serial(port, baudrate=9600, timeout=5)

def send_location():
    ser.write(b'AT+CGNSINF\r\n')  # get current GPS location
    time.sleep(1)
    response = ser.read(ser.in_waiting).decode('utf-8').strip()
    if '+CGNSINF: ' in response:
        data = response.split(',')[1:3]
        lat = data[0][:2] + '.' + data[0][2:]
        lng = data[1][:3] + '.' + data[1][3:]
        message = "My current GPS location: {}, {}".format(lat, lng)
        ser.write(b'AT+CMGF=1\r\n')  # set SMS mode to text
        time.sleep(1)
        ser.write(('AT+CMGS="' + phone_number + '"\r\n').encode('utf-8'))  # set recipient's number
        time.sleep(1)
        ser.write((message + "\r\n").encode('utf-8'))  # send message
        time.sleep(1)
        ser.write(bytes([26]))  # send Ctrl+Z to end message
        time.sleep(1)
        response = ser.read(ser.in_waiting).decode('utf-8').strip()
        if 'OK' in response:
            print("Location sent to", phone_number)
        else:
            print("Failed to send location")

send_location()
ser.close()
