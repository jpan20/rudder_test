import threading
import time
import sys
from roboclaw import Roboclaw

rc = Roboclaw("/dev/ttyACM0", 38400)
rc.Open()
rc.ReadVersion(0x80)
#Parameters
rc.ReadMinMaxMainVoltages(0x80)
rc.SetMainVoltages(0x80, 110, 130) # Allowed range: 11 V - 13 V
rc.SetM1MaxCurrent(0x80, 500) # 2 Amps
rc.SetPWMMode(0x80, 0) # Locked Antiphase
rc.SetM1EncoderMode(0x80, 1) # Analog Mode
#Configuration
getConfig = rc.GetConfig(0x80)
config = getConfig[1] # index zero is 1 for success, 0 for failure.
config = config | 0x0003 # Packet serial mode
rc.SetConfig(0x80, config)
rc.SetPinFunctions(0x80, 2, 0, 0) # S3 = E-Stop, S4 = Disabled, S5 = Disabled
rc.WriteNVM(0x80)

def gotoPos():
    while True:
        count = rc.ReadEncM1(0x80)
        print(count[1])
        P = 250
        I = 120
        D = 180
        maxI = 100
        deadZone = 20
        minPos = 0
        maxPos = 2000
        rc.SetM1PositionPID(0x80, P, I, D, maxI, deadZone, minPos, maxPos)
        rc.ReadM1PositionPID(0x80)
        accel = 100
        speed = 200
        deccel = 100
        angle = 0
        position = int(1396 + -9.95*angle + 0.00118*angle**2 + 0.000915*angle**3)
        rc.SpeedAccelDeccelPositionM1(0x80, accel, speed, deccel, position, 1)

#Runs regardless of user input
threading1 = threading.Thread(target=gotoPos)
threading1.daemon = True
threading1.start()

while True:
    if raw_input().lower() == 'quit':
        rc.DutyAccelM1(0x80, 0, 0)
        sys.exit()
