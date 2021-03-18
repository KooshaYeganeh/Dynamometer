#!/bin/bash


a=$(FLASK_APP=app.py)
b=$(FLASK_ENV=development)
c=$(flask run)

echo $a
echo $b
echo $c








