# IOT Home GC Project

## Build your Raspberry Pi as your development workstation

Download Raspbian Stretch from here:
<https://www.raspberrypi.org/downloads/raspbian/>
I used the 10-29-2018 version, but newer should be better

You can use these instructions if you need help burning the SD Card
<https://trendblog.net/install-raspbian-sd-card-os-x-windows/>

Boot up your Pi and run through the prompts to configure the locality, connect it to your network and update the software.

## Build the Environment

Open a terminal window and perform the following commands:
	sudo apt update
	sudo apt upgrade
	sudo apt install virtualenv

	cd ~/Desktop
	mkdir gcprojects
	cd gcprojects
	mkdir virtualenvs
	cd virtualenvs
	
	virtualenv -p /usr/bin/python3 iothome
	source iothome/bin/activate

You should now have “(iothome)” to the left of your command prompt indicating a virtual environment

## Git Clone the IOT Home Server

	cd ~/Desktop/gcprojects
	git clone https://github.com/merlit64/iothome

This will create the iothome directory and add the project files on your local computer, as well as initiate the git synchronization between the development workstation and GitHub





