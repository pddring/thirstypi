# thirstypi
Raspberry Pi automatic watering system

This is an attempt to make an automated watering sytem using the following components:

- Raspberry Pi Zero W

Flash the Pi using the Imaging tool: https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/. I went for the lightweight version of raspbian, with SSH and WiFi enabled so that I could connect to it headless (without plugging in a screen and keyboard). I set the hostname to thirstypi

- Adafruit miniPiTFT 1.3" 240x240 screen: https://shop.pimoroni.com/products/adafruit-mini-pitft-1-3-240x240-tft-add-on-for-raspberry-pi?variant=31371861065811

This tutorial guides you through how to test the screen: https://learn.adafruit.com/pitft-linux-python-animated-gif-player/python-setup-2

Enable SPI with `raspi-config` (it's under interfacing options)

Install pip3: 
```
sudo apt-get install python3-pip
```

Install the python RGB Display library, font and other required libraries:
```
pip3 install adafruit-circuitpython-rgb-display
pip3 install --upgrade --force-reinstall spidev
sudo apt-get install fonts-dejavu
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
```

Hmm. This is a deadend - my screen has broken. I'll come back to this later.

- Relay
I have a 4 relay module a bit like this: https://www.amazon.co.uk/ELEGOO-Optocoupler-Compatible-Official-Raspberry/dp/B06XK6HCQC

|Relay pins|Pi pin name|Pi pin number|
|----------|-----------|-------------|
|GND       |GND        |6            |
|IN1       |GPIO14     |8            |
|IN2       |GPIO15     |10           |
|IN3       |GPIO18     |12           |
|IN4       |GPIO23     |16           |

- Capacitive moisture sensor

- Google Home automation
Currently working through this: https://developers.google.com/assistant/sdk/guides/service/python/embed/config-dev-project-and-account
