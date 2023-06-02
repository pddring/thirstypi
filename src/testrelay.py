import time
import gpiozero
print("Testing relays")
RELAY_PINS = [14, 15, 18, 23]

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False

relays = []
for pin in RELAY_PINS:
  relays.append(gpiozero.OutputDevice(pin, active_high=True, initial_value=True))
  
for i in range(4):
  print("Relay", i, "off")
  relays[i].on()
  time.sleep(1)
        
  print("Relay", i, "on")
  relays[i].off() # switch on
  time.sleep(1)

print("done")
