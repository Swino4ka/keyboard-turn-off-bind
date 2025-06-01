import keyboard
import os
import string

HOTKEY_FILE = "hotkey.txt"
if not os.path.exists(HOTKEY_FILE):
    print("File hotkey.txt is not found. First, launch set_hotkey.py")
    exit(1)

with open(HOTKEY_FILE, "r") as f:
    try:
        hotkey_scan_code = int(f.read().strip())
    except ValueError:
        print("Wrong format, hotkey.txt")
        exit(1)

keyboard_blocked = False

latin = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
cyrillic = list("ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
polish = list("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
german_french_spanish = list("äöüßèéêîçñÄÖÜËÏÑ")

unicode_letters = latin + cyrillic + polish + german_french_spanish

special_keys = [
    'space', 'enter', 'tab', 'backspace', 'caps lock',
    'esc', 'insert', 'delete', 'home', 'end',
    'page up', 'page down',
    'up', 'down', 'left', 'right',
    'num lock', 'scroll lock', 'pause',
    'print screen', 'menu', 'application',
    'windows', 'winleft', 'winright',
    'shift', 'shiftleft', 'shiftright',
    'ctrl', 'ctrlleft', 'ctrlright',
    'alt', 'altleft', 'altright'
]

function_keys = [f"f{i}" for i in range(1, 25)]

combos_to_block = [
    "alt+f4", "alt+tab", "alt+esc", "alt+enter",
    "win+d", "win+r", "win+e", "win+tab",
    "ctrl+s", "ctrl+z", "ctrl+x", "ctrl+v", "ctrl+c", "ctrl+a"
]

modifiers = ['shift', 'ctrl', 'alt', 'windows']

keys_to_block = unicode_letters + special_keys + function_keys + modifiers

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
        for combo in combos_to_block:
            try:
                keyboard.add_hotkey(combo, lambda: None, suppress=True)
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
