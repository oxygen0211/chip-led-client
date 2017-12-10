# CHIP LED client

client library for https://github.com/oxygen0211/chip-led-controller

## usage
```
from client import LEDStrip

led = LEDStrip('chip.local', 5000)
success = led.setColor(255, 255, 255)
```

for example see client.py
