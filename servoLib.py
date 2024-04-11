import machine
import utime 

class ServoMotor:
    def __init__(self, pin):
        self.pin = pin
        self.pwm = machine.PWM(pin)
        self.pwm.freq(50)

    def set_angle(self, angle):
        duty_cycle = self._map(angle, 0, 180, 20, 120)
        self.pwm.duty(duty_cycle)

    def _map(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)




