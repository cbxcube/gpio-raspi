#!/bin/bash

echo "Name of functional settup - backup directory name"
read projectname
echo "Creating backup directory $projectname"
mkdir /root/gpio-raspi/bkp/display_config/$projectname
cd /root/gpio-raspi/bkp/display_config/$projectname
if [ $? == 0 ]; then
	echo "Backup directory created successfully. Path:"
	pwd
else
	echo "Failed to create backup direcotry. Exiting."
	exit 1
fi


copy_status() {
	if [ $? == 0 ]; then
		echo "file backed up successfully"
		ls -latr |tail -1
	else 
		echo "file failed to be backed up"
	fi
}


cp /etc/rc.local _etc_rc.local
copy_status
cp /etc/modprobe _etc_modprobe
copy_status
cp -R /etc/modprobe.d .
copy_status
cp /etc/modprobe.d/raspi-blacklist.conf _etc_modprobe.d_raspi-blacklist.conf
copy_status
# indicate target with "." to keep original name
cp /usr/share/X11/xorg.conf.d/99-*.conf .
copy_status
cp /etc/modules _etc_modules
copy_status

cd - 


echo "Files backed up in "bkp/display_config" directory. Commit changes to GIT!"
exit 0
