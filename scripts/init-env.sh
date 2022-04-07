#!/bin/bash
rm -Rf bin pyvenv.cfg
wget https://smartpy.io/cli/install.sh
chmod +x install.sh
./install.sh --prefix bin
rm install.sh
virtualenv .
cd bin && ln -sf SmartPy.sh spy && cd ..
