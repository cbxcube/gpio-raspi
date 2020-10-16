#!/bin/bash

cp /etc/motd user_config_files/_etc_motd
cp /root/.bash_profile user_config_files/_root_.bash_profile
cp /root/.bashrc user_config_files/_root_.bashrc
cp /home/pi/.ssh/authorized_keys user_config_files/_home_pi_.ssh_authorized_keys
echo "Files backed up in "user_config_files" directory. Commit changes to GIT!"
exit 0
