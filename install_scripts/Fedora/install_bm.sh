#!/usr/bin/sh

rpm -qs fzf &>/dev/null || sudo dnf install fzf
ls $HOME/.local/bin &>/dev/null || mkdir -p $HOME/.local/bin
curl -sS https://raw.githubusercontent.com/madx/bm/main/bm > $HOME/.local/bin/bm
chmod +x $HOME/.local/bin/bm
