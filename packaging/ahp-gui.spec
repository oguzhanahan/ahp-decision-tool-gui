# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec for AHP Decision Tool v1.0 - Single-file executable build.

This produces a standalone one-file GUI application.

Usage (on a machine with Python + tkinter + deps installed):
    pyinstaller ahp-gui.spec

Requirements for builder:
    pip install pyinstaller numpy scipy pandas matplotlib customtkinter fpdf2

The resulting dist/ahp-gui (or ahp-gui.exe on Windows) is fully self-contained.

MISRA / project rules: This spec keeps the spirit of small, reviewable units.
All runtime code remains in the original <=250 LOC modules.
"""

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Collect matplotlib data (critical for plots in results/sensitivity)
matplotlib_datas = collect_data_files('matplotlib', include_py_files=False)

# Collect customtkinter assets if any (images, themes)
customtkinter_datas = collect_data_files('customtkinter', include_py_files=False)

# Hidden imports that static analysis often misses
hiddenimports = [
    'customtkinter',
    'darkdetect',
    'fpdf',
    'PIL',
    'PIL._tkinter_finder',
    'numpy',
    'scipy',
    'scipy.linalg',
    'scipy.sparse',
    'pandas',
    'matplotlib',
    'matplotlib.backends.backend_tkagg',
    'matplotlib.figure',
    'matplotlib.pyplot',
    'tkinter',
    'tkinter.ttk',
    'tkinter.filedialog',
    'tkinter.messagebox',
]

# Add all submodules for safety (small overhead, reliable)
hiddenimports += collect_submodules('ahp_tool')

a = Analysis(
    ['src/ahp_tool/gui/app.py'],  # or use the entry point script
    pathex=[os.path.abspath('src')],
    binaries=[],
    datas=[
        *matplotlib_datas,
        *customtkinter_datas,
        # Include example data if present in future
        # ('examples/car_purchase.json', 'ahp_tool/examples'),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'pytest', 'hypothesis', 'ruff', 'mypy',  # dev only
        'tkinter.test',  # not needed
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ahp-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # compress if UPX available (optional)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI app, no console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.ico',  # add later if icon created
)

# For one-folder mode (uncomment if you prefer folder over single file for easier debug)
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=True,
#     upx_exclude=[],
#     name='ahp-gui',
# )
