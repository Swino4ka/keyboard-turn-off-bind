import keyboard

print("Press the button that you want to use as a hotkey...")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        scan_code = event.scan_code
        with open("hotkey.txt", "w") as f:
            f.write(str(scan_code))
        print(f"Hotkey is saved as scan-code: {scan_code}")
        break