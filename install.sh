#!/bin/bash

echo -e "\033c"

if [ ! -d venv ];then
  python -m venv venv
fi

python.exe -m pip install --upgrade pip
python.exe -m pip install -r requirements.txt

