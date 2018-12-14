# IOT Home GC Project

## Build your Raspberry Pi as your development workstation

Download Raspbian Stretch from here:
<https://www.raspberrypi.org/downloads/raspbian/>
I used the 10-29-2018 version, but newer should be better

You can use these instructions if you need help burning the SD Card
<https://trendblog.net/install-raspbian-sd-card-os-x-windows/>

Boot up your Pi and run through the prompts to configure the locality, connect it to your network and update the software.

## Build the Directory structure

Open a terminal window and perform the following commands:

	sudo apt update
	sudo apt upgrade
	sudo apt install virtualenv

	cd ~/Desktop
	mkdir gcprojects
	cd gcprojects
	mkdir virtualenvs
	mkdir redis
	

## Install and start Redis

To install and start Redis perform the following commands:

	cd ~/Desktop/gcprojects/redis
	sudo apt install tcl
	wget http://download.redis.io/redis-stable.tar.gz
	tar xvzf redis-stable.tar.gz
	cd redis-stable
	make
	cd src
	sudo cp redis-server /usr/local/bin
	sudo cp redis-cli /usr/local/bin
	
Open a separate terminal window and run 

	redis-server

Let that terminal window run in the background while you perform the next steps on a different terminal.

## Build and Start your Virtual Environment

	cd ~/Desktop/gcprojects/virtualenvs
	sudo apt install virtualenv
	virtualenv -p /usr/bin/python3 iothome
	source iothome/bin/activate

You should now have “(iothome)” to the left of your command prompt indicating a virtual environment.  You want to perform all of the following commands with that virtual environment active.


## Git Clone the IOT Home Server and install Dependencies

	cd ~/Desktop/gcprojects
	git clone https://github.com/merlit64/iothome.git

This will create the iothome directory and add the project files on your local computer, as well as initiate the git synchronization between the development workstation and GitHub.

Now install all package requirements.

	cd ~/Desktop/gcprojects/iothome
	pip3 install -r requirements.txt
	
## Run the Django Project and test

From the command line:

	cd ~/Desktop/gcprojects/iothome
	pip install django
	ifconfig
	python3 manage.py runserver x.x.x.x:8000
	
Now browse to http://x.x.x.x:8000/discovery
You should be able to type into the lower text box and hit send.  It should move to the upper text box
Now browse to the same URL from another PC on the network.  You should be able to type text in the lower text box and hit send and it should show up in both text boxes


##  Next Steps

What we have here is Web Sockets.  We will use Web Sockets to receive communications from our Raspberry Pi relays and from Alexa.
The next goals are to build those relays devices and Alexa apps and have them communicate back to the server through Web Sockets.





