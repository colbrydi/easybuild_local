#!/bin/bash

# Source this file to set up easybuild to run in the current directory.

# Load EasyBuild module
module purge
module load EasyBuild

# Export configuration path
export EASYBUILD_CONFIGFILES=./config.cfg

