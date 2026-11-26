# 911 (992.2) Precision Night Cockpit — zsh-syntax-highlighting (0.8.0+)
# Race-Tex Charcoal (#141619), Ice Grey (#dadad6), Guards/Carmine Red (#e55c5a)
# Source after zsh-syntax-highlighting.zsh in a truecolor-capable terminal.

typeset -gA ZSH_HIGHLIGHT_STYLES
typeset -gA ZSH_HIGHLIGHT_PATTERNS

# Enable main, brackets, pattern, cursor, and root highlighters
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor root)

# Main highlighter — core & commands
ZSH_HIGHLIGHT_STYLES[default]='fg=#dadad6'
ZSH_HIGHLIGHT_STYLES[unknown-token]='fg=#e56c6a,bold'
ZSH_HIGHLIGHT_STYLES[reserved-word]='fg=#b488cc'
ZSH_HIGHLIGHT_STYLES[arg0]='fg=#7fb887'
ZSH_HIGHLIGHT_STYLES[command]='fg=#7fb887'
ZSH_HIGHLIGHT_STYLES[hashed-command]='fg=#7fb887'
ZSH_HIGHLIGHT_STYLES[alias]='fg=#7fb887'
ZSH_HIGHLIGHT_STYLES[suffix-alias]='fg=#7fb887,underline'
ZSH_HIGHLIGHT_STYLES[global-alias]='fg=#6ac4cb'
ZSH_HIGHLIGHT_STYLES[builtin]='fg=#6fa2de'
ZSH_HIGHLIGHT_STYLES[function]='fg=#6fa2de'
ZSH_HIGHLIGHT_STYLES[precommand]='fg=#98ce9f,underline'
ZSH_HIGHLIGHT_STYLES[autodirectory]='fg=#98ce9f,underline'
ZSH_HIGHLIGHT_STYLES[commandseparator]='fg=#e55c5a'

# Main highlighter — paths, globs & history
ZSH_HIGHLIGHT_STYLES[path]='fg=#dadad6,underline'
ZSH_HIGHLIGHT_STYLES[path_pathseparator]='fg=#9297a2'
ZSH_HIGHLIGHT_STYLES[path_prefix]='fg=#b4b7be,underline'
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]='fg=#9297a2'
ZSH_HIGHLIGHT_STYLES[globbing]='fg=#8cb9f2'
ZSH_HIGHLIGHT_STYLES[history-expansion]='fg=#caa2e0'

# Main highlighter — substitutions & arithmetic
ZSH_HIGHLIGHT_STYLES[command-substitution]='fg=#dadad6'
ZSH_HIGHLIGHT_STYLES[command-substitution-unquoted]='fg=#dadad6'
ZSH_HIGHLIGHT_STYLES[command-substitution-quoted]='fg=#e0be66'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]='fg=#b488cc'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-unquoted]='fg=#b488cc'
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter-quoted]='fg=#caa2e0'
ZSH_HIGHLIGHT_STYLES[process-substitution]='fg=#dadad6'
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]='fg=#b488cc'
ZSH_HIGHLIGHT_STYLES[arithmetic-expansion]='fg=#e89158'

# Main highlighter — options, quotes & escapes
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]='fg=#b4b7be'
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]='fg=#b4b7be'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]='fg=#dadad6'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-unclosed]='fg=#f48583,underline'
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]='fg=#b488cc'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]='fg=#e0be66'
ZSH_HIGHLIGHT_STYLES[single-quoted-argument-unclosed]='fg=#f48583,underline'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]='fg=#e0be66'
ZSH_HIGHLIGHT_STYLES[double-quoted-argument-unclosed]='fg=#f48583,underline'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]='fg=#f0d282'
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument-unclosed]='fg=#f48583,underline'
ZSH_HIGHLIGHT_STYLES[rc-quote]='fg=#6ac4cb'
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]='fg=#6ac4cb'
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]='fg=#84d8de'
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]='fg=#84d8de'

# Main highlighter — assignments, redirections & comments
ZSH_HIGHLIGHT_STYLES[assign]='fg=#edede9'
ZSH_HIGHLIGHT_STYLES[redirection]='fg=#e89158'
ZSH_HIGHLIGHT_STYLES[named-fd]='fg=#ad7f66'
ZSH_HIGHLIGHT_STYLES[numeric-fd]='fg=#ad7f66'
ZSH_HIGHLIGHT_STYLES[comment]='fg=#858a96'

# Brackets highlighter (5-level cycle + matching pair + error pill)
ZSH_HIGHLIGHT_STYLES[bracket-error]='fg=#f48583,bg=#2a2124,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-1]='fg=#6fa2de,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-2]='fg=#e0be66,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-3]='fg=#7fb887,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-4]='fg=#b488cc,bold'
ZSH_HIGHLIGHT_STYLES[bracket-level-5]='fg=#6ac4cb,bold'
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]='fg=#edede9,bg=#292d36,bold,underline'

# Pattern highlighter — destructive rm -rf / rm -fr redline badge (4.84:1 AA)
ZSH_HIGHLIGHT_PATTERNS+=('rm -(rf|fr)' 'fg=#f4f3ef,bg=#bf3b3e,bold')
ZSH_HIGHLIGHT_PATTERNS+=('rm (-r -f|-f -r)' 'fg=#f4f3ef,bg=#bf3b3e,bold')

# Cursor, root & line highlighters
ZSH_HIGHLIGHT_STYLES[cursor]='bg=#292d36'
ZSH_HIGHLIGHT_STYLES[root]='fg=#f4f3ef,bg=#bf3b3e,bold'
ZSH_HIGHLIGHT_STYLES[line]='none'
