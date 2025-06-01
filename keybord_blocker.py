import keyboard
import time
import os

HOTKEY_FILE = "hotkey.txt"
if not os.path.exists(HOTKEY_FILE):
    print("Hotkey not found. First run: set_hotkey.py")
    exit(1)

with open(HOTKEY_FILE, "r") as f:
    hotkey = f.read().strip()

keyboard_blocked = False

def toggle_block():
    global keyboard_blocked
    keyboard_blocked = not keyboard_blocked
    print("Keybord is blocked." if keyboard_blocked else "Keybord is unblocked.")

keyboard.add_hotkey(hotkey, toggle_block)

print("Program is running. Press the hotkey to block/unblock the keyboard.")
try:
    while True:
        if keyboard_blocked:
            keyboard.block_key('*') 
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Closing the program.")
