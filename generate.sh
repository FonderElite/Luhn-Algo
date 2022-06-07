#!/bin/bash
ARG=$1
sudo python3 banner.py
for i in {1..$ARG};
do
sudo python3 luhn_prototype
done
