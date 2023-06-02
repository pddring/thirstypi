import gpiozero

class RelayController: 
  def __init__(self, pins=[14, 15, 18, 23]):
    self.relays = []
    for pin in pins:
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