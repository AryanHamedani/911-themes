# 911 (992.2) Precision Night Cockpit — fzf (0.74+)
# 4-plane cockpit hierarchy: Deep Carbon preview (#0c0e11), Race-Tex chrome
# input/header/footer (#131519), Race-Tex Charcoal list (#141619), Smoked
# Carmine active row (#261b1f), Slate Grey Neo multi-select (#292d36),
# Guards Red instrument needle (#e55c5a), and PCCB/Weissgold match highlights.
#
# POSIX-compatible: prepends cockpit layout ergonomics so user flags already in
# FZF_DEFAULT_OPTS take precedence, then appends the 44-role 911 --color spec.

export FZF_DEFAULT_OPTS="--layout=reverse --border=rounded --info=inline-right --prompt='› ' --pointer='▌' --marker='┃' --separator='─' --scrollbar='▎' --ellipsis='…' --scroll-off=3 --highlight-line${FZF_DEFAULT_OPTS:+ $FZF_DEFAULT_OPTS} --color=fg:#dadad6,bg:#141619,list-fg:#dadad6,list-bg:#141619,hl:#e0be66:bold,fg+:#edede9,bg+:#261b1f,hl+:#f0d282:bold,gutter:#141619,selected-bg:#292d36,selected-fg:#edede9,selected-hl:#f0d282:bold,query:#edede9:regular,ghost:#858a96:regular,disabled:#858a96:regular,nomatch:#858a96:regular,info:#9297a2,prompt:#e55c5a:bold,pointer:#e55c5a:bold,marker:#7fb887:bold,spinner:#6ac4cb,header:#b4b7be,header-bg:#131519,footer:#9297a2,footer-bg:#131519,input-bg:#131519,preview-bg:#0c0e11,preview-fg:#dadad6,border:#434854,list-border:#2f3440,input-border:#434854,header-border:#2f3440,footer-border:#2f3440,preview-border:#2f3440,label:#b4b7be:bold,list-label:#b4b7be,input-label:#edede9:bold,header-label:#6fa2de,footer-label:#9297a2,preview-label:#b4b7be,scrollbar:#434854,preview-scrollbar:#434854,separator:#2f3440,gap-line:#252932"
