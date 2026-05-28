# UnPaste

UnPaste is a lightweight CLI tool to remove formatting from text. It works in headless environments and has **no dependencies**.

## Problem
Users frequently copy formatted text (e.g., from Word, web pages) and need to paste it as plain text. Existing tools (e.g., PureText) are Windows-only or require GUI dependencies.

## Solution
UnPaste strips formatting from stdin or files and outputs plain text to stdout.

## Usage
```bash
# From stdin
echo "Hello, **world**!" | python3 unpaste.py
# Output: Hello, world!

# From file
python3 unpaste.py < input.txt
```

## Technical Architecture
- **Input**: stdin or file.
- **Processing**: Regex to remove Markdown/HTML formatting.
- **Output**: Plain text to stdout.
- **Dependencies**: None.

## Reproducible Tutorial
1. Clone the repository:
   ```bash
   git clone https://github.com/femirins/unpaste.git
   cd unpaste
   ```
2. Test the tool:
   ```bash
   echo "Hello, **world**!" > input.txt
   python3 unpaste.py < input.txt
   ```
   Expected output: `Hello, world!`

## License
MIT