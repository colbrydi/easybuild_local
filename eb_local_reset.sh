#!/bin/bash

# Deletes and reset's install directory

rm -rf software tempdir
mkdir -p ./software/modules/
mkdir -p ./tempdir/

module unuse ./software/modules/all

echo "Deleted and reset install directory. Suggested commands to run next:"
echo "conda deactivate"
echo "module purge"