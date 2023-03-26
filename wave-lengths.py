# the purpose of this program is to map explorer buttons to sound frequencies which will be displayed on the
# screen and also just to generally fuck about
import time, machine
from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER
from pimoroni import Button, Analog, Buzzer

# Set up the display
display = PicoGraphics(display=DISPLAY_PICO_EXPLORER)

# Create a pen colour to draw with
WHITE = display.create_pen(255, 255, 255)

# Set up buttons with correct pin numbers
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

# Set up analogs using correct pin number
adc0 = Analog(26)
adc1 = Analog(27)
adc2 = Analog(28)

# Create buzzer with GPIO 0-7 (the pin needs to be connected to AUDIO with a wire)
buzzer = Buzzer(0)

# Choose a font and switch to the white pen
display.set_font("bitmap8")
display.set_pen(WHITE)

# Display some text
display.text("Hello Explorer", 0, 0, scale=3)

# Update the screen
display.update()

def press_button(button_state, message, freq):
    if (button_state):
        print(message)
        buzzer.set_tone(freq)
        time.sleep(0.5)
        buzzer.set_tone(0)
        
def read_adc(adc):
    print(adc.read_voltage())
    time.sleep(5)
    
def play_tone(freqs):
    for f in freqs:
        buzzer.set_tone(f)
        time.sleep(0.2)
        buzzer.set_tone(0)
        time.sleep(0.2)

while True:
    state_a = button_a.read()
    state_b = button_b.read()
    state_x = button_x.read()
    state_y = button_y.read()
    press_button(state_a, 'a', 100)
    press_button(state_b, 'b', 500)
    press_button(state_x, 'c', 1000)
    press_button(state_y, 'd', 5000)
    
    play_tone([250, 500, 1000])
    
    buzzer.set_tone(0)
    
    #read_adc(adc0)
    #read_adc(adc1)
    #read_adc(adc2)
