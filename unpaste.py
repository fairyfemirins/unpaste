#!/usr/bin/env python3
"""
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

if __name__ == "__main__":
    main()