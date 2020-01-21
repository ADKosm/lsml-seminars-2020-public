#!/usr/bin/env bash

set -e

# get link from this site - https://www.anaconda.com/distribution/

wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O install-conda.sh
chmod +x install-conda.sh
./install-conda.sh

echo "export PATH=/home/alex/anaconda3/bin:\$PATH" >> .bashrc
