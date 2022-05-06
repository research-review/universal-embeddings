#!/bin/bash

# To be executed in parent directory
if ! test -f "README.md"; then
    echo "README.md file not found in current directory. Canceling."
    exit
fi

rsync -aP --exclude={'instance','__pycache__','.*'} ./ user@embeddings.cs.uni-xxx.de:/tmp/embeddings.cc
