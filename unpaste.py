#!/usr/bin/env python3
"""
<<<<<<< HEAD
UnPaste: A CLI utility to remove formatting from text.

Features:
- Removes formatting from input text (stdin or file).
- Outputs plain text to stdout.
- No dependencies, works in headless environments.

Usage:
  # From stdin
  echo "Hello, **world**!" | python3 unpaste.py
  
  # From file
  python3 unpaste.py < input.txt
"""

import re
import sys

def remove_formatting(text: str) -> str:
    """Remove common formatting (bold, italics, etc.) from text."""
    # Remove Markdown/HTML formatting
    text = re.sub(r'\*\*|__|\*|_|`', '', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Normalize whitespace
    text = ' '.join(text.split())
    return text

def main():
    # Read from stdin
    input_text = sys.stdin.read()
    if not input_text:
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(1)
    
    # Output plain text
    print(remove_formatting(input_text))
=======
UnPaste: A CLI tool to unformat text from stdin or clipboard.

Usage:
  echo "formatted text" | python3 unpaste.py   # Unformat from stdin
  python3 unpaste.py --clipboard             # Unformat from clipboard (if available)
"""

import sys
import argparse

class UnPaste:
    def unformat_text(self, text):
        """Remove formatting from text (e.g., RTF, HTML, Word styles)."""
        # Basic unformatting: strip whitespace, normalize line breaks
        text = " ".join(text.split()).strip()
        return text

def main():
    parser = argparse.ArgumentParser(description="UnPaste: Unformat text.")
    parser.add_argument("--clipboard", action="store_true", help="Unformat text from clipboard (if available)")
    args = parser.parse_args()

    unpaste = UnPaste()
    
    if args.clipboard:
        try:
            import pyperclip
            text = pyperclip.paste()
            unformatted = unpaste.unformat_text(text)
            print(unformatted)
        except ImportError:
            print("Error: pyperclip not available. Install with 'pip install pyperclip'")
            sys.exit(1)
    else:
        # Read from stdin
        text = sys.stdin.read()
        unformatted = unpaste.unformat_text(text)
        print(unformatted)
>>>>>>> de81701 (Initial commit: UnPaste - Unformat text before pasting (CLI tool))

if __name__ == "__main__":
    main()