import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

PINS = [
    board.A3,   # SW1
    board.D6,   # SW2
    board.D7,   # SW3
    board.D8,   # SW4
    board.D9,   # SW5
    board.D10   # SW6
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False, 
    pull=True 
)

keyboard.keymap = [
    [
        KC.A, KC.C, KC.E,
        KC.B, KC.D, KC.G  
    ]
]

if __name__ == '__main__':
    keyboard.go()