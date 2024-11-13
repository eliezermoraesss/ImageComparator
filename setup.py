# setup.py
import os
from shutil import rmtree

# Configuration
PYTHON_FILE = "image_comparator.py"  # Replace with your main Python file
ICON_FILE = "image-comparator.ico"   # Replace with your icon file path
OUTPUT_DIR = "dist"                  # Output directory for the executable
BUILD_DIR = "build"                  # Build directory

# Clean previous builds
if os.path.exists(OUTPUT_DIR):
    rmtree(OUTPUT_DIR)
if os.path.exists(BUILD_DIR):
    rmtree(BUILD_DIR)

# PyInstaller command
pyinstaller_command = (
    f"pyinstaller "
    f"--noconfirm "              # Replace existing output directory
    f"--onefile "                # Create single executable file
    f"--windowed "               # Hide console window when running
    f"--icon={ICON_FILE} "       # Set custom icon
    f"--name=ImageComparator "   # Set output executable name
    f"--clean "                  # Clean cache before building
    f"{PYTHON_FILE}"             # Your main Python file
)

# Execute PyInstaller
os.system(pyinstaller_command)
