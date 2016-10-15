from gpiozero import LED

from time import sleep


if(__name__=="__main__"):
    led = LED(17)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)