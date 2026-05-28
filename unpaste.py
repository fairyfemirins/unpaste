#!/usr/bin/env python3
"""
Unpaste: Cross-platform CLI tool to paste unformatted text.
Strips formatting (e.g., from Microsoft Office) when pasting.

Usage:
  unpaste          # Paste unformatted text to stdout
  unpaste --clip   # Copy unformatted text to clipboard
"""

import sys
import pyperclip
import argparse
from typing import Optional


def strip_formatting(text: str) -> str:
    """Remove formatting from text (e.g., RTF, HTML)."""
    return text.encode('ascii', 'ignore').decode('ascii')


def main() -> None:
    parser = argparse.ArgumentParser(description='Paste unformatted text.')
    parser.add_argument('--clip', action='store_true', help='Copy unformatted text to clipboard')
    args = parser.parse_args()

    try:
        clipboard_text = pyperclip.paste()
        unformatted_text = strip_formatting(clipboard_text)
        
        if args.clip:
            pyperclip.copy(unformatted_text)
            print("Unformatted text copied to clipboard.")
        else:
            print(unformatted_text)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()