import time
import gpiozero
print("Testing relays")
RELAY_PINS = [8, 10, 12, 16]

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False

relays = []
for pin in RELAY_PINS:
  relays.append(gpiozero.OutputDevice(pin, active_high=True, initial_value=False))
  
for i in range(4):
  print("Relay", i, "off")
  relays[i].off()
  time.sleep(1)
        
  print("Relay", i, "on")
  relays[i].on() # switch on
  time.sleep(1)

print("done")
