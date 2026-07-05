@echo off
REM Build script for AHP Decision Tool single-file .exe on Windows
setlocal

echo === AHP Decision Tool v1.0 Single-EXE Builder (Windows) ===

if not exist ".build_venv" (
    python -m venv .build_venv
)
call .build_venv\Scripts\activate.bat

echo Installing build dependencies...
python -m pip install --upgrade pip
python -m pip install pyinstaller numpy scipy pandas matplotlib customtkinter fpdf2

echo Building single-file executable...
pyinstaller --clean ahp-gui.spec

echo.
echo Build complete!
echo Executable: dist\ahp-gui.exe

echo.
echo You can now distribute dist\ahp-gui.exe as a standalone application.
pause
