import time
import RPi.GPIO as GPIO


class LightControl:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.light_1 = 18
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.light_1, GPIO.OUT)


    def run(self):
        count_down = 0
        while True:
            current_time = time.time()
            should_light_on = self.compute(current_time, count_down)
            if should_light_on:
                print("Turn on the light")
                GPIO.output(self.light_1, GPIO.HIGH)
            else:
                print("Turn off the light")
                GPIO.output(self.light_1, GPIO.LOW)
            time.sleep(5)
            count_down += 1

    @staticmethod
    def compute(current_time, count_down) -> bool:
        if(count_down % 10) == 0:
            return False
        else:
            return True
