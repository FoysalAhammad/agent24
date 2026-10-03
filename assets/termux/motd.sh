#!/data/data/com.agnt24/files/usr/bin/bash

# Setup TERMUX_APP_PACKAGE_MANAGER
source "/data/data/com.agnt24/files/usr/bin/termux-setup-package-manager" || exit 1

terminal_width="$(stty size | cut -d" " -f2)"
if [[ "$terminal_width" =~ ^[0-9]+$ ]] && [ "$terminal_width" -gt 60 ]; then

    motd="
 \e[47m                \e[0m  \e[1mWelcome to Agent 24!\e[0m
 \e[47m  \e[0m            \e[0;37m\e[47m .\e[0m
 \e[47m  \e[0m  \e[47m  \e[0m        \e[47m  \e[0m  \e[1mDocs:\e[0m      \e[4mhttps://foysalahammad.github.io/agent24\e[0m
 \e[47m  \e[0m  \e[47m  \e[0m        \e[47m  \e[0m  \e[1mRepo:\e[0m      \e[4mhttps://github.com/FoysalAhammad/agent24\e[0m
 \e[47m  \e[0m            \e[47m  \e[0m  \e[1mIssues:\e[0m   \e[4mhttps://github.com/FoysalAhammad/agent24/issues\e[0m
 \e[47m  \e[0m            \e[0;37m\e[47m .\e[0m
 \e[47m                \e[0m  \e[1mAgent 24 version:\e[0m ${TERMUX_VERSION-Unknown}
"

    motd_indent="                   "

else

    motd="
\e[1mWelcome to Agent 24!\e[0m

\e[1mDocs:\e[0m      \e[4mhttps://foysalahammad.github.io/agent24\e[0m
\e[1mRepo:\e[0m      \e[4mhttps://github.com/FoysalAhammad/agent24\e[0m
\e[1mIssues:\e[0m   \e[4mhttps://github.com/FoysalAhammad/agent24/issues\e[0m

\e[1mAgent 24 version:\e[0m ${TERMUX_VERSION-Unknown}
"

    motd_indent=""
fi

motd+="
${motd_indent}\e[1mWorking with packages:\e[0m
${motd_indent}\e[1mSearch:\e[0m  pkg search <query>
${motd_indent}\e[1mInstall:\e[0m pkg install <package>
${motd_indent}\e[1mUpgrade:\e[0m pkg upgrade
"


if [ "$TERMUX_APP_PACKAGE_MANAGER" = "apt" ]; then

    motd+="
${motd_indent}\e[1mSubscribing to additional repos:\e[0m
${motd_indent}\e[1mRoot:\e[0m pkg install root-repo
${motd_indent}\e[1mX11:\e[0m  pkg install x11-repo

${motd_indent}For fixing any repository issues,
${motd_indent}try 'termux-change-repo' command.
"

fi

motd+="
${motd_indent}Report issues at \e[4mhttps://github.com/FoysalAhammad/agent24/issues\e[0m
"

echo -e "$motd"
