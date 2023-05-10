import pyperclip
from pynput.mouse import Button, Controller
import time

"""
The idea is to retrieve messages from closed telegram (or any other messager) messages one by one from screen and save 
them in clipboard then save in appropriate format

pynput wiki https://pynput.readthedocs.io/en/latest/mouse.html
pyperclip wiki https://pypi.org/project/pyperclip/
"""

# Laptop screen options
message_1 = (1003, 710)  # start

# Read pointer position
mouse = Controller()
# print('The current pointer position is {0}'.format(
#     mouse.position))  # (1003, 710)
mouse.position = message_1
mouse.press(Button.left)
time.sleep(1)
mouse.press(Button.right)

# After message is copied, save it from clipboard into variable


# text = pyperclip.paste()
# print(text)

# Append