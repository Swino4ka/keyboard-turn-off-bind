import keyboard

print("Press the key that you want to use as a hotkey to block / unblock your keyboard...")

key = keyboard.read_key()
with open("hotkey.txt", "w") as f:
    f.write(key)

print(f"Hotkey '{key}' saved to 'hotkey.txt'.")
