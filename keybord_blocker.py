import keyboard
import os

HOTKEY_FILE = "hotkey.txt"
if not os.path.exists(HOTKEY_FILE):
    print("File hotkey.txt is not found. First, launch set_hotkey.py")
    exit(1)

with open(HOTKEY_FILE, "r") as f:
    try:
        hotkey_scan_code = int(f.read().strip())
    except ValueError:
        print("Wrong formate, hotkey.txt")
        exit(1)

keyboard_blocked = False

# Латиница, цифры, кириллица
latin_letters = list("abcdefghijklmnopqrstuvwxyz0123456789")
russian_letters = list("ёйцукенгшщзхъфывапролджэячсмитьбю")
other_keys = [
    'space', 'enter', 'tab', 'backspace', 'shift', 'ctrl', 'alt',
    'caps lock', 'esc', 'up', 'down', 'left', 'right',
    'home', 'end', 'delete', 'insert', 'page up', 'page down',
    'win', 'menu', 'print screen'
]

keys_to_block = latin_letters + russian_letters + other_keys

def toggle_block():
    global keyboard_blocked
    keyboard_blocked = not keyboard_blocked
    if keyboard_blocked:
        print("Keybord is blocked.")
        for key in keys_to_block:
            try:
                keyboard.block_key(key)
            except:
                pass
    else:
        print("Keybord is unblocked.")
        keyboard.unhook_all()
        keyboard.hook(dummy_block)
        keyboard.on_press_key(hotkey_scan_code, lambda _: toggle_block(), suppress=False)

def dummy_block(e):
    pass

keyboard.hook(dummy_block)
keyboard.on_press_key(hotkey_scan_code, lambda _: toggle_block(), suppress=False)

print(f"Program is ready. (scan_code): {hotkey_scan_code}")
keyboard.wait()