#!/usr/bin/sh

rpm -qs fzf || sudo dnf install fzf
curl -sS https://raw.githubusercontent.com/madx/bm/main/bm > $HOME/.local/bin/bm
chmod +x $HOME/.local/bin/bm
