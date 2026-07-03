import os

__version__ = "0.1.0"

INSTALL_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERSION_FILE = os.path.join(INSTALL_DIR, "..", "VERSION")

if os.path.exists(VERSION_FILE):
    try:
        with open(VERSION_FILE) as f:
            __version__ = f.read().strip()
    except Exception:
        pass
