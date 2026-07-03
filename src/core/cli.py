import os
import sys
import subprocess
from . import daemon
from . import state
from . import tui

TERMINALS = ["foot", "alacritty", "kitty", "ghostty", "wezterm", "xterm"]

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "refresh":
        state.trigger_refresh()
    elif len(sys.argv) > 1 and sys.argv[1] == "daemon":
        sys.stderr = open('/tmp/waybar-ai-status-error.log', 'w')
        daemon.run()
    elif len(sys.argv) > 1 and sys.argv[1] == "config":
        if not sys.stdout.isatty():
            for term in TERMINALS:
                if subprocess.run(["which", term], capture_output=True).returncode == 0:
                    subprocess.Popen([term, "-e", sys.argv[0], "config"])
                    break
            return
        tui.run()
    else:
        print("Usage: waybar-ai-status [daemon|refresh|config]")
        sys.exit(1)
