import time
import gpiozero
print("Testing relays")
RELAY_PINS = [14, 15, 18, 23]

# Triggered by the output pin going high: active_high=True
# Initially off: initial_value=False

class RelayController: 
  def __init__(self):
    self.relays = []
    for pin in RELAY_PINS:
      self.relays.append(gpiozero.OutputDevice(pin, active_high=True, initial_value=True))

  def on(self, channel):
    self.relays[channel].off()
  
  def off(self, channel):
    self.relays[channel].on()

  def set(self, channel, value):
    if value:
      self.relays[channel].off()
    else:
      self.relays[channel].on()


relays = RelayController()

for i in range(4):
  print("Relay", i, "on")
  relays.on(i)
  time.sleep(1)
        
  print("Relay", i, "off")
  relays.off(i) # switch on
  time.sleep(1)

print("done")
