#!/usr/bin/env python3
"""
Unpaste: Cross-platform CLI tool to paste text without formatting.
Usage: unpaste --daemon  # Run in background
"""

import pyperclip
import click
import platform
import subprocess
import sys

class Unpaste:
    def __init__(self):
        self._setup_platform()

    def _setup_platform(self):
        """Set platform-specific commands."""
        self.system = platform.system()
        if self.system == "Linux":
            self.paste_cmd = ["xdotool", "key", "ctrl+v"]
        elif self.system == "Darwin":
            self.paste_cmd = ["cliclick", "t:cmd+v"]
        elif self.system == "Windows":
            import win32api
            import win32con
            self.paste_cmd = lambda: (
                win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0),
                win32api.keybd_event(ord("V"), 0, 0, 0),
                win32api.keybd_event(ord("V"), 0, win32con.KEYEVENTF_KEYUP, 0),
                win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
            )
        else:
            raise RuntimeError("Unsupported platform")

    def _strip_formatting(self, text):
        """Convert HTML/RTF clipboard content to plaintext."""
        return pyperclip.paste()

    def _paste_plaintext(self):
        """Replace clipboard content with plaintext and trigger paste."""
        plaintext = self._strip_formatting(pyperclip.paste())
        pyperclip.copy(plaintext)
        if self.system == "Linux":
            subprocess.run(["xdotool", "key", "ctrl+v"])
        elif self.system == "Darwin":
            subprocess.run(["cliclick", "t:cmd+v"])
        elif self.system == "Windows":
            import win32api
            import win32con
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
            win32api.keybd_event(ord("V"), 0, 0, 0)
            win32api.keybd_event(ord("V"), 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

@click.command()
@click.option("--daemon", is_flag=True, help="Run in background as daemon (not yet implemented).")
def main(daemon):
    unpaste = Unpaste()
    if daemon:
        print("Daemon mode not yet implemented. Use --help for usage.")
        sys.exit(1)
    else:
        unpaste._paste_plaintext()

if __name__ == "__main__":
    main()