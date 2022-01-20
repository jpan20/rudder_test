# Rudder Test

# Contents

- [Wiring](#wiring)
- [Configuration](#configuration)
- [Run the test](#runthetest)

# Wiring
Rudder pins are connected to M1A M1B on roboclaw.

Potentiometer green pin to EN1, orange pin to encoder power, black pin to ground :
<p align="center"><img src="https://user-images.githubusercontent.com/47678311/150372742-87883759-2e3b-4509-8113-fe85f6c1f0c5.jpeg" | width=300></p >
<p align="center"><img src="https://user-images.githubusercontent.com/47678311/150373292-7378792c-87cf-4b3a-83c0-51150ad1509f.jpeg" | width=300></p >

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
