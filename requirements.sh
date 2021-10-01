#!/bin/sh

linuxmodules='requirements_src/modules.txt'
echo -e "\n \e[1;32m [*] Downloading Package Information... \e[0;m \n"
yes | sudo apt-get update


cat $linuxmodules | while read module
do
	echo -e "\n \e[1;34m [+] Installing $module \e[0;m \n"
	yes | sudo apt-get install $module
done


pipmodules='requirements_src/PipModules.txt'
echo -e "\n \e[1;32m [+] INSTALLING PIP PACKAGES... \e[0;m \n"

yes | pip3 install -r $pipmodules

echo -e "\n \e[1;31m [-] Removing Unwanted Packages... \e[0;m \n"
sudo apt-get autoremove

echo -e "\n \e[1;32m [-] Cleaning Downloaded Packages..."
sudo apt-get clean
echo -e "\n \e[1;32m [√] FINISHED"