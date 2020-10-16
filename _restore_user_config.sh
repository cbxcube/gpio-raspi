#!/bin/bash

cp user_config_files/_etc_motd /etc/motd
chmod 644 /etc/motd
cp user_config_files/_root_.bash_profile /root/.bash_profile
chmod 644 /root/.bash_profile
cp user_config_files/_root_.bashrc /root/.bashrc
chmod 644 /root/.bashrc
cp user_config_files/_home_pi_.ssh_authorized_keys /home/pi/.ssh/authorized_keys
chmod 600 /home/pi/.ssh/authorized_keys
chown pi:pi /home/pi/.ssh/authorized_keys
echo "Files restored"
exit 0
