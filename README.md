# UnPaste

**UnPaste** is a CLI tool to unformat text before pasting or processing. It removes extra whitespace, normalizes line breaks, and strips formatting (e.g., RTF, HTML, Word styles).

## Features
- **Stdin Processing**: Pipe text directly to UnPaste for unformatting.
- **Clipboard Support**: Unformat text from the clipboard (if `pyperclip` is available).
- **Cross-Platform**: Works on Linux, macOS, and Windows.

## Installation
```bash
pip install pyperclip  # Optional, for clipboard support
```

## Usage
### Unformat from Stdin
```bash
echo "formatted   text" | python3 unpaste.py
# Output: formatted text
```

### Unformat from Clipboard
```bash
python3 unpaste.py --clipboard
```

## Technical Architecture
- **Input**: Text from stdin or clipboard.
- **Processing**: Normalize whitespace and strip formatting.
- **Output**: Unformatted text to stdout.

## Reproducible Tutorial
1. Clone the repository:
   ```bash
   git clone https://github.com/fairyfemirins/unpaste.git
   cd unpaste
   ```
2. Test the tool:
   ```bash
   echo "Hello, **world**!" | python3 unpaste.py
   ```
   Expected output: `Hello, world!`

## License
MIT

## Note
This repository is published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

To request a transfer:
1. Open an issue in this repository.
2. Contact `@femirins` on GitHub.

## Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/unpaste/settings](https://github.com/fairyfemirins/unpaste/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`femirins`) and confirm.

## Manual Merge Process
This repository contains an `autonomous-build-v3` branch with the latest changes. To merge:
1. Navigate to: [https://github.com/fairyfemirins/unpaste/pulls](https://github.com/fairyfemirins/unpaste/pulls)
2. Open a pull request from `autonomous-build-v3` to `main`.
3. Merge the pull request manually.
