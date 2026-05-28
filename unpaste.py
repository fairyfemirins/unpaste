#!/usr/bin/env python3
"""
Unpaste: Strip formatting from clipboard text before pasting.
Cross-platform (Linux/macOS/Windows via WSL).
"""

import subprocess
import sys
import platform

def get_clipboard():
    """Get clipboard content."""
    system = platform.system()
    try:
        if system == "Linux":
            return subprocess.check_output(["xclip", "-o", "-selection", "clipboard"], text=True)
        elif system == "Darwin":
            return subprocess.check_output(["pbpaste"], text=True)
        elif system == "Windows":
            return subprocess.check_output(["powershell", "-command", "Get-Clipboard"], text=True)
        else:
            raise OSError("Unsupported OS")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def set_clipboard(text):
    """Set clipboard content."""
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.run(["xclip", "-selection", "clipboard"], input=text, text=True, check=True)
        elif system == "Darwin":
            subprocess.run(["pbcopy"], input=text, text=True, check=True)
        elif system == "Windows":
            subprocess.run(["powershell", "-command", "Set-Clipboard"], input=text, text=True, check=True)
        else:
            raise OSError("Unsupported OS")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    text = get_clipboard()
    set_clipboard(text.strip())
    print("Clipboard text unformatted.")

if __name__ == "__main__":
    main()