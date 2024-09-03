# EasyBuild and Module System Terminology & Commands

## Table of Contents
1. EasyBuild Basics
2. Common EasyBuild Commands
3. Module System Commands
4. Toolchains in EasyBuild
5. Toolchain Naming Scheme

## EasyBuild Basics

### EasyBuild
- **EasyBuild**: A software build and installation framework that automates the building, installing, and managing scientific software on HPC systems.

### EasyConfig
- **EasyConfig**: A configuration file (`*.eb`) used by EasyBuild to define how software should be built and installed, including details like dependencies, patches, and environment settings.

### EasyBlock
- **EasyBlock**: Python classes used by EasyBuild to implement the building process for specific types of software. Examples include `ConfigureMake`, `CMakeMake`, `PythonPackage`, etc.

### Build Dependencies
- **Build Dependencies**: Software or libraries required at build time but not necessarily at runtime. Defined in the `builddependencies` section of an EasyConfig.

### Runtime Dependencies
- **Runtime Dependencies**: Software or libraries required when running the installed software. Defined in the `dependencies` section of an EasyConfig.

### Toolchain
- **Toolchain**: A set of compilers, libraries, and tools used to build software. Toolchains ensure consistency and compatibility across different builds.

### Sanity Check
- **Sanity Check**: A post-installation check in EasyBuild that verifies the software was installed correctly by checking for specific files or executing commands.

## Common EasyBuild Commands

### Build and Install
- `eb Hello-2.10-GCCcore-11.2.0.eb`  # Build and install the software described in the EasyConfig file
- `eb --robot Hello-2.10-GCCcore-11.2.0.eb`  # Automatically resolve and build dependencies
- `eb --parallel=8 Hello-2.10-GCCcore-11.2.0.eb`  # Run builds in parallel using 8 cores

### Copy and Modify EasyConfigs
- `eb --copy-ec Hello-2.10-GCCcore-11.2.0.eb`  # Copy an existing EasyConfig file for modification
- `eb --try-toolchain-version=2023a Hello-2.10-GCCcore-11.2.0.eb`  # Try building with a different toolchain version

### Debugging and Logs
- `eb -d Hello-2.10-GCCcore-11.2.0.eb`  # Run EasyBuild in debug mode
- `eb --skip Hello-2.10-GCCcore-11.2.0.eb`  # Skip already completed steps (e.g., configure, build, install)
- `eb --log Hello-2.10-GCCcore-11.2.0.eb`  # Specify a custom log file location

### Environment Variables
- `export EASYBUILD_CONFIGFILES=./config.cfg`  # Use a custom EasyBuild configuration file.
  - This is used in `activate_easybuild_local.sh`.
- `export EASYBUILD_SOURCEPATH=./sources`  # Set the path for source files

## Module System Commands

### Basic Module Commands
- `module avail`  # List all available modules
- `module load Hello/2.10-GCCcore-11.2.0`  # Load the Hello module into the environment.
  - Load is used in `activate_easybuild_local.sh` to load easybuild itself.
- `module unload Hello/2.10-GCCcore-11.2.0`  # Unload the Hello module from the environment
- `module list`  # List all currently loaded modules
- `module spider Hello`  # Search for modules by keyword
- `module purge`  # Unload all currently loaded modules.
  - Purge is used in `activate_easybuild_local.sh` and suggested to be ran after `eb_local_reset.sh`.

### Custom Module Paths
- `module use ./software/modules/all`  # Add a custom path to the module search paths.
  - Use is used in `eb_local_use.sh`.
- `module unuse ./software/modules/all`  # Remove a custom path from the module search paths.
  - Unuse is used in `eb_local_reset.sh`.

### Checking Module Conflicts
- `module show Hello/2.10-GCCcore-11.2.0`  # Show the environment changes a module will make
- `module swap Hello/2.10-GCCcore-11.2.0 <modulename>`  # Swap one module for another

## Toolchains in EasyBuild

### What is a Toolchain?
A **toolchain** in EasyBuild is a set of compilers, libraries, and tools that are used together to build software. The purpose of a toolchain is to ensure consistency, compatibility, and reproducibility across different software builds.

### Types of Toolchains
- **GCCcore**: Basic toolchain based on GCC, providing a minimal environment.
- **foss**: Free and Open Source Software toolchain, usually includes GCC, OpenMPI, and other libraries.
- **intel**: Toolchain based on Intel compilers and libraries.
- **Cray**: Toolchain for Cray systems, using Cray-provided compilers and libraries.

### Toolchain Options
- **usempi**: Enable MPI (Message Passing Interface) support.
- **openmp**: Enable OpenMP (parallel programming) support.
- **pic**: Position-independent code, useful for shared libraries.
- **cstd**: Set the C/C++ standard version (e.g., `gnu++11`).

## Toolchain Naming Scheme

### Toolchain Naming Convention
The naming convention for toolchains in EasyBuild typically follows this pattern:

`<toolchain-name>-<toolchain-version>`

For example:
- **GCCcore-11.2.0**: GCC toolchain, version 11.2.0, providing basic compilers and libraries.
- **foss-2021b**: A comprehensive toolchain including GCC, OpenMPI, and other libraries, version 2021b.

### Example of Toolchain Usage in an EasyConfig
```
easyblock = 'ConfigureMake'

name = 'Hello'
version = '2.10'

homepage = 'https://www.gnu.org/software/hello/'

description = """
The GNU Hello program produces a familiar, friendly greeting. Yes, this is another
implementation of the classic program that prints "Hello, world!" when you run it.

Slightly modified to fit our modules versions. Orginal source can be found at: 
https://github.com/easybuilders/easybuild-easyconfigs/blob/develop/easybuild/easyconfigs/h/Hello/Hello-2.10-GCCcore-8.2.0.eb
"""

toolchain = {'name': 'GCCcore', 'version': '11.2.0'}

source_urls = [GNU_SOURCE]
sources = [SOURCELOWER_TAR_GZ]
checksums = ['31e066137a962676e89f69d1b65382de95a7ef7d914b8cb956f41ea72e0f516b']

builddependencies = [
    ('binutils', '2.37'),
]

sanity_check_paths = {
    'files': ['bin/hello'],
    'dirs': ['share/man/man1'],
}
sanity_check_commands = ['hello']

moduleclass = 'tools'
```

In this example, `GCCcore-11.2.0` is used as the toolchain, `binutils-2.37` is a build dependency, and `hello` is the command being checked. Try building and installing this software using the provided EasyConfig file.