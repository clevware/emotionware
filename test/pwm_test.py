import time
import RPi.GPIO as GPIO

USING_PIN = 17


GPIO.setmode(GPIO.BOARD)
GPIO.setup(USING_PIN, GPIO.OUT)

p = GPIO.PWM(USING_PIN, 50)  # 通道为 12 频率为 50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()