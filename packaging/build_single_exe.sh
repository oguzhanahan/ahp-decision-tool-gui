#!/bin/bash
# Build script for AHP Decision Tool single-file executable
# Run this on a clean machine with Python 3.10+ and desktop environment

set -e

echo "=== AHP Decision Tool v1.0 Single-EXE Builder ==="

# Create venv (recommended)
if [ ! -d ".build_venv" ]; then
    python -m venv .build_venv
fi
source .build_venv/bin/activate

echo "Installing build dependencies..."
pip install --upgrade pip
pip install pyinstaller numpy scipy pandas matplotlib customtkinter fpdf2

echo "Building single-file executable (this may take 30-90 seconds)..."
pyinstaller --clean ahp-gui.spec

echo ""
echo "✅ Build complete!"
echo "   Executable location: dist/ahp-gui"
echo ""
echo "You can now distribute 'dist/ahp-gui' as a standalone application."
echo "Test it with: ./dist/ahp-gui"
