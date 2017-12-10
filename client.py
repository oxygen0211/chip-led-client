from client import LEDStrip

led = LEDStrip('chip-led.local', 5000)
success = led.setColor(255, 255, 255)
print success
