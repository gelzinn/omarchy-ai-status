# Updates

To update to the latest version, run the install script again:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/gelzinn/omarchy-ai-status/main/install.sh)
```

Or if you have the repo cloned locally:

```bash
./install.sh
```

The script detects that Omarchy AI Status is already installed and pulls the latest changes from the repository automatically.

## How it works

The install script clones the repository to `~/.local/share/omarchy-ai-status/` on first run. On subsequent runs, it detects the existing `.git` directory and runs `git pull --ff-only` to fetch and apply the latest updates.
