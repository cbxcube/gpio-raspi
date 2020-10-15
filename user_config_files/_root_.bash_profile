alias ll='ls -lah'
alias ls='ls --color=auto'

alias cdio="cd /root/gpio"
alias cdiod="cd /root/gpio/displays"
alias cdiog="cd /root/gpio/gui"
alias cdiow="cd /root/gpio/workshop-kit-python-code"

alias gpiomng="/root/gpio/workshop-kit-python-code/rungpio.sh"

alias gpiotemp="cd gpio/workshop-kit-python-code/ && python 7_temperature-to-file.py"

# networking
alias networkon="route add default gw 192.168.0.1 eth0 && echo 'nameserver 8.8.8.8' >> /etc/resolv.conf"
alias routeon="route add default gw 192.168.0.1 eth0"
alias dnson="echo 'nameserver 8.8.8.8' >> /etc/resolv.conf"

# motd
cat /etc/motd

# execute
gpio readall
i2cdetect -y 1

echo "aliases: "
alias

