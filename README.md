# 🛡️ Keyboard Blocker for Your PC

This is a simple Python tool to block all keyboard input when a hotkey is pressed. Perfect for cat owners, streamers, or anyone who wants to prevent accidental key presses.

## 🚀 Features

- ✅ Blocks **all keyboard input**
- ✅ Blocks special keys (Enter, Tab, Arrows, Ctrl, Alt, Win, etc.)
- ✅ Blocks dangerous key combos (Alt+F4, Win+R, Ctrl+Z, etc.)
- ✅ Works **without admin privileges**
- ✅ Supports **hotkey switching**
- ✅ Safe and simple

---

## 📁 Project Structure

```

keyboard\_guard/
├── set\_hotkey.py        # Lets you pick a hotkey (saved by scan code)
├── keyboard\_blocker.py  # Main script that blocks/unblocks the keyboard
├── hotkey.txt           # Saved hotkey (as scan code)
└── requirements.txt     # Required Python packages

````

---

## 🧪 Installation

1. Clone this repository or download the files.
2. Install required dependencies:

```bash
pip install -r requirements.txt
````

3. Run the hotkey setup:

```bash
set_hotkey.py
```

4. Press the key you want to use to toggle the blocker.

5. Then run the main blocker script:

```bash
keyboard_blocker.py
```

---

## ⚠️ Notes

* The script uses **scan codes** for hotkeys, which makes them layout-independent.
* If you lock your keyboard and forget the hotkey reboot or kill the script manually.
* Tested on Windows. May require tweaks for Linux/MacOS.

---
