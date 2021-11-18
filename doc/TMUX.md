Jump to tmux session named $SESSION if this session already exists otherwise start new tmux session $SESSION with one window and two frames with working directories set to $DIRLEFT and $DIRRIGHT.

If there is a client already connected to $SESSION, bring corresponding terminal window to foreground.

Set WHICHTMUX to path to tmux.
