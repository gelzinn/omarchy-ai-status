import sys
from . import daemon
from . import state

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "refresh":
        state.trigger_refresh()
    elif len(sys.argv) > 1 and sys.argv[1] == "daemon":
        sys.stderr = open('/tmp/waybar-ai-status-error.log', 'w')
        daemon.run()
    else:
        print("Usage: waybar-ai-status [daemon|refresh]")
        sys.exit(1)
