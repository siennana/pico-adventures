from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from pimoroni import Button  #Button(button, invert=True, repeat_time=200, hold_time=1000)
from machine import Pin

# Set up the display
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

# Onboard led
led = Pin(25, Pin.OUT)

#GPIO
GP2 = Pin(2, Pin.OUT)

# Set up the buttons
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)
# returns true if the button is held down
#state = button_a.read()

led.value(1)
GP2.value(0)

# Create a pen colour to draw with
WHITE = display.create_pen(255, 255, 255)

# Choose a font and switch to the white pen
display.set_font("bitmap8")
display.set_pen(WHITE)

# Display some text
display.text("What's up Joshypoo", 10, 30, wordwrap=100, scale=5)

# Update the screen
display.update()
