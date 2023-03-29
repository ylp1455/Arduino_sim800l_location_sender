# Arduino_sim800l_location_sender

# Send GPS location via SMS using Arduino and SIM800L
This project demonstrates how to send your GPS location to a given phone number via SMS using an Arduino board and SIM800L module. The project uses the TinyGPS++ library to get the GPS location and the SoftwareSerial library to communicate with the SIM800L module.

## Hardware components
- Arduino board (e.g., Arduino Uno)
- SIM800L module
- GPS module (e.g., NEO-6M)
- Push button
- Jumper wires
- Software libraries
- TinyGPS++
- SoftwareSerial
## Wiring diagram
Connect the hardware components as shown in the following diagram:

```lua
GPS module           Arduino           SIM800L module
VCC ---------------- 5V
GND ---------------- GND
TX ----------------- RX
RX ----------------- TX

```

Make sure to insert a SIM card with SMS capability into the SIM800L module and power it up. Then, press the button connected to the board to send your GPS location to the given phone number via SMS.

# License
This project is licensed under the MIT License. Feel free to use it for any purpose.