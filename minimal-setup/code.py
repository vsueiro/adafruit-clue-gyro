import time
from adafruit_clue import clue

# This is a simple script to detect button presses on the Adafruit CLUE

print(clue)

while True:
    if clue.button_a:
        print("Button A pressed!")

    if clue.button_b:
        print("Button B pressed")

    time.sleep(0.05)
