# Unpaste

**Unpaste** is a cross-platform CLI tool that strips formatting from clipboard text and pastes it as plaintext. No more manual pasting into Notepad!

## Features
- **Cross-Platform:** Linux, macOS, Windows.
- **Zero Dependencies:** Uses `pyperclip` and platform-native tools.
- **Instant:** No GUI, no bloat.

## Installation
```bash
pip install pyperclip click pywin32  # Windows only
chmod +x unpaste.py
sudo ln -s $(pwd)/unpaste.py /usr/local/bin/unpaste
```

## Usage
```bash
unpaste          # One-time paste
unpaste --daemon # Run in background (not yet implemented)
```

## Technical Architecture
1. **Clipboard:** `pyperclip` reads/writes clipboard.
2. **Platform Detection:** `platform.system()` selects the right paste command.
3. **Paste Simulation:**
   - Linux: `xdotool key ctrl+v`
   - macOS: `cliclick t:cmd+v`
   - Windows: `win32api.keybd_event`

## Limitations
- **Daemon Mode:** Not yet implemented (requires `pynput` for keyboard hooks).
- **HTML/RTF:** Only strips plaintext formatting (no HTML/RTF parsing).

## License
MIT