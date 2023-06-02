import time
import gpiozero
from RelayController import *
print("Testing relays")
RELAY_PINS = [14, 15, 18, 23]

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False
relays = RelayController(RELAY_PINS)

for i in range(4):
  print("Relay", i, "on")
  relays.on(i)
  time.sleep(1)
        
  print("Relay", i, "off")
  relays.off(i) # switch on
  time.sleep(1)

print("done")
