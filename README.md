# simple module to operate a DC motor with a Microcontroller using micropython. 
setup:
`motor1 = DCMOTOR(IN_pin_1, IN_pin_2, EnablePin*)`  

Usage:  

`motor1.forward(1) `  
Motor runs forward at 1% power.  

`motor1.backwards(100)`  
Motor runs backwards at 100% power.  

`motor1.stop()`  
motor stops.  

`motor1.uninstall()`  
The pins de-initialize and free the pins to be used at the default setting again. 
