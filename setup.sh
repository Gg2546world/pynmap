#!/bin/bash

INSTALL_DIR=$(pwd)
BIN_DIR="$PREFIX/bin"

echo "[*] Starting pynmap installation..."

echo "[*] Installing dependencies from requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "[!] Warning: requirements.txt not found, skipping pip install."
fi

echo "[*] Creating global command..."
cat <<EOF > "$BIN_DIR/pynmap"
#!/bin/bash
python "$INSTALL_DIR/main.py" "\$@"
EOF

chmod +x "$BIN_DIR/pynmap"

echo "[+] Success! You can now use 'pynmap' command from anywhere."
