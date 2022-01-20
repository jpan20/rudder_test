# rudder_test

# Contents

- [Wiring](#wiring)
- [Configuration](#configuration)
- [Run the test](#runthetest)

# Wiring
Rudder pins are connected to M1A M1B on roboclaw:
<p align="center"><img src="https://user-images.githubusercontent.com/47678311/150372702-57bcd579-8339-47f3-b517-290cb1cb9419.jpeg"></p>

Potentiometer green pin to EN1, orange pin to encoder power, black pin to ground :
<p align="center"><img src="https://user-images.githubusercontent.com/47678311/150373292-7378792c-87cf-4b3a-83c0-51150ad1509f.jpeg"></p>

# Configuration
* Make sure motor voltage range: 11V ~ 13V
* Max current: 1A
* PWM mode: Locked Antiphase
* Encoder mode: Analog
* Control mode: Packet Serial Mode

# Run the test

* cd into test folder 
   ```
   $ python test.py
   ```
* rudder angle will be printed out
* type "quit" in command line will terminate the test
