from cx_Freeze import setup, Executable
import sys

# Files to include
include_files = [
    'client/'  # Include all files in this folder
]

# Build options
build_exe_options = {
    'packages': ['os', 'json', 'tkinter', 'customtkinter', 'pickle', 'requests'],  # Add any extra packages your script needs
    'include_files': include_files,  # Include additional files
}


if sys.platform == 'win32':
    base = 'Win32GUI'


# Executable configuration
executables = [
    Executable(
        'gui.py',  # Main script file
        target_name='BoardGameBorrow',  # macOS apps don't need ".app" suffix in the target name
        base=base
    )
]

# Setup script
setup(
    name='BoardGameBorrow',
    version='1.0',
    description='Share your board games with friends',
    options={'build_exe': build_exe_options},
    executables=executables
)