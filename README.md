# Getting Started with the EasyBuild Local Directory

This guide will help you get started with using the EasyBuild repository for local software installations. Follow the steps below to set up your environment, build software, and manage your installations.

### Table of Contents

- [Getting Started with the EasyBuild Local Directory](#getting-started-with-the-easybuild-local-directory)
    - [Table of Contents](#table-of-contents)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Your Environment](#2-set-up-your-environment)
  - [3. Install Software Locally](#3-install-software-locally)
  - [4. Use Locally Installed Software](#4-use-locally-installed-software)
  - [5. Reset the Environment (Optional)](#5-reset-the-environment-optional)
  - [6. Manage Conda Environments (Optional)](#6-manage-conda-environments-optional)
  - [Additional Resources](#additional-resources)

## 1. Clone the Repository

First, clone the repository to your local machine:

```
git clone https://github.com/colbrydi/easybuild_local.git
```

Navigate to the repository directory:

```
cd easybuild_local
```

## 2. Set Up Your Environment

To begin using EasyBuild in this repository, you need to set up your environment by sourcing the `activate_easybuild_local.sh` script. This script loads the necessary modules and points EasyBuild to the local configuration file.

Run the following command:

```
source activate_easybuild_local.sh
```

This will load EasyBuild and configure it to use the paths defined in `config.cfg`.

## 3. Install Software Locally

Once your environment is set up, you can start installing software locally using EasyBuild. The repository contains EasyBuild configuration files (`.eb` files) for several software packages in the `easyconfigs/` directory.

To install a software package, run:

```
eb --parallel=8 --robot ./easyconfigs/<FILENAME>.eb
```

Replace `<FILENAME>` with the name of the configuration file you want to build.

For example, to build QGIS, you would run:

```
eb --parallel=8 --robot ./easyconfigs/QGIS-3.28.1-foss-2023a.eb
```

## 4. Use Locally Installed Software

After the installation is complete, you can make the locally installed software available by running the following script:

```
source eb_local_use.sh
```

This adds the locally installed modules to the module search path, allowing you to load and use them.

For example, to load QGIS, you would run:

```
module load QGIS
```

## 5. Reset the Environment (Optional)

If you need to clean up your environment and reset the installation directories, you can use the `eb_local_reset.sh` script. This script will delete the `software/` directory and recreate the necessary directories for a fresh start. This will also deactivate your conda environment.

To reset the environment, run:

```
source eb_local_reset.sh
```

## 6. Manage Conda Environments (Optional)

If your build requires Python-based dependencies, you might need to manage Conda environments. The repository provides a script, `enableconda.sh`, to help with this.

To activate a Conda environment, you first need to load the `Conda/3` module then run this script.

```
module load Conda/3
source enableconda.sh
```

This script sets up Conda and activates the `base` environment by default. You can customize this as needed for your project.



## Additional Resources

- [EasyBuild Documentation](https://easybuild.readthedocs.io/)
- [EasyBuild EasyConfigs](https://github.com/easybuilders/easybuild-easyconfigs)