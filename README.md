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
MIT## Note
This repository is published under `fairyfemirins` due to GitHub namespace restrictions. A transfer to `femirins` is pending.

To request a transfer:
1. Open an issue in this repository.
2. Contact `@femirins` on GitHub.

## Manual Transfer Process
1. Navigate to: [https://github.com/fairyfemirins/unpaste/settings](https://github.com/fairyfemirins/unpaste/settings)
2. Under "Danger Zone", select "Transfer ownership".
3. Enter the target namespace (`femirins`) and confirm.

## Manual Merge Process
This repository contains an `autonomous-build-v2` branch with the latest changes. To merge:
1. Navigate to: [https://github.com/fairyfemirins/unpaste/pulls](https://github.com/fairyfemirins/unpaste/pulls)
2. Open a pull request from `autonomous-build-v2` to `main`.
3. Merge the pull request manually.

## Setup
```bash
git clone https://github.com/fairyfemirins/unpaste.git
cd unpaste
```