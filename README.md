# Unpaste

Strip formatting from clipboard text before pasting. Cross-platform (Linux/macOS/Windows via WSL).

## Installation
```bash
pip install pyclip
curl -o /usr/local/bin/unpaste https://raw.githubusercontent.com/femirins/unpaste/main/unpaste.py
chmod +x /usr/local/bin/unpaste
```

## Usage
1. Copy formatted text (e.g., from Word/Google Docs).
2. Run `unpaste` in terminal.
3. Paste into any plaintext editor (formatting removed).

## Technical Architecture
- **Input**: System clipboard (via `xclip`/`pbpaste`/`clip`).
- **Processing**: Plaintext extraction.
- **Output**: System clipboard (overwrites original).

## License
MIT