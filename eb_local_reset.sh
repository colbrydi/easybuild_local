#!/bin/bash

# Deletes and reset's install directory

rm -rf software
mkdir -p ./software/modules/
mkdir -p ./tempdir/


echo "Deleted and reset install directory. Suggested commands to run next:"
echo "conda deactivate"
echo "module purge"