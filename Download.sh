#!/bin/bash

# this File is For linux users
# before Run this file install python virtualenv on you System

Download(){
	echo $(wget https://github.com/kooshakoosha/Dynamometer.git)
	echo $(sudo apt install python3-pip)
	echo $(apt-get install python3-virtualenv)
	echo $(unzip Dynamometer-master.zip)
	echo $(cd Dynamometer-master)
	echo $(source venv/bin/activate)
	echo $(pip3 install -r requirement.txt)
}





