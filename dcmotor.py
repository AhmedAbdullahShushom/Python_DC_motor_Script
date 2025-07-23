from machine import Pin, ADC, PWM

class DCMotor:      
  def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)
        self.enable_pin = PWM(Pin(enable_pin, Pin.OUT))
        self.min_duty = min_duty
        self.max_duty = max_duty

  def forward(self,speed):
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)
    
  def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

  def stop(self):
    self.enable_pin.duty(0)
    self.pin1.value(0)
    self.pin2.value(0)
   
  def uninstall(self):
      self.pin1.off()
      self.pin2.off()
      self.enable_pin.deinit()
      print("motor is detached from the pulse pins \n")
      print(self.pin1,self.pin2,self.enable_pin, ": are reset to GPIO default")
      
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle
