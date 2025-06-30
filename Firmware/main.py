# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add encoder support
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define your pins here!
PINS = [board.D3, board.D6, board.D7, board.D8, board.D9, board.D10]

# Configure the encoder stuff
encoder_handler.pins = (
    (board.D2, board.D1, board.D0, False),  # (pin_a, pin_b, pin_button, is_inverted)
)

# Define encoder actions
Zoom_in = KC.LCTRL(KC.EQUAL)
Zoom_out = KC.LCTRL(KC.MINUS)
encoder_handler.map = [
    ((Zoom_out, Zoom_in, KC.NO),),
]

#Configuring the display stuff
bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    flip = False,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
)

display.entries = [
        TextEntry(text="Logan Macropad", x=64, y=16, x_anchor="M", y_anchor="M"),
]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.B, KC.C, 
     KC.D, KC.E, KC.F, ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
