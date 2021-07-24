#!/bin/bash

# this File is For Debian base systems users
# before Run this file install python virtualenv on you System

Download(){
	echo $(wget https://github.com/kooshakoosha/Dynamometer.git)
	echo $(sudo apt install python-pip)
	echo $(sudo dnf install python3-virtualenv)
	echo $(unzip Dynamometer-master.zip)
	echo $(cd Dynamometer-master)
	echo $(source venv/bin/activate)
	echo $(pip install -r requirement.txt)
}





