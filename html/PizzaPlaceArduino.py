import time, sys
from fhict_cb_01.CustomPymata4 import CustomPymata4
board = CustomPymata4(com_port = "COM7")

board.displayOn()
board.set_pin_mode_dht(12, sensor_type=11, differential=.05)
board.set_pin_mode_digital_output(4)
board.set_pin_mode_digital_output(3)

timer=14.6
loopcount=0
minute=0
seconds=0
minutemaker=1


while float(timer)>-.00000001:
    humidity, temperature, timestamp = board.dht_read(12)
    print(humidity, temperature)
    board.displayShow(timer)
    print(temperature)
    time.sleep(1)
    timer-=.01
    loopcount+=1
    seconds+=1
    if 0==seconds-60*minutemaker:
        minute+=1
        minutemaker+=1
    if 0==loopcount-60*minute:
        timer-=.40
    if float(timer)>-.001:
        board.digital_pin_write(4,1)
    else:
        board.digital_pin_write(4,0)
        board.play_tone(3,255,5)
        time.sleep(5)
        board.digital_pin_write(3,0)



        

