# Fallback Installation

Due to GitHub API restrictions, this project is published as a tarball release. To install:

```bash
# Download and extract the release
wget https://github.com/fairyfemirins/unpaste/releases/download/v0.1.0/unpaste-0.1.0.tar.gz
mkdir -p unpaste && tar -xzvf unpaste-0.1.0.tar.gz -C unpaste

# Run the static prototype
cd unpaste/static
python3 -m http.server 8000
```

Open `http://localhost:8000` in your browser to try the demo.