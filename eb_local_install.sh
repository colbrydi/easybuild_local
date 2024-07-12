#!/bin/bash

# Load EasyBuild module
module purge
module load EasyBuild

# Export configuration path
export EASYBUILD_CONFIGFILES=./config.cfg

# Download the AppImage
# wget https://releases.lmstudio.ai/linux/x86/0.2.27/beta/LM_Studio-0.2.27.AppImage -P LM_Studio_module/sources

# Build the module
#eb LM_Studio_module/easyconfigs/LM_Studio-0.2.27.eb --robot
