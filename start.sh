#!/bin/bash

pip install --upgrade pip
pip install virtualenv
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python bot.py