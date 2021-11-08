#!/bin/bash
virtualenv .
./scripts/install-smartpy.sh local-install bin
cd bin && ln -sf SmartPy.sh spy && cd ..
